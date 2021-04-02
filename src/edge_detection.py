#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import cv2import numpy as np

class EdgeDetection:

    def __init__(self):
        self.img_sub = rospy.Subscriber('/camera/rgb/imgage_raw', Image, self.img_callback)

    def img_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        plt.imshow(img)

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        plt.imshow(gray, cmap='gray')

        kernel_size = 9
        grayBlur = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

        lowEnd = 30
        highEnd = 100
        edges = cv2.Canny(grayBlur, lowEnd, highEnd)


        
    
