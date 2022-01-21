#!usr/bin/env python
from os import remove
import numpy as np
import math


def project(v):
    return np.array([v[0], v[1]])

def unit_vector(vector):
        return vector / np.linalg.norm(vector)

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def slice(points):
    
    angles = []

    bound_x = np.array([0.5, (3 ** 0.5) / 2])
    bound_y = np.array([-(3 ** 0.5) / 2, 0.5])
    for i in range(len(points)):
        x = dot(points[i], bound_x)
        y = dot(points[i], bound_y)
        t = math.atan2(y, x) * 180.0 / np.pi
        angles.append(t)

    sections = [[], [], [], [], [], []]
    for i, t in enumerate(angles):
        if 60 > t >= 0:
            idx = int(t / 10)
            sections[idx].append(points[i])

    return sections

def point_distance(points):
    projection = []
    for p in points:
        if p[2] < 0:
            continue
        projection.append(np.array([p[0], p[1]]))
    sections = slice(projection)

    dis = [[], [], [], [], [], []]
    for i, sec in enumerate(sections):
        for p in sec:
            dis[i].append((p[0] ** 2 + p[1] ** 2) ** 0.5)
    return dis
    

    
