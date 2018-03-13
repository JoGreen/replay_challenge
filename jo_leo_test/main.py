from jo_leo_test.triangle import triangle
from jo_leo_test import escaping_points
from jo_leo_test.input_parser  import parse_file

def remove_useless_points(p):
    if triangle.contains(*p):
        points.remove(p)
        print ('point removed')


src, trg, triangles = parse_file('data.txt')

points = set()
for triangle in triangles:
    points = set.union(escaping_points(*triangle.get_vertices() ) )

for triangle in triangles:
    map(remove_useless_points, points)







