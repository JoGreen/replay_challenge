from jo_leo_test.triangle import Triangle
from jo_leo_test.input_parser  import parse_file
from jo_leo_test import graph
from multiprocessing import Pool, cpu_count
import networkx as nx
import time, tqdm
import itertools
from networkx.algorithms import has_path

src, trg, triangles = parse_file('input_1.txt')
t0 = time.time()
points = []

for t in triangles:
    corners = t.surrounding_corners()
    # todo:
    # check t.contains(point) for all point in corners and all triangle t in triangles
    # and append only the corners as said above
    points.append(corners)

points = list(itertools.chain.from_iterable(points))

points.append(src)
points.append(trg)
print(len(points))

print(time.time()-t0)
t0 = time.time()

s = set(points)

print(len(s))

print(time.time()-t0)
t0 = time.time()

G = graph.create(points)

#if has_path(G, src, trg):
#    pass


