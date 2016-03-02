"""
created feb 29th, 2016
By Eric Friesenhahn


List of stuff to do

 compute_critical(p)
 Find_largest_city(gj)
 check_significant(lower,upper,observed)
 euclidean_distance(a, b)
 mean_center(points)
 average_nearest_neighbor_distance(points)
 minimum_bounding_rectangle(points)
 mbr_area(mbr)
 expected_distance(area, n)
 check_significant(lower,upper,observed)
 ...among other things

 """

import math


def compute_critical(p):
    lower = min(p)
    upper = max(p)

    return lower, upper

def check_significant(lower, upper, observed):

    return observed < lower or observed > upper

def euclidean_distance(a, b):

    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    return distance

def find_largest_city(gj):

     max_population = 0
     for feat in gj['features']:
         test_max_pop = feat['properties']['pop_max']
         if test_max_pop > max_population:
             max_population = test_max_pop
             city = feat['properties']['name']

     return city, max_population

def mean_center(points):
    sumx= 0.0
    sumy= 0.0
    for coord in points:
        sumx+=coord[0]
        sumy+=coord[1]
    x= sumx/len(points)
    y=sumy/len(points)

    return x, y

def average_nearest_neighbor_distance(points):
    min_dist_sum = 0
    for coord_x in points:
        first = True
        for  coord_y in points:
            if coord_x == coord_y:
              continue
            else:
                 d = euclidean_distance(coord_x, coord_y)
                 if first:
                    min_dist = d
                    first = False
                 else:
                    if d < min_dist:
                        min_dist = d
        min_dist_sum += min_dist

    mean_d = min_dist_sum / len(points)

    return mean_d

def minimum_bounding_retangle(points):
     xmin = 0
     xmax = 0
     ymin = 0
     ymax = 0
     for coord in points:
         if coord[0] < xmin:
             xmin = coord[0]
         elif coord[0] > xmax:
             xmax = coord[0]

         if coord[1] < ymin:
             ymin = coord[1]
         elif coord[1] > ymax:
             ymax = coord[1]

     xcorner = xmax - xmin
     ycorner = ymax - ymin
     mbr = [0,0,xcorner,ycorner]

     return mbr

def mbr_area(mbr):
    length = mbr[3] - mbr[1]
    width = mbr[2] - mbr[0]
    area = length * width

    return area

def expected_distance(area, n):
    expected = .5 * math.sqrt(area/n)

    return expected


