import random
import math

from .utils import create_n_rand_pts
from .utils import euclidean_distance

def p_perms(p=99,n=100):
	
	mean_nn_dist =  []
	
	for i in range(p):
		mean_nn_dist.append(average_nearest_neighbor_distance(create_n_rand_pts(100)));
	
	return mean_nn_dist

def monte_carlo_critical_bound_check(lb,ub,obs):
	return obs<lb or obs>ub
	
def minimum_bounding_rectangle(points):
    """
    Given a set of points, compute the minimum bounding rectangle.

    Parameters
    ----------
    points : list
             A list of points in the form (x,y)

    Returns
    -------
     : list
       Corners of the MBR in the form [xmin, ymin, xmax, ymax]
    """
    #set initial params
    xmin=points[1][0]
    ymin=points[1][1]
    xmax=points[1][0]
    ymax=points[1][1]
    
    for i in points:
        curr_x=i[0]
        curr_y=i[1]
        if curr_x < xmin:
            xmin= curr_x 
        elif curr_x > xmax:
            xmax= curr_x
                
        if curr_y < ymin:
            ymin= curr_y 
        elif curr_y > ymax:
            ymax= curr_y 
    mbr = [xmin,ymin,xmax,ymax]

    return mbr

def find_largest_city(gj):
    """
    Iterate through a geojson feature collection and
    find the largest city.  Assume that the key
    to access the maximum population is 'pop_max'.

    Parameters
    ----------
    gj : dict
         A GeoJSON file read in as a Python dictionary

    Returns
    -------
    city : str
           The largest city

    population : int
                 The population of the largest city
    """
    maximum=0;
    features=gj['features']
    
    for i in features:
        if (i['properties']['pop_max']>maximum):
            maximum=i['properties']['pop_max']
            city=i['properties']['nameascii']
    return city, maximum


def write_your_own(gj):
    """
    Here you will write your own code to find
    some attribute in the supplied geojson file.

    Take a look at the attributes available and pick
    something interesting that you might like to find
    or summarize.  This is totally up to you.

    Do not forget to write the accompanying test in
    tests.py!
    """
    #Calculate the number of citues with two-word names
    features=gj['features']
    count = 0
    for i in features:
        if(' ' in i['properties']['name']):
            count= count+1   
    
    return count

def mean_center(points):
    """
    Given a set of points, compute the mean center

    Parameters
    ----------
    points : list
         A list of points in the form (x,y)

    Returns
    -------
    x : float
        Mean x coordinate

    y : float
        Mean y coordinate
    """
    x_tot=0
    y_tot=0
    
    for i in points:
        x_tot+=i[0]
        y_tot+=i[1]
        
    x = x_tot/len(points)
    y = y_tot/len(points)

    return x, y


def average_nearest_neighbor_distance(points):
    """
    Given a set of points, compute the average nearest neighbor.

    Parameters
    ----------
    points : list
             A list of points in the form (x,y)

    Returns
    -------
    mean_d : float
             Average nearest neighbor distance

    References
    ----------
    Clark and Evan (1954 Distance to Nearest Neighbor as a
     Measure of Spatial Relationships in Populations. Ecology. 35(4)
     p. 445-453.
    """
    mean_d = 0
    for i in points:
        dist_nearest=1e9
        for j in points:
            dist = euclidean_distance(i, j)
            if i==j:
                continue
            elif dist < dist_nearest:
                dist_nearest = dist;
        mean_d += dist_nearest;
    mean_d=mean_d/(len(points))
    return mean_d