#!/usr/bin/env python
import rospy

from pcl_msgs.msg import PolygonMesh
from sensor_msgs import point_cloud2

from util.detection_grid import point_distance
from util.motor import update_motor

import os
from threading import Thread


def callback(data):
    points_iter = point_cloud2.read_points(data.cloud)
    points = []
    for p in points_iter:
        points.append(p)
    dis = point_distance(points)
    strength = [0, 0, 0, 0, 0, 0]
    for i, D in enumerate(dis):
        for d in D:
            s = max(0, min(1 - (d - 0.5) / 3, 1))
            strength[i] = max(strength[i], s)
    strength = strength[::-1]

    print(strength)
    update_motor(strength)

def listener():
    rospy.init_node('mesh_listener', anonymous=True)
    rospy.Subscriber("kimera_vio_ros/mesh", PolygonMesh, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
