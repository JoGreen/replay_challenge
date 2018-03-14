from  jo_leo_test.triangle import Triangle


def parse_file(path):
    #type:(str)-> Union(tuple, tuple, [Triangle])
    file = open(path, 'r')
    i = 0
    triangles = []
    for line in file:
        line = line.strip()
        if i == 0:
            split = line.split(" ")
            source = int(split[0]), int(split[1])
            target = int(split[2]), int(split[3])
        elif i == 1:
            pass
        else:
            split = line.split(" ")
            triangles.append(Triangle(int(split[0]), int(split[1]), int(split[2]), int(split[3]), int(split[4]), int(split[5])))
        i += 1
    return source, target, triangles



