from utils import *

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


def mean_center(points):

    x = 0
    y = 0

    for i in points:
        x += i[0]
        y += i[1]

    x /= len(points)
    y /= len(points)

    return x, y


def minimum_bounding_rectangle(points):

    mbr = [0, 0, 0, 0]
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    for p in points:
        if p[0] < x_min:
            x_min = p[0]
        if p[0] > x_max:
            x_max = p[0]
        if p[1] < y_min:
            y_min = p[1]
        if p[1] > y_max:
            y_max = p[1]
        mbr = [x_min, y_min, x_max, y_max]

    return mbr


def mbr_area(mbr):

    l = mbr[2] - mbr[0]
    w = mbr[3] - mbr[1]
    area = l * w

    return area


def expected_distance(area, n):

    expected = 0.5 * (math.sqrt(area / n))

    return expected


def compute_critical(points):

    l = min(points)
    u = max(points)

    return l, u


def check_significant(l, u, observed):

    if (l < observed) or (observed < u):
        result = True
    else:
        result = False

    return result

