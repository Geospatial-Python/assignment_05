import math
import random


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
    x=0.0
    y=0.0
    i=0

    for p in points:
        x= x + points[i][0]
        y= y + points[i][1]
        i= i + 1

    x = x/len(points)
    y = y/len(points)
    return x, y

def create_random(entries):
    rng = random.Random()
    result = []
    for i in range(entries):
        x=rng.random()
        y=rng.random()
        point=(x,y)
        result.append(point)
    return result
    
def permutations(number_of_permutations, number_of_points):


    result = []
    for i in range(number_of_permutations):
        points = create_random(number_of_points)
        observed_avg = average_nearest_neighbor_distance(points)
        result.append(observed_avg)

    return result

def compute_critical(permutations):
    lower = min(permutations)
    upper = max(permutations)

    result = lower,upper
    return result

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
    n = 1
    total = 0
    for i, p1 in enumerate(points):
        nearest = math.inf

        for j, p2 in enumerate(points):

            if i == j:
                continue

            a = p1
            b = p2
            dist = euclidean_distance(a,b)
            if dist < nearest:
                    nearest = dist

        total += nearest
        n += 1





    mean_d = total/n


    return mean_d


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
    xmin = math.inf
    xmax = 0.0
    ymin = math.inf
    ymax = 0.0
    i=0
    for p in points:
        if points[i][0]<xmin:
            xmin=points[i][0]
        if points[i][0]>xmax:
            xmax=points[i][0]
        if points[i][1]<ymin:
            ymin=points[i][1]
        if points[i][1]>ymax:
            ymax=points[i][1]
        i=i+1

    mbr = [xmin,ymin,xmax,ymax]

    return mbr


def mbr_area(mbr):
    """
    Compute the area of a minimum bounding rectangle
    """
    [xmin,ymin,xmax,ymax]=mbr
    area = (xmax-xmin)*(ymax-ymin)

    return area


def expected_distance(area, n):
    """
    Compute the expected mean distance given
    some study area.

    This makes lots of assumptions and is not
    necessarily how you would want to compute
    this.  This is just an example of the full
    analysis pipe, e.g. compute the mean distance
    and the expected mean distance.

    Parameters
    ----------
    area : float
           The area of the study area

    n : int
        The number of points
    """

    expected = 0.5*((area/n)**0.5)
    return expected


"""
Below are the functions that you created last week.
Your syntax might have been different (which is awesome),
but the functionality is identical.  No need to touch
these unless you are interested in another way of solving
the assignment
"""

def manhattan_distance(a, b):
    """
    Compute the Manhattan distance between two points

    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------
    distance : float
               The Manhattan distance between the two points
    """
    distance =  abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance


def euclidean_distance(a, b):
    """
    Compute the Euclidean distance between two points

    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------

    distance : float
               The Euclidean distance between the two points
    """

    distance = math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
    return distance




def shift_point(point, x_shift, y_shift):
    """
    Shift a point by some amount in the x and y directions

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    x_shift : int or float
              distance to shift in the x direction

    y_shift : int or float
              distance to shift in the y direction

    Returns
    -------
    new_x : int or float
            shited x coordinate

    new_y : int or float
            shifted y coordinate

    Note that the new_x new_y elements are returned as a tuple

    Example
    -------
    >>> point = (0,0)
    >>> shift_point(point, 1, 2)
    (1,2)
    """
    x = getx(point)
    y = gety(point)

    x += x_shift
    y += y_shift

    return x, y


def check_coincident(a, b):
    """
    Check whether two points are coincident
    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------
    equal : bool
            Whether the points are equal
    """
    return a == b


def check_in(point, point_list):
    """
    Check whether point is in the point list

    Parameters
    ----------
    point : tuple
            In the form (x,y)

    point_list : list
                 in the form [point, point_1, point_2, ..., point_n]
    """
    return point in point_list


def getx(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    Returns
    -------
     : int or float
       x coordinate
    """
    return point[0]


def gety(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    Returns
    -------
     : int or float
       y coordinate
    """
    return point[1]
