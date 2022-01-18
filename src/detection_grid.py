#!usr/bin/env python
from os import remove
import numpy as np
import math

def grid(A):
    
    def project(v):
        return np.array([v[0], v[1]])

    def unit_vector(vector):
            return vector / np.linalg.norm(vector)

    def dot(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]

    # def angle_between(v1, v2):
    #     v1_u = unit_vector(v1)
    #     v2_u = unit_vector(v2)
    #     return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    angles = []
    grid = [[], [], [], [], [], []]

    bound_x = np.array([0.5, (3 ** 0.5) / 2])
    bound_y = np.array([-(3 ** 0.5) / 2, 0.5])
    for i in range(len(A)):
        # t = angle_between(bound,A[i])*180/np.pi
        # if bound[0] * A[i][1] - bound[1] * A[i][0] < 0:
        #     t *= -1
        x = dot(A[i], bound_x)
        y = dot(A[i], bound_y)
        t = math.atan2(y, x) * 180.0 / np.pi
        # print(x, y, t)

        angles.append(t)
    for i, t in enumerate(angles):
        if 60 > t >= 0:
            idx = int(t / 10)
            grid[idx].append(A[i])
    #print(angles)
    #for t, _ in angles:
        #if t > 0:
            #print(t)
    return grid, angles

def PointDistance(A):
    sections, angles = grid([np.array([p[0], p[1]]) for p in A])
    dis = [[], [], [], [], [], []]
    for i, sec in enumerate(sections):
        for p in sec:
            dis[i].append((p[0] ** 2 + p[1] ** 2) ** 0.5)
    return dis, angles
    
    for i in range(len(sections)):
        for j in range(len(sections[i])):
            sections[i][j] = (sections[i][j][0]**2 + sections[i][j][1]**2 + sections[i][j][2]**2)**(1/2)
    return sections
#print(PointDistance([(1,1,2),(1,2,3),(4,5,7),(5,6,8),(8,9,4)]))

    
