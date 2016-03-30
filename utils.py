import math
import random

import analytics

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


def generate_random_points(n):
    n_points = [(random.uniform(0, 1), random.uniform(0, 1)) for x in range(n)]
    return n_points


def permutations(p=99, n=100):
    solution = []
    for tations in range(p):
        solution.append(analytics.average_nearest_neighbor_distance(generate_random_points(n)))
    return solution


def crit_tations(perms):
    max_tation = max(perms)
    min_tation = min(perms)
    return max_tation, min_tation


def check_yer_sig(max_tation2, min_tation2, obser_tation):
    return min_tation2 <= obser_tation or obser_tation <= max_tation2


