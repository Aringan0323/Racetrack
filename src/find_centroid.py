#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from preprocess_img import TriangleMask
from edge_detection import EdgeDetection

class findCentroid:

    def __init__(self):
        self.img_sub = rospy.Subscriber('/canny_mask', Image, self.img_callback)
        self.img_pub = rospy.Publisher('/centroid_img', Image, queue_size=1)
        self.centroid_pub = rospy.Publisher('/centroidXVal', Int32, queue_size=1)
        self.bridge = cv_bridge.CvBridge()

    def img_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg)

        # Create Centroid
        M = cv2.moments(img)

        # Add centroid to middle of dashed line
        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            img = cv2.circle(img, (cx, cy), 20, (255,255,255), -1)
            self.img_pub.publish(self.bridge.cv2_to_imgmsg(img))

            # Publish for use in PID
            self.centroid_pub.publish(cx)
        
if __name__ == "__main__":
    rospy.init_node('centroid_finder')
    mask_publisher = TriangleMask()
    edge_detector = EdgeDetection()
    centroid_finder = findCentroid()
    rospy.spin()
