#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

def scan_callback(msg):
    #len(msg.ranges) is 720
    range_left = msg.ranges[270*2]
    range_right = msg.ranges[90*2]

    range_back1 = msg.ranges[(210*2)]
    range_back2 = msg.ranges[(150*2)]
    range_back3 = msg.ranges[(205*2)]
    range_back4 = msg.ranges[(155*2)]
    range_back5 = msg.ranges[(230*2)]
    range_back6 = msg.ranges[(140*2)]

    range_ahead1 = msg.ranges[(30*2)]
    range_ahead2 = msg.ranges[(330*2)]
    range_ahead3 = msg.ranges[(25*2)]
    range_ahead4 = msg.ranges[(335*2)]
    range_ahead5 = msg.ranges[(40*2)]
    range_ahead6 = msg.ranges[(320*2)]
    range_ahead7 = msg.ranges[(35*2)]
    range_ahead8 = msg.ranges[(325*2)]
    
    cos25 = math.cos(math.radians(25))
    cos30 = math.cos(math.radians(30))
    cos35 = math.cos(math.radians(35))
    cos40 = math.cos(math.radians(40))

    range_back1=range_back1*cos30
    range_back2=range_back2*cos30
    range_back3=range_back3*cos25
    range_back4=range_back4*cos25
    range_back5=range_back5*cos40
    range_back6=range_back6*cos40
    
    
    range_ahead1=range_ahead1*cos30
    range_ahead2=range_ahead2*cos30
    range_ahead3=range_ahead3*cos25
    range_ahead4=range_ahead4*cos25
    range_ahead5=range_ahead5*cos40
    range_ahead6=range_ahead6*cos40
    range_ahead7=range_ahead5*cos35
    range_ahead8=range_ahead6*cos35
    
    count=0
    count_back=0
    if range_ahead1 != 0:
	count=count+1 
    if range_ahead2 != 0:
	count=count+1 
    if range_ahead3 != 0:
	count=count+1 
    if range_ahead4 != 0:
	count=count+1 
    if range_ahead5 != 0:
	count=count+1 
    if range_ahead6 != 0:
	count=count+1
    if range_ahead7 != 0:
	count=count+1
    if range_ahead8 != 0:
	count=count+1

    if range_back1 != 0:
	count_back=count_back+1 
    if range_back2 != 0:
	count_back=count_back+1
    if range_back3 != 0:
	count_back=count_back+1
    if range_back4 != 0:
	count_back=count_back+1
    if range_back5 != 0:
	count_back=count_back+1
    if range_back6 != 0:
	count_back=count_back+1     

    range_back=(range_back1+range_back2+range_back3+range_back4+range_back5+range_back6)/count_back
    range_ahead=(range_ahead1+range_ahead2+range_ahead3+range_ahead4+range_ahead5+range_ahead6+range_ahead7+range_ahead8)/count
			
    
    print(range_ahead)
    print(range_back)

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
