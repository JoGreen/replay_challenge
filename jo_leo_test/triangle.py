class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.v0 = (x0,y0)
        self.v1 = (x1,y1)
        self.v2 = (x2,y2)

    def get_vertices(self):
        return self.v0, self.v1, self.v2

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

    def find_escaping_points(self, v1, v2, v3):
        # type:(tuple, tuple, tuple)->set
        points = []
        for v in [v1, v2, v3]:
            x, y = v
            coordinates_x = [x - 1, x, x + 1]
            coordinates_y = [y - 1, y, y + 1]

            for px in coordinates_x:
                for py in coordinates_y:
                    p = px, py
                    if p != v:
                        if not self.contains(p):
                            points.append(p)

        points = set(points)
        return points