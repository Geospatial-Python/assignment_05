import math

def check_significant(lower, upper, observed_avg):
    bool significance = false
    if(upper-lower <= observed_avg)
        significance = true
    return significance 

def compute_critical(listOfAvgNNDistances):
    criticalPoints = []
    criticalPoints[0] = min(listOfAvgNNDistances)
    criticalPoints[1] = max(listOfAvgNNDistances)
    return criticalPoints;

def permutations(p):
    listOfAvgNNDistances = []
    
    for x in range(p):
        tmpList = []
        tmpList.append(create_random_points(100))
        listOfAvgNNDistances.append(average_nearest_neighbor_distance(tmpList))

    return listOfAvgNNDistances    

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
    listOfDistances = []
    
    for n in points:
        lowest = 100
        for x in points:
            if euclidean_distance(n,x)!= 0 and euclidean_distance(n,x) < lowest:
                lowest = euclidean_distance(n,x)
        listOfDistances.append(lowest)

    totalOfDistances = 0

    for z in listOfDistances:
        totalOfDistances += z

    mean_d = totalOfDistances/len(points)

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
    minX = 100
    minY = 100
    maxX = 0
    maxY = 0

    for n in points:
        if n[0] < minX:
            minX = n[0]
        if n[0] > maxX:
            maxX = n[0]
        if n[1] < minY:
            minY = n[1]
        if n[1] > maxY:
            maxY = n[1]
        
    mbr = [minX,minY,maxX,maxY]

    return mbr

def mbr_area(mbr):
    """
    Compute the area of a minimum bounding rectangle
    """
    
    area = 0

    length = mbr[3]-mbr[1]
    width = mbr[2] - mbr[0]

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
    expected = 0.5 * (math.sqrt(area/n))

    
    return expected


