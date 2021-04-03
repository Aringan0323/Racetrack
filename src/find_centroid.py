#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
fromt std_msgs import Int32

class findCentroid:

    def __init__(self):
        self.img_sub = rospy.Subscriber('/canny_mask', Image, self.img_callback)
        self.img_pub = rospy.Publisher('/centroidXVal', Int32, queue_size=1)
        self.bridge = cv_bridge.CvBridge()

    def img_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg)

        M = cv2.moments(img)

        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(img, (cx, cy), 20, (0,0,255), -1)
            self.img_pub.publish(cx)
        
if __name__ == "__main__":
    rospy.init_node('centroidXVal')
    mask_publisher = findCentroid()
    rospy.spin()

