#!/usr/bin/env python
import rospy
from pcl_msgs.msg import PolygonMesh
from detection_grid import PointDistance
from sensor_msgs import point_cloud2
from motor import runrunmotor

def callback(data):
    g = point_cloud2.read_points(data.cloud)
    points = []
    for p in g:
        points.append(p)
    dis, angles = PointDistance(points)
    strength = [0, 0, 0, 0, 0, 0]
    for i, D in enumerate(dis):
        for d in D:
            s = max(0, min(1 - (d - 0.5) / 10.5, 1))
            strength[i] = max(strength[i], s)
    rospy.loginfo(strength)
    runrunmotor(strength)

def listener():
    rospy.init_node('mesh_listener', anonymous=True)
    rospy.Subscriber("kimera_vio_ros/mesh", PolygonMesh, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()
