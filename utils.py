"""
same date as other,
same guy as other.
y'know, german last name?

Stuff to do here

manhattan_distance
euclidean_distance
getx
gety
shift_point
check_coincident
check_in
create_random
permutations

...at least, I hope

"""
import math
import random
from .analytics import average_nearest_neighbor_distance

def manhattan_distance(a, b):
    distance =  abs(a[0] - b[0]) + abs(a[1] - b[1])

    return distance

def euclidian_distance(a, b):
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    return distance

def getx(point):

    return point[0]

def gety(point):

    return point[1]

def shift_point(point, x_shift, y_shift):

     x = getx(point)
     y = gety(point)

     x += x_shift
     y += y_shift

     return x, y

def check_coincident(a, b):

    return a == b

def check_in(point, point_list):

    return point in point_list

def create_random(n, seed=None):
    random.seed(seed)
    points = [(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]

    return points

def permutations(p=99, n=100):
     
     perm = []
     for x in range(p):
         points = create_random(n, None)
         avg_nnd = average_nearest_neighbor_distance(points)
         perm.append(avg_nnd)
 
     return perm
