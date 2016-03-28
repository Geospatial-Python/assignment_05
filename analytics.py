import json
import math

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
    list_cities = []
    list_pop = []

    for d in kj['features']:
        pop_max = d['properties']['pop_max']
        citys = d['properties']['ls_name']
        list_cities.append(citys)
        list_pop.append(pop_max)

    max_population = max(list_pop)
    index_pop = list_pop.index(max_population)

    city = list_cities[index_pop]

    return city, max_population

def write_your_own(gj, city):
    """
    Here you will write your own code to find
    some attribute in the supplied geojson file.
    Take a look at the attributes available and pick
    something interesting that you might like to find
    or summarize.  This is totally up to you.
    Do not forget to write the accompanying test in
    tests.py!
    """
    list_cities2 = []
    home_state = []

    for s in gj['features']:
        citys2 = s['properties']['ls_name']
        statenm = s['properties']['adm1name']
        list_cities2.append(citys2)
        home_state.append(statenm)

    citynumber = list_cities2.index(city)
    stateans = home_state[citynumber]

    return stateans

def getx(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.
    Parameters
    ----------
    point : tuple
            in the form (x,y)
    Returns
    -------
     : int or float
       x coordinate
    """
    return point[0]


def gety(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.
    Parameters
    ----------
    point : tuple
            in the form (x,y)
    Returns
    -------
     : int or float
       y coordinate
    """
    return point[1]

