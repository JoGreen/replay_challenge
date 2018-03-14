from jo_leo_test.triangle import Triangle
from jo_leo_test.input_parser  import parse_file
from jo_leo_test import graph
from multiprocessing import Pool, cpu_count
import networkx as nx
import time, tqdm
import itertools
from networkx.algorithms import has_path

def is_point_useful(tr, point):
    #type:(Triangle, list)-> bool
    x, y  = point
    ## check first the bounding box of the triangle
    b_box = tr.bounding_box()
    Xmin, Xmax = b_box[0]
    Ymin, Ymax = b_box[1]
    if x < Xmin or x > Xmax or y < Ymin or y > Ymax :
     #Definitely not within the polygon!
        return True
    ##else check accurately inside the polygon
    return not tr.contains(point)


def remove_point_inside_triangle():
    pass


src, trg, triangles = parse_file('input_1.txt')
t0 = time.time()
points = []

for t in triangles:
    esc_points = t.find_escaping_points()
    #apply is_point_useful to all esc_points and all traingles
    #add only those for which is_point_useful is True
    is_point_useful(t, esc_points[0])
    points.append(esc_points)

points = list(itertools.chain.from_iterable(points))


points.append(src)
points.append(trg)
print(len(points))

print(time.time() -t0)
t0 = time.time()


G = graph.create(points)

#if has_path(G, src, trg):
#    pass


