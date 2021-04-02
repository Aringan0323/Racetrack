#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2import numpy as np

class EdgeDetection:

    def __init__(self):
        self.imgSub = rospy.Subscriber('/triangle_mask', Image, triangleCB)

    def triangleCB(self, msg):
    