#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class pid:   
    def __init__(self):
        self.centroid_sub = rospy.Subscriber('/theta', Int32, self.centroid_cb)
        self.offset_sub = rospy.Subscriber('/offset', Int32, self.offset_cb)
        self.move = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.offset = 0
        self.twist = Twist()
        self.bridge = CvBridge()

    def centroid_cb(self, msg):
        theta = msg.data
        angle_err = theta - 180
        print(angle_err)
        self.twist.linear.x = 2
        self.twist.angular.z = -(float(angle_err)/(180))* 1.5
        self.move.publish(self.twist)

    def offset_cb(self, msg):
        return
        


