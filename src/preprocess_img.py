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

    def img_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        w = img.shape[1]
        h = img.shape[0]
        verts = np.array([[0,0],[w,0],[w,h],[int(w/2),int(h/2.2)],[0,h]], np.int32)
        triangle_img = cv.fillPoly(img,pts=[verts], color=(0, 0, 255))

        triangle_img_hsv = cv.cvtColor(triangle_img, cv.COLOR_BGR2HSV)
        lower_white = np.array([0,0,0], dtype=np.uint8)
        upper_white = np.array([0,0,255], dtype=np.uint8)
        white_triangle_mask = cv.inRange(triangle_img_hsv,  lower_white, upper_white)

        self.img_pub.publish(self.bridge.cv2_to_imgmsg(white_triangle_mask))


if __name__ == "__main__":
    rospy.init_node('triangle_mask')
    mask_publisher = TriangleMask()
    rospy.spin()
