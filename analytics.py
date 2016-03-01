import math
 import random
 from utils import euclidean_distance, n_random_points

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

     featureList = gj['features']

     max_population = 0
     for featureEntry in featureList:
         if featureEntry["properties"]["pop_max"] > max_population:
             max_population = featureEntry["properties"]["pop_max"]
             city = featureEntry["properties"]["nameascii"]


     return city, max_population

 def write_your_own(gj):


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


     sums = map(sum,zip(*points))
     sumsL = list(sums)
     avgs = map(lambda xy: xy/len(points),sumsL)
     avgsL = list(avgs)
     x = avgsL[0]
     y = avgsL[1]

     return x,y

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

      shDistL =[]
     mean_sum = 0
     for point in points:
         shortestDistance = 9999999999
         for dpoint in points:
             if point != dpoint:
                 dist = euclidean_distance(point, dpoint)
                 if(shortestDistance > dist):
                     shortestDistance = dist

         shDistL.append(shortestDistance)
         mean_sum = shortestDistance + mean_sum

     print(shDistL)
     sums = sum(shDistL)
     mean_d = mean_sum/len(shDistL)
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


     xmin = 99999999999
     ymin = 99999999999
     xmax = -9999999999
     ymax = -9999999999
     for point in points:
         if point[0] < xmin:
             xmin = point[0]
         if point[1] < ymin:
             ymin = point[1]
         if point[0] > xmax:
             xmax = point[0]
         if point[1] > ymax:
             ymax = point[1]
     mbr = [xmin,ymin,xmax,ymax]

     return mbr

 def mbr_area(mbr):
     """
     Compute the area of a minimum bounding rectangle
     """
     length = mbr[2] - mbr[0]
     width  = mbr[3] - mbr[1]
     area = length*width

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

     expected = 0.5 * (math.sqrt(area/n))
     return expected


 def permutation_nearest_distance(p=99,n=100):
     """
     Finds the nearest neighbor distance for p permutations with n
     random points
     :param p: permutation number of times you want to try different
     simulations for monte carlo
     :param n: random point number
     :return LDist: list of distances, length p
     """
     LDist = []
     for x in range(p): #loop from 0 to p
         #create n random points
         points = n_random_points(n) # returns [(x,y),(a,b)..]
         #compute mean neighbor distance
         mean_d = average_nearest_neighbor_distance(points)
         LDist.append(mean_d)

     return LDist

 def critical_points(LDist):
     """
     Find the critical points, the largest/smallest distances
     :param LDist: the list of mean distances
     :return CList: list containing critical points
     """
     CList = []
     smallest = min(LDist)
     largest = max(LDist)
     CList.append(smallest)
     CList.append(largest)
     #print(CList)
     return CList

 def significant(CList,distance):
     """
     Returns True if the observed distance is significant
     :param CList: list of critical points
     :param distance: the observed distance
     :return result: True/False
     """

     if distance < CList[0] or distance > CList[1]:
         result = True
     else:
         result = False
     return result