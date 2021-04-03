#!/usr/bin/env python

class lineDetection:

    def __init__(self):
        self.img_sub = rospy.Subscriber('/canny_mask', Image, self.img_callback)
        self.img_pub = rospy.Publisher('/', Image, queue_size=1)
