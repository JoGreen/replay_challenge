import itertools

class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.v0 = (x0,y0)
        self.v1 = (x1,y1)
        self.v2 = (x2,y2)

    def get_vertices(self):
        return self.v0, self.v1, self.v2

    def bounding_box(self):
        max_coord = []
        min_coord = []
        for coords in zip(*[self.v0, self.v1, self.v2]):
            max_coord.append(max(coords))
            min_coord.append(min(coords))
        return list(zip(min_coord, max_coord))

    def contains(self, t):
        # type:(tuple)->bool
        points = [ self.v0, self.v1, self.v2 ]
        n = len(points)
        inside = False
        x,y = t
        p1x, p1y = points[0]
        for i in range(1, n + 1):
            p2x, p2y = points[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def find_escaping_points(self):
        # type:(tuple, tuple, tuple)->set
        points = []
        for v in [self.v0, self.v1, self.v2]:
            x, y = v
            coordinates_x = [x - 1, x, x + 1]
            coordinates_y = [y - 1, y, y + 1]

            for escape_p in zip(coordinates_x, coordinates_y):
                if escape_p != (x,y):
                    if not self.contains(escape_p):
                        points.append(escape_p)
        return points