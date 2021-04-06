#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from std_msgs.msg import Int32
from sensor_msgs.msg import LaserScan

'''
This class is not used in the main program. The original intention for this function was to 
detect obstacles in the robot's path and then publish an offset value that determined where it
should move to avoid the obstacle.
'''

class obstacleDetector:

    def __init__(self):
        
        self.lidar_sub = rospy.Subscriber('/scan', LaserScan, self.laser_cb)
        self.offset_pub = rospy.Publisher('/offset', Int32, queue_size=1)

    def laser_cb(self, msg):
        # Looks in front of the robot for obstacles and publishes the index in the ranges array
        # of the closest object in front of the robot.
        ranges = msg.ranges
        n = len(ranges)
        front_left = ranges[0:int(n/30)]
        front_right = ranges[int((23*n)/24):n]
        front_right = np.flip(front_right, axis=0)
        front = np.concatenate((front_left, front_right), axis=0)
        fours = np.array([4]*len(front))
        clean_front = np.where(front > 3, fours, front)
        minimum = np.min(clean_front)
        if minimum < 4:
            print(np.argmin(clean_front))

    
    # def calculate_offset(self, front):
    #     l = len(front)
    #     max_run_start = -1
    #     max_run_end = -1
    #     curr_run_start = -1
    #     for i in range(l):
    #         if front[i] < 4:
    #             if curr_run_start == -1:
    #                 curr_run_start = i
    #         else:
    #             counter


if __name__ == "__main__":
    rospy.init_node('object_detector')
    detector = obstacleDetector()
    rospy.spin()