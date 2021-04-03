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
        verts = np.array([[w,h],  [0,h], [int(w/2), int(h/2)]], np.int32)
        masked_img = cv.fillPoly(img,pts=[verts], color=(0, 0, 255))
        cv.imshow("Mask", masked_img)
        self.img_pub.publish(self.bridge.cv2_to_imgmsg(masked_img))


if __name__ == "__main__":
    rospy.init_node('triangle_mask')
    mask_publisher = TriangleMask()
    rospy.spin()
