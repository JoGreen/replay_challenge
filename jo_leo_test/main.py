from jo_leo_test.triangle import triangle
from jo_leo_test import escaping_points
from jo_leo_test.input_parser  import parse_file

def useful_points(p):
    if triangle.contains(*p):
        points.remove(p)


src, trg, triangles = parse_file('data.txt')
triangles = []
points = set()
for triangle in triangles:
    points = set.union(escaping_points(*triangle.get_vertices() ) )

for triangle in triangles:
    map(useful_points, points)







