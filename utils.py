import math
import random


def getx(point):
    return point[0]


def gety(point):
    return point[1]


def expected_distance(area, n):
    expected = 0.5 * (math.sqrt(area / n))
    return expected


def manhattan_distance(a, b):
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance


def euclidean_distance(a, b):
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance


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
