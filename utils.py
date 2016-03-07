import math
import random


def create_random_points(n):
    randomPoints = []
    for x in range(n):
        randomPoints.append((random.random(), random.random())

    
    return randomPoints

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
    xSum = 0
    ySum = 0

    for n in points:
        xSum += n[0]
        ySum += n[1]

    x = xSum/len(points)
    y = ySum/len(points)

    return x, y


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
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
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
