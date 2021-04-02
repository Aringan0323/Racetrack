#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2 as cv
from cv_bridge import CvBridge, CvBridgeError

class TriangleMask:
    
    def __init__(self):
        self.img_sub = rospy.Subscriber('/camera/rgb/imgage_raw', Image, img_callback)
        self.img_pub = rospy.Publisher('/triangle_mask', Image, queue_size=1)
        self.bridge = CvBridge()

    def img_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        w = img.size[0]
        h = img.size[0]
        apex = [int(w/2), int(h/2)]
        left_vert = [0,h]
        right_vert = [w,h]
        verts = np.array([apex, left_vert, right_vert], np.int8).reshape((-1, 1, 2))
        masked_img = cv2.fillPoly(img, [verts], color=(0, 0, 255))
        self.img_pub.publish(masked_img)


if __name__ == "__main__":
    rospy.init_node('triangle_mask')
    mask_publisher = TriangleMask()
    rospy.spin()
