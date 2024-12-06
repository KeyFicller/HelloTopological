from manim import *
import numpy as np
import glm
import math

box_global_coordinate = [
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [1.0, 0.0, 1.0],
    [1.0, 1.0, 1.0],
    [0.0, 1.0, 1.0]
    ]

def look_at(eye, center, up):
    return glm.lookAtLH(eye, center, up)

def polygon_transform(indices, matrix):
    points = []
    for index in indices:
        points.append(matrix * box_global_coordinate[index])
    polygon = Polygon(*points)
    polygon.set_fill(GREEN, 0.8)
    return polygon

class hello_topological(Scene):
    def construct(self):
        eye = [-1e6, -1e6, 1e6]
        center = [0, 0, 0]
        up = [1, 1, math.sqrt(3)]

        view_matrix = look_at(eye, center, up)
        self.add(polygon_transform([0, 1, 2, 3], view_matrix))
        self.add(polygon_transform([0, 1, 5, 4], view_matrix))
        self.add(polygon_transform([1, 2, 6, 5], view_matrix))
        self.add(polygon_transform([2, 3, 7, 6], view_matrix))
        self.add(polygon_transform([3, 0, 4, 7], view_matrix))
        self.add(polygon_transform([4, 5, 6, 7], view_matrix))