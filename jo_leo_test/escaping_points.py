

def find_points(v1, v2, v3):
    #type:(tuple, tuple, tuple)->list
    v1_points = []
    x, y = v1
    coordinates_x = [x-1, x, x+1]
    coordinates_y = [y-1, y, y+1]
    points = []
    for x in coordinates_x:
        for y in coordinates_y:
            points.append((x,y) )


    return points
