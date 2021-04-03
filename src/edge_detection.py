#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sensor_msgs.msg import Image

class EdgeDetection:

    def __init__(self):
        self.img_sub = rospy.Subscriber('/triangle_mask', Image, self.img_callback)
        self.img_pub = rospy.Publisher('/canny_mask', Image, queue_size=1)
        self.bridge = cv_bridge.CvBridge()

    def img_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        kernelSize = 31
        grayBlur = cv2.GaussianBlur(gray, (kernelSize, kernelSize), 0)

        lowEnd = 30
        highEnd = 100
        edges = cv2.Canny(grayBlur, lowEnd, highEnd)

        self.img_pub.publish(self.bridge.cv2_to_imgmsg(edges))

if __name__ == "__main__":
    rospy.init_node('canny_mask')
    mask_publisher = EdgeDetection()
    rospy.spin()


        
    
