import math


def find_largest_city(gj):
    list_cities = []
    list_pop = []

    for d in gj['features']:
        pop_max = d['properties']['pop_max']
        citys = d['properties']['ls_name']
        list_cities.append(citys)
        list_pop.append(pop_max)

    max_population = max(list_pop)
    index_pop = list_pop.index(max_population)
    city = list_cities[index_pop]

    return city, max_population


def write_your_own(gj, city):

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


def mean_center(points):
    x = 0
    y = 0
    for coor in points:
        x += coor[0]/len(points)
        y += coor[1]/len(points)
    return x, y


def average_nearest_neighbor_distance(points):
    shortest_path = []
    for num1, p_one in enumerate(points):
        distance = []
        for num2, p_two in enumerate(points):
            if num1 != num2:
                distance.append(math.sqrt((p_one[0] - p_two[0])**2 + (p_one[1] - p_two[1])**2))
        shortest_path.append(min(distance))
    mean_d = sum(shortest_path)/len(shortest_path)
    return mean_d


def minimum_bounding_rectangle(points):
    mbr = []
    x_list = []
    y_list = []
    for point in points:
        x_list.append(point[0])
        y_list.append(point[1])
    mbr.append(min(x_list))
    mbr.append(min(y_list))
    mbr.append(max(x_list))
    mbr.append(max(y_list))
    return mbr


def mbr_area(mbr):
    length = abs(mbr[0] - mbr[2])
    width = abs(mbr[1] - mbr[3])
    area = length * width
    return area

