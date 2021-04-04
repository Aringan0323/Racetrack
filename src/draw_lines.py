#!/usr/bin/env python

import rospy, cv2, cv_bridge
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
        self.bridge = cv_bridge.CvBridge()
        self.lines = None

    def img_cb(self, img_msg):

        img = self.bridge.imgmsg_to_cv2(img_msg)
        self.lines = cv2.HoughLinesP(img, 1, np.pi/180,80, minLineLength=10, maxLineGap=250)

    def og_img_cb(self, img_msg):
        img = self.bridge.imgmsg_to_cv2(img_msg, 'bgr8')

        try:
            for line in self.lines:
                x1, y1, x2, y2 = line[0]
                img = cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 3)
            self.img_pub.publish(self.bridge.cv2_to_imgmsg(img))
        except TypeError as e:
            pass

if __name__ == "__main__":
    rospy.init_node('centroid_finder')
    mask_publisher = TriangleMask()
    edge_detector = EdgeDetection()
    line_finder = Lines()
    rospy.spin()
