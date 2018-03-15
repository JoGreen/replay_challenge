from jo_leo_test.triangle import Triangle
from jo_leo_test.input_parser  import parse_file
from jo_leo_test import graph
from multiprocessing import Pool, cpu_count
import networkx as nx
import time, tqdm
import itertools
from networkx.algorithms import has_path


def filter_points_in_triangle(point_list):
    return lambda tr: itertools.filterfalse(lambda x: tr.contains(x), point_list)


src, dest, triangles = parse_file('input_1.txt')
t0 = time.time()
points = []

for t in triangles:
    corners = t.surrounding_corners()
    points.append(corners)

points = list(itertools.chain.from_iterable(points))
print(len(points))

print(time.time()-t0)
t0 = time.time()

s = set(points)

s.add(src)
s.add(dest)

print(time.time()-t0)
t0 = time.time()

filter_all = map(filter_points_in_triangle(points), triangles)

print(time.time()-t0)
t0 = time.time()

#points = list(itertools.chain.from_iterable(filter_all))

#print(len(points))

print(time.time()-t0)
t0 = time.time()



G = graph.create(points)

#if has_path(G, src, dest):
#    pass


