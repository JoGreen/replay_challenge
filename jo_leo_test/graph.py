import  networkx as nx
from jo_leo_test.triangle import Triangle

def create(points):
    #type: ([tuple])-> nx.Graph

    pass


def reachable_point():
    pass


def distance(p1, p2):
    #type:()->float
    x1, y1 = p1
    x2, y2 = p2

    return ((x2-x1)**2+(y2-y1)**2 )**0.5

