#!/usr/bin/env python

import rospy, cv2, cv_bridge
import math
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from preprocess_img import TriangleMask
from edge_detection import EdgeDetection


class Lines:

    def __init__(self):

        self.img_sub = rospy.Subscriber('/canny_mask', Image, self.img_cb)
        self.og_img_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.og_img_cb)
        self.img_pub = rospy.Publisher('/line_overlay', Image, queue_size=1)
        self.theta_pub = rospy.Publisher('/theta', Int32, queue_size=1)
        self.bridge = cv_bridge.CvBridge()
        self.lines = None

    def img_cb(self, img_msg):

        img = self.bridge.imgmsg_to_cv2(img_msg)

        self.lines = cv2.HoughLines(img,  1, math.pi / 180, 100, 0, 0, min_theta=0, max_theta=math.pi/2)

    def og_img_cb(self, img_msg):
        img = self.bridge.imgmsg_to_cv2(img_msg, 'bgr8')
        try:
            thetalist = []
            for line in self.lines:
                rho = line[0][0]
                theta = line[0][1]
                thetalist.append(theta)
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                img = cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 3)
            avgtheta = (sum(thetalist)/len(thetalist))
            avgangle = avgtheta*(180/math.pi)
            self.img_pub.publish(self.bridge.cv2_to_imgmsg(img))
        except TypeError as e:
            avgangle = 180
            pass
        self.theta_pub.publish(int(avgangle))

if __name__ == "__main__":
    rospy.init_node('centroid_finder')
    mask_publisher = TriangleMask()
    edge_detector = EdgeDetection()
    line_finder = Lines()
    rospy.spin()
