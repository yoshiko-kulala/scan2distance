#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

def scan_callback(msg):
    range_back=-1
    range_ahead=-1

    range_front_list=[]

    range_front_list.insert(0,msg.ranges[695]*math.cos(math.radians(12.5)))
    range_front_list.insert(1,msg.ranges[696]*math.cos(math.radians(12.0)))
    range_front_list.insert(2,msg.ranges[697]*math.cos(math.radians(12.0)))
    range_front_list.insert(3,msg.ranges[698]*math.cos(math.radians(11.5)))
    range_front_list.insert(4,msg.ranges[699]*math.cos(math.radians(11.0)))
    range_front_list.insert(5,msg.ranges[700]*math.cos(math.radians(10.5)))
    range_front_list.insert(6,msg.ranges[701]*math.cos(math.radians(10.0)))
    range_front_list.insert(7,msg.ranges[702]*math.cos(math.radians(9.5)))
    range_front_list.insert(8,msg.ranges[703]*math.cos(math.radians(9.0)))
    range_front_list.insert(9,msg.ranges[704]*math.cos(math.radians(8.5)))
    range_front_list.insert(10,msg.ranges[705]*math.cos(math.radians(8.0)))
    range_front_list.insert(11,msg.ranges[706]*math.cos(math.radians(7.0)))
    range_front_list.insert(12,msg.ranges[707]*math.cos(math.radians(6.5)))
    range_front_list.insert(13,msg.ranges[708]*math.cos(math.radians(6.0)))
    range_front_list.insert(14,msg.ranges[709]*math.cos(math.radians(5.5)))
    range_front_list.insert(15,msg.ranges[710]*math.cos(math.radians(5.0)))
    range_front_list.insert(16,msg.ranges[711]*math.cos(math.radians(4.5)))
    range_front_list.insert(17,msg.ranges[712]*math.cos(math.radians(4.0)))
    range_front_list.insert(18,msg.ranges[713]*math.cos(math.radians(3.5)))
    range_front_list.insert(19,msg.ranges[714]*math.cos(math.radians(3.0)))
    range_front_list.insert(20,msg.ranges[715]*math.cos(math.radians(2.5)))
    range_front_list.insert(21,msg.ranges[716]*math.cos(math.radians(2.0)))
    range_front_list.insert(22,msg.ranges[717]*math.cos(math.radians(1.5)))
    range_front_list.insert(23,msg.ranges[718]*math.cos(math.radians(1.0)))
    range_front_list.insert(24,msg.ranges[719]*math.cos(math.radians(0.5)))
    range_front_list.insert(25,msg.ranges[0])
    range_front_list.insert(26,msg.ranges[1]*math.cos(math.radians(0.5)))
    range_front_list.insert(27,msg.ranges[2]*math.cos(math.radians(1.0)))
    range_front_list.insert(28,msg.ranges[3]*math.cos(math.radians(1.5)))
    range_front_list.insert(29,msg.ranges[4]*math.cos(math.radians(2.0)))
    range_front_list.insert(30,msg.ranges[5]*math.cos(math.radians(2.5)))
    range_front_list.insert(31,msg.ranges[6]*math.cos(math.radians(3.0)))
    range_front_list.insert(32,msg.ranges[7]*math.cos(math.radians(3.5)))
    range_front_list.insert(33,msg.ranges[8]*math.cos(math.radians(4.0)))
    range_front_list.insert(34,msg.ranges[9]*math.cos(math.radians(4.5)))
    range_front_list.insert(35,msg.ranges[10]*math.cos(math.radians(5.0)))
    range_front_list.insert(36,msg.ranges[11]*math.cos(math.radians(5.5)))
    range_front_list.insert(37,msg.ranges[12]*math.cos(math.radians(6.0)))
    range_front_list.insert(38,msg.ranges[13]*math.cos(math.radians(6.5)))
    range_front_list.insert(39,msg.ranges[14]*math.cos(math.radians(7.0)))
    range_front_list.insert(40,msg.ranges[15]*math.cos(math.radians(7.5)))
    range_front_list.insert(41,msg.ranges[16]*math.cos(math.radians(8.0)))
    range_front_list.insert(42,msg.ranges[17]*math.cos(math.radians(8.5)))
    range_front_list.insert(43,msg.ranges[18]*math.cos(math.radians(9.0)))
    range_front_list.insert(44,msg.ranges[19]*math.cos(math.radians(9.5)))
    range_front_list.insert(45,msg.ranges[20]*math.cos(math.radians(10.0)))
    range_front_list.insert(46,msg.ranges[21]*math.cos(math.radians(10.5)))
    range_front_list.insert(47,msg.ranges[22]*math.cos(math.radians(11.0)))
    range_front_list.insert(48,msg.ranges[23]*math.cos(math.radians(11.5)))
    range_front_list.insert(49,msg.ranges[24]*math.cos(math.radians(12.0)))
    range_front_list.insert(50,msg.ranges[25]*math.cos(math.radians(12.5)))

    front_cou=0
    front_ave=0
    front_min=1300.0


    for item in range_front_list:
        if item<1200 or item>0:
            front_cou=front_cou+1
            front_ave=front_ave+item

    front_ave=front_ave/front_cou

    range_right_list=[]

    range_right_list.insert(0,msg.ranges[155]*math.cos(math.radians(12.5)))
    range_right_list.insert(1,msg.ranges[156]*math.cos(math.radians(12.0)))
    range_right_list.insert(2,msg.ranges[157]*math.cos(math.radians(12.0)))
    range_right_list.insert(3,msg.ranges[158]*math.cos(math.radians(11.5)))
    range_right_list.insert(4,msg.ranges[159]*math.cos(math.radians(11.0)))
    range_right_list.insert(5,msg.ranges[160]*math.cos(math.radians(10.5)))
    range_right_list.insert(6,msg.ranges[161]*math.cos(math.radians(10.0)))
    range_right_list.insert(7,msg.ranges[162]*math.cos(math.radians(9.5)))
    range_right_list.insert(8,msg.ranges[163]*math.cos(math.radians(9.0)))
    range_right_list.insert(9,msg.ranges[164]*math.cos(math.radians(8.5)))
    range_right_list.insert(10,msg.ranges[165]*math.cos(math.radians(8.0)))
    range_right_list.insert(11,msg.ranges[166]*math.cos(math.radians(7.0)))
    range_right_list.insert(12,msg.ranges[167]*math.cos(math.radians(6.5)))
    range_right_list.insert(13,msg.ranges[168]*math.cos(math.radians(6.0)))
    range_right_list.insert(14,msg.ranges[169]*math.cos(math.radians(5.5)))
    range_right_list.insert(15,msg.ranges[170]*math.cos(math.radians(5.0)))
    range_right_list.insert(16,msg.ranges[171]*math.cos(math.radians(4.5)))
    range_right_list.insert(17,msg.ranges[172]*math.cos(math.radians(4.0)))
    range_right_list.insert(18,msg.ranges[173]*math.cos(math.radians(3.5)))
    range_right_list.insert(19,msg.ranges[174]*math.cos(math.radians(3.0)))
    range_right_list.insert(20,msg.ranges[175]*math.cos(math.radians(2.5)))
    range_right_list.insert(21,msg.ranges[176]*math.cos(math.radians(2.0)))
    range_right_list.insert(22,msg.ranges[177]*math.cos(math.radians(1.5)))
    range_right_list.insert(23,msg.ranges[178]*math.cos(math.radians(1.0)))
    range_right_list.insert(24,msg.ranges[179]*math.cos(math.radians(0.5)))
    range_right_list.insert(25,msg.ranges[180])
    range_right_list.insert(26,msg.ranges[181]*math.cos(math.radians(0.5)))
    range_right_list.insert(27,msg.ranges[182]*math.cos(math.radians(1.0)))
    range_right_list.insert(28,msg.ranges[183]*math.cos(math.radians(1.5)))
    range_right_list.insert(29,msg.ranges[184]*math.cos(math.radians(2.0)))
    range_right_list.insert(30,msg.ranges[185]*math.cos(math.radians(2.5)))
    range_right_list.insert(31,msg.ranges[186]*math.cos(math.radians(3.0)))
    range_right_list.insert(32,msg.ranges[187]*math.cos(math.radians(3.5)))
    range_right_list.insert(33,msg.ranges[188]*math.cos(math.radians(4.0)))
    range_right_list.insert(34,msg.ranges[189]*math.cos(math.radians(4.5)))
    range_right_list.insert(35,msg.ranges[190]*math.cos(math.radians(5.0)))
    range_right_list.insert(36,msg.ranges[191]*math.cos(math.radians(5.5)))
    range_right_list.insert(37,msg.ranges[192]*math.cos(math.radians(6.0)))
    range_right_list.insert(38,msg.ranges[193]*math.cos(math.radians(6.5)))
    range_right_list.insert(39,msg.ranges[194]*math.cos(math.radians(7.0)))
    range_right_list.insert(40,msg.ranges[195]*math.cos(math.radians(7.5)))
    range_right_list.insert(41,msg.ranges[196]*math.cos(math.radians(8.0)))
    range_right_list.insert(42,msg.ranges[197]*math.cos(math.radians(8.5)))
    range_right_list.insert(43,msg.ranges[198]*math.cos(math.radians(9.0)))
    range_right_list.insert(44,msg.ranges[199]*math.cos(math.radians(9.5)))
    range_right_list.insert(45,msg.ranges[200]*math.cos(math.radians(10.0)))
    range_right_list.insert(46,msg.ranges[201]*math.cos(math.radians(10.5)))
    range_right_list.insert(47,msg.ranges[202]*math.cos(math.radians(11.0)))
    range_right_list.insert(48,msg.ranges[203]*math.cos(math.radians(11.5)))
    range_right_list.insert(49,msg.ranges[204]*math.cos(math.radians(12.0)))
    range_right_list.insert(50,msg.ranges[205]*math.cos(math.radians(12.5)))

    right_cou=0
    right_ave=0

    for item in range_right_list:
        if item<1200 or item>0:
            right_cou=right_cou+1
            right_ave=right_ave+item
    right_ave=right_ave/right_cou

    range_left_list=[]

    range_left_list.insert(0,msg.ranges[515]*math.cos(math.radians(12.5)))
    range_left_list.insert(1,msg.ranges[516]*math.cos(math.radians(12.0)))
    range_left_list.insert(2,msg.ranges[517]*math.cos(math.radians(12.0)))
    range_left_list.insert(3,msg.ranges[518]*math.cos(math.radians(11.5)))
    range_left_list.insert(4,msg.ranges[519]*math.cos(math.radians(11.0)))
    range_left_list.insert(5,msg.ranges[520]*math.cos(math.radians(10.5)))
    range_left_list.insert(6,msg.ranges[521]*math.cos(math.radians(10.0)))
    range_left_list.insert(7,msg.ranges[522]*math.cos(math.radians(9.5)))
    range_left_list.insert(8,msg.ranges[523]*math.cos(math.radians(9.0)))
    range_left_list.insert(9,msg.ranges[524]*math.cos(math.radians(8.5)))
    range_left_list.insert(10,msg.ranges[525]*math.cos(math.radians(8.0)))
    range_left_list.insert(11,msg.ranges[526]*math.cos(math.radians(7.0)))
    range_left_list.insert(12,msg.ranges[527]*math.cos(math.radians(6.5)))
    range_left_list.insert(13,msg.ranges[528]*math.cos(math.radians(6.0)))
    range_left_list.insert(14,msg.ranges[529]*math.cos(math.radians(5.5)))
    range_left_list.insert(15,msg.ranges[530]*math.cos(math.radians(5.0)))
    range_left_list.insert(16,msg.ranges[531]*math.cos(math.radians(4.5)))
    range_left_list.insert(17,msg.ranges[532]*math.cos(math.radians(4.0)))
    range_left_list.insert(18,msg.ranges[533]*math.cos(math.radians(3.5)))
    range_left_list.insert(19,msg.ranges[534]*math.cos(math.radians(3.0)))
    range_left_list.insert(20,msg.ranges[535]*math.cos(math.radians(2.5)))
    range_left_list.insert(21,msg.ranges[536]*math.cos(math.radians(2.0)))
    range_left_list.insert(22,msg.ranges[537]*math.cos(math.radians(1.5)))
    range_left_list.insert(23,msg.ranges[538]*math.cos(math.radians(1.0)))
    range_left_list.insert(24,msg.ranges[539]*math.cos(math.radians(0.5)))
    range_left_list.insert(25,msg.ranges[540])
    range_left_list.insert(26,msg.ranges[541]*math.cos(math.radians(0.5)))
    range_left_list.insert(27,msg.ranges[542]*math.cos(math.radians(1.0)))
    range_left_list.insert(28,msg.ranges[543]*math.cos(math.radians(1.5)))
    range_left_list.insert(29,msg.ranges[544]*math.cos(math.radians(2.0)))
    range_left_list.insert(30,msg.ranges[545]*math.cos(math.radians(2.5)))
    range_left_list.insert(31,msg.ranges[546]*math.cos(math.radians(3.0)))
    range_left_list.insert(32,msg.ranges[547]*math.cos(math.radians(3.5)))
    range_left_list.insert(33,msg.ranges[548]*math.cos(math.radians(4.0)))
    range_left_list.insert(34,msg.ranges[549]*math.cos(math.radians(4.5)))
    range_left_list.insert(35,msg.ranges[550]*math.cos(math.radians(5.0)))
    range_left_list.insert(36,msg.ranges[551]*math.cos(math.radians(5.5)))
    range_left_list.insert(37,msg.ranges[552]*math.cos(math.radians(6.0)))
    range_left_list.insert(38,msg.ranges[553]*math.cos(math.radians(6.5)))
    range_left_list.insert(39,msg.ranges[554]*math.cos(math.radians(7.0)))
    range_left_list.insert(40,msg.ranges[555]*math.cos(math.radians(7.5)))
    range_left_list.insert(41,msg.ranges[556]*math.cos(math.radians(8.0)))
    range_left_list.insert(42,msg.ranges[557]*math.cos(math.radians(8.5)))
    range_left_list.insert(43,msg.ranges[558]*math.cos(math.radians(9.0)))
    range_left_list.insert(44,msg.ranges[559]*math.cos(math.radians(9.5)))
    range_left_list.insert(45,msg.ranges[560]*math.cos(math.radians(10.0)))
    range_left_list.insert(46,msg.ranges[561]*math.cos(math.radians(10.5)))
    range_left_list.insert(47,msg.ranges[562]*math.cos(math.radians(11.0)))
    range_left_list.insert(48,msg.ranges[563]*math.cos(math.radians(11.5)))
    range_left_list.insert(49,msg.ranges[564]*math.cos(math.radians(12.0)))
    range_left_list.insert(50,msg.ranges[565]*math.cos(math.radians(12.5)))

    left_cou=0
    left_ave=0

    for item in range_left_list:
        if item<1200 or item>0:
            left_cou=left_cou+1
            left_ave=left_ave+item
    left_ave=left_ave/left_cou

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

    if count_back!=0:
        range_back=(range_back1+range_back2+range_back3+range_back4+range_back5+range_back6)/count_back
    if count!=0:
        range_ahead=(range_ahead1+range_ahead2+range_ahead3+range_ahead4+range_ahead5+range_ahead6+range_ahead7+range_ahead8)/count
			
    
    #if front_cou!=0:
    #    range_front = (range_front1 + range_front2 + range_front3 + range_front4 + range_front5 + range_front6 + range_front7)/front_cou


    print "front:",
    print(front_ave)
    print "left:",
    print(left_ave)
    print "right:",
    print(right_ave)
    print("")

    if right_ave>0:
        pub1.publish(right_ave)
    if range_ahead>0:
        pub2.publish(range_ahead)
    if left_ave>0:
        pub3.publish(left_ave)
    if range_back>0:
        pub4.publish(range_back)
    if front_ave>0:
        pub5.publish(front_ave)
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
