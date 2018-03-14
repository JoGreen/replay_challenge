from jo_leo_test.triangle import Triangle
from jo_leo_test.input_parser  import parse_file
from jo_leo_test import graph
from multiprocessing import Pool, cpu_count
import networkx as nx
import time, tqdm
import itertools
from networkx.algorithms import has_path

def remove_useless_points(tr, point):
    #type:(Triangle, list)->tuple or None
    if tr.contains(point):
        print ('point added to black list')
        return point


def remove_point_inside_triangle():
    pass


src, trg, triangles = parse_file('input_1.txt')
t0 = time.time()
points = set()
for t in triangles:
    points = points.union(t.find_escaping_points(*t.get_vertices() ) )


pool = Pool(cpu_count() -1)
for t in triangles:
    #map(remove_useless_points, points)
    #useless_points = pool.map(remove_useless_points, [t]*len(points), points) # use starmap
    useless_points = map(remove_useless_points, [t]*len(points), points)

pool.close()

useless_points = set(list(useless_points)  )
useless_points.remove(None)
points = points.union([src, trg])
useful_points = (p for p in points if p not in useless_points)

print(time.time() -t0)


print(len(list(useful_points)))


G = graph.create(useful_points, triangles)

#if has_path(G, src, trg):
#    pass


