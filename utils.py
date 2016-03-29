import math

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
    x = 0
    y = 0
    for coor in points:
        x += coor[0]/len(points)
        y += coor[1]/len(points)

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
    shortest_path = []
    mean_d = 0

    for p_one in points:
        distance = []
        for p_two in points:
            if math.sqrt((p_one[0] - p_two[0])**2 + (p_one[1] - p_two[1])**2)==0:
                continue
            distance.append(math.sqrt((p_one[0] - p_two[0])**2 + (p_one[1] - p_two[1])**2))
        shortest_path.append(min(distance))

    mean_d = sum(shortest_path)/len(shortest_path)
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

    mbr = []
    x_list = []
    y_list = []

    for point in points:
        x_list.append(point[0])
        y_list.append(point[1])

    mbr.append(min(x_list))
    mbr.append(min(y_list))
    mbr.append(max(x_list))
    mbr.append(max(y_list))

    return mbr

def mbr_area(mbr):
    """
    Compute the area of a minimum bounding rectangle
    """
    area = 0

    length = abs(mbr[0] - mbr[2])
    width = abs(mbr[1] - mbr[3])

    area = length * width

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

    expected = 0

    expected = 0.5 * (math.sqrt(area / n))
    return expected

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