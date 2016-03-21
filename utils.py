import math
import random

"""
	1. Organize the functions that were in point_pattern.py into the appropriate modules.
	2. Update the tests to reflect the new structure.
	3. Write a function to generate $n$ random points, where the user defines $n$.
	4. Write a function that takes $p$ an integer number of permutations. For each
	    permutation, create $n$ random points and compute the mean nearest neighbor distance.
	    Let this function default to p=99 and n=100. Make sure that the user can alter these
	    values if they like.
	5. Write a function to compute the critical points in the results returned by the
	    function you wrote in 4. If p = 99, then the function in 4 should return a list of 99
	    distances. This function will take that list and find the smallest and largest distances.
	    These are the critical points of the Monte Carlo test.
	6. Write a function that takes the critical points of the Monte Carlo simulation and the
	    observed value and returns True is the observed distance is significant, i.e., less than
	    or greater than the observed. Otherwise, return False.
	7. Write tests for items 3, 4, 5, and 6.
	8. Look at the file, functional_test.py. In that file I have written a single functional
	    test that ties together all of your previous work. For this test, you should replace the
	    module and function names with your own values. For example, I assume that all the
	    necessary methods are in the point_pattern module. Since you refactored the structure of
	    the code in completing #1, the point_pattern module does not exist. Instead, analytics
	    and utils do. Additionally,for #3 - 5, you wrote functions. I guessed at what you might
	    name these, but leave it to you to update the functional test with the names you selected.
"""


def manhattan_distance(a, b):

    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance


def euclidean_distance(a, b):

    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
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


def getx(point):

    return point[0]


def gety(point):

    return point[1]


def average_nearest_neighbor_distance(points):

    mean_d = 0
    nearest_neighbor = None

    for point in points:
        for otherPoint in points:
            if check_coincident(point, otherPoint):
                continue
            current_distance = euclidean_distance(point, otherPoint)
            if nearest_neighbor is None:
                nearest_neighbor = current_distance
            elif nearest_neighbor > current_distance:
                nearest_neighbor = current_distance

        mean_d += nearest_neighbor
        nearest_neighbor = None

    mean_d /= len(points)

    return mean_d


def create_random_points(n):

    random_points = [(random.uniform(0, 1), random.uniform(0, 1)) in range(n)]

    return random_points


def permutation(p=99, n=100):

    per = []
    for x in range(p):
        per.append(average_nearest_neighbor_distance(create_random_points(n)))

    return per

