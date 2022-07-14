#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

def scan_callback(msg):
    #len(msg.ranges) is 720
    range_ahead = msg.ranges[30*2]
    range_left = msg.ranges[270*2]
    range_right = msg.ranges[90*2]
    range_back = msg.ranges[210*2]
    if range_right>0:
        pub1.publish(range_right)
    if range_ahead>0:
        pub2.publish(range_ahead)
    if range_left>0:
        pub3.publish(range_left)
    if range_back>0:
        pub4.publish(range_back)


pub1 = rospy.Publisher('range_right', Float32, queue_size=10)
pub2 = rospy.Publisher('range_ahead', Float32, queue_size=10)
pub3 = rospy.Publisher('range_left', Float32, queue_size=10)
pub4 = rospy.Publisher('range_back', Float32, queue_size=10)
rospy.init_node('range_ahead')

scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)

rospy.spin()