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
        for coords in zip(*list(self.get_vertices())):
            max_coord.append(max(coords))
            min_coord.append(min(coords))
        return list(zip(min_coord, max_coord))

    def contains(self, point): ### todo and debug
        # type:(tuple)->bool
        vertices = list(self.get_vertices())
        if point in vertices:
            return True
        n = len(vertices)
        inside = False
        x,y = point
        ## check first the bounding box of the triangle
        b_box = self.bounding_box()
        Xmin, Xmax = b_box[0]
        Ymin, Ymax = b_box[1]
        if x < Xmin or x > Xmax or y < Ymin or y > Ymax:
            # Definitely not within the polygon!
            return False
        p1x, p1y = vertices[0]
        for i in range(1, n + 1):
            p2x, p2y = vertices[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def surrounding_corners(self):
        # type:(tuple, tuple, tuple)->set
        surr_corners = []
        for v in list(self.get_vertices()):
            x, y = v
            coordinates_x = [x - 1, x, x + 1]
            coordinates_y = [y - 1, y, y + 1]

            for corner in itertools.product(coordinates_x, coordinates_y):
                if not self.contains(corner):
                    surr_corners.append(corner)
        return surr_corners