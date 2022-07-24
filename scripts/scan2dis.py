#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
range_left = -1
range_right = -1
range_back=-1
range_ahead=-1
range_front = -1
# range_kago=-1

def scan_callback(msg):
    #len(msg.ranges) is 720
    if msg.ranges[270*2]>0:
        range_left = msg.ranges[270*2]
    if msg.ranges[90*2]>0:
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

    range_front1 = msg.ranges[(0)]
    range_front2 = msg.ranges[(1*2)]*math.cos(math.radians(1))
    range_front3 = msg.ranges[(2*2)]*math.cos(math.radians(2))
    range_front4 = msg.ranges[(3*2)]*math.cos(math.radians(3))
    range_front5 = msg.ranges[(359*2)]*math.cos(math.radians(1))
    range_front6 = msg.ranges[(358*2)]*math.cos(math.radians(2))
    range_front7 = msg.ranges[(357*2)]*math.cos(math.radians(3))
    
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

    if count_back!=0:
        range_back=(range_back1+range_back2+range_back3+range_back4+range_back5+range_back6)/count_back
    if count!=0:
        range_ahead=(range_ahead1+range_ahead2+range_ahead3+range_ahead4+range_ahead5+range_ahead6+range_ahead7+range_ahead8)/count
			
    front_cou=0
    if range_front1>0:
        front_cou=front_cou+1
    if range_front2>0:
        front_cou=front_cou+1
    if range_front3>0:
        front_cou=front_cou+1
    if range_front4>0:
        front_cou=front_cou+1
    if range_front5>0:
        front_cou=front_cou+1
    if range_front6>0:
        front_cou=front_cou+1
    if range_front7>0:
        front_cou=front_cou+1
    if front_cou!=0:
        range_front = (range_front1 + range_front2 + range_front3 + range_front4 + range_front5 + range_front6 + range_front7)/front_cou

    # list_kago = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # list_kago.insert(0, msg.ranges[(0)])
    # list_kago.insert(1, msg.ranges[(1*2)]*math.cos(math.radians(1)))
    # list_kago.insert(2, msg.ranges[(2*2)]*math.cos(math.radians(2)))
    # list_kago.insert(3, msg.ranges[(3*2)]*math.cos(math.radians(3)))
    # list_kago.insert(4, msg.ranges[(4*2)]*math.cos(math.radians(4)))
    # list_kago.insert(5, msg.ranges[(5*2)]*math.cos(math.radians(5)))
    # list_kago.insert(6, msg.ranges[(6*2)]*math.cos(math.radians(6)))
    # list_kago.insert(7, msg.ranges[(7*2)]*math.cos(math.radians(7)))
    # list_kago.insert(8, msg.ranges[(359*2)]*math.cos(math.radians(1)))
    # list_kago.insert(9, msg.ranges[(358*2)]*math.cos(math.radians(2)))
    # list_kago.insert(10, msg.ranges[(357*2)]*math.cos(math.radians(3)))
    # list_kago.insert(11, msg.ranges[(356*2)]*math.cos(math.radians(4)))
    # list_kago.insert(12, msg.ranges[(355*2)]*math.cos(math.radians(5)))
    # list_kago.insert(13, msg.ranges[(354*2)]*math.cos(math.radians(6)))
    # list_kago.insert(14, msg.ranges[(353*2)]*math.cos(math.radians(7)))

    # for item in list_kago:
    #     if item==0:
    #         item = 1000
    # if max(list_kago)<1000:
    #     range_kago=max(list_kago)

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
    if range_front>0:
        pub5.publish(range_front)
    # if range_kago>0:
    #     pub6.publish(range_kago)


pub1 = rospy.Publisher('range_right', Float32, queue_size=10)
pub2 = rospy.Publisher('range_ahead', Float32, queue_size=10)
pub3 = rospy.Publisher('range_left', Float32, queue_size=10)
pub4 = rospy.Publisher('range_back', Float32, queue_size=10)
pub5 = rospy.Publisher('range_front', Float32, queue_size=10)
# pub6 = rospy.Publisher('range_kago', Float32, queue_size=10)
rospy.init_node('range_ahead')

scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)

rospy.spin()
