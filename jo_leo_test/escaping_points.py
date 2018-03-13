

def find_points(v1, v2, v3):
    #type:(tuple, tuple, tuple)->set
    points = []
    for v in [v1, v2, v3]:
        x, y = v
        coordinates_x = [x-1, x, x+1]
        coordinates_y = [y-1, y, y+1]

        for px in coordinates_x:
            for py in coordinates_y:
                if (px, py) != v:
                    points.append((px,py) )


    points = set(points)
    return points

