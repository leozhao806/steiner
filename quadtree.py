import numpy as np


class Node():
    def __init__(self, x0, y0, w, h, points):
        self.x0 = x0
        self.y0 = y0
        self.w = w
        self.h = h
        self.points = points
        self.child = []

    def getw(self):
        return self.w

    def geth(self):
        return self.h

    def getp(self):
        return self.points


def subdivide(node, k):
    if len(node.points) <= k:
        return

    w_, h_ = node.w / 2, node.h /2
    p = contains([node.x0, node.y0], w_, h_, node.points)
    x1 = Node(node.x0, node.y0, w_, h_, p)
    subdivide(x1, k)
    p = contains([node.x0, node.y0 + h_], w_, h_, node.points)
    x2 = Node(node.x0, node.y0 + h_, w_, h_, p)
    subdivide(x2, k)
    p = contains([node.x0 + w_, node.y0 + h_], w_, h_, node.points)
    x3 = Node(node.x0 + w_, node.y0 + h_, w_, h_, p)
    subdivide(x3, k)
    p = contains([node.x0 + w_, node.y0], w_, h_, node.points)
    x4 = Node(node.x0 + w_, node.y0, w_, h_, p)
    subdivide(x4, k)

    node.child = [x1, x2, x3, x4]


def contains(boundary, w, h, points):
    pts = []
    for i in range(points.shape[0]):
        if points[i][0] >= boundary[0] and points[i][0] <= boundary[0] + w:
            if points[i][1] >= boundary[1] and points[i][1] <= boundary[1] + h:
                pts.append([points[i][0], points[i][1]])
    return np.array(pts)


def find_child(node):
    if not node.child:
        return [node]

    else:
        child = []
        for c in node.child:
            child += (find_child(c))
        return child