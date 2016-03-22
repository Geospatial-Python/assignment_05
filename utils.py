import math
import random
import sys
sys.path.append('C://Users/jmaynard/Documents/GitHub/assignment_05')

import analytics



def create_random(entries):
    rng = random.Random()
    result = []
    for i in range(entries):
        x=rng.random()
        y=rng.random()
        point=(x,y)
        result.append(point)
    return result

def permutations(number_of_permutations, number_of_points):


    result = []
    for i in range(number_of_permutations):
        points = create_random(number_of_points)
        observed_avg = analytics.average_nearest_neighbor_distance(points)
        result.append(observed_avg)

    return result

def compute_critical(permutations):
    lower = min(permutations)
    upper = max(permutations)

    result = lower,upper
    return result

def check_significant(lower, upper, observed):

    if observed<lower or observed>upper:
        return True
    else:
        return False
