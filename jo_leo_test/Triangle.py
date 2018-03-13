class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.v0 = (x0,y0)
        self.v1 = (x1,y1)
        self.v2 = (x2,y2)

    def contains(self, x, y):
        points = [ self.v0, self.v1, self.v2 ]
        n = len(points)
        inside = False
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
