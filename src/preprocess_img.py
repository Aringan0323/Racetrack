#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2 as cv
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

class TriangleMask:
    
    def __init__(self):
        self.img_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.img_callback)
        self.img_pub = rospy.Publisher('/triangle_mask', Image, queue_size=1)
        self.bridge = CvBridge()
        
        # Width and height of the image. The dimensions are specific to the resolution of the 
        # robot's camera, so a robot with a camera of a different resolution will have to 
        # have these values tuned to the resolution of the camera.
        w = 1920
        h = 1080

        # Defining the verticies of the trapezoid
        y1 = int((5*h)/9)
        y2 = int((7*h)/9)
        x1 = int((6*w)/16)
        x2 = int((10*w)/16)

        # Defining the areas of the image around the trapezoid which will be masked out
        self.area1 = np.array([[0,0], [w,0],[w,y2],[x2,y1],[x1,y1],[0,y2]], np.int32)
        self.area2 = np.array([[0,h],[0,y2],[w,y2],[w,h]], np.int32)

    def img_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        # Filling the areas around the trapezoid in the image
        triangle_img = cv.fillPoly(img,pts=[self.area1,self.area2], color=(0, 0, 255))


        triangle_img_hsv = cv.cvtColor(triangle_img, cv.COLOR_BGR2HSV)
        lower_white = np.array([0,0,0], dtype=np.uint8)
        upper_white = np.array([0,0,255], dtype=np.uint8)
        white_triangle_mask = cv.inRange(triangle_img_hsv,  lower_white, upper_white)

        bgr_mask = np.zeros_like(img)
        bgr_mask[:,:,0] = white_triangle_mask
        bgr_mask[:,:,1] = white_triangle_mask
        bgr_mask[:,:,2] = white_triangle_mask

        self.img_pub.publish(self.bridge.cv2_to_imgmsg(bgr_mask, 'bgr8'))

