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
        self.centroid_sub = rospy.Subscriber('/centroidXVal', Int32, self.centroid_cb)
        self.move = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.twist = Twist()
        self.bridge = CvBridge()

    def centroid_cb(self, msg):
        cx = msg.data
        # Calculating an error between the middle of the screen and the centroid
        angle_err = (cx)-960
        self.twist.linear.x = 0.4

        # Uses centroid error to control angular velocity
        self.twist.angular.z = -(float(angle_err)/(960))* 1.5
        self.move.publish(self.twist)

        


