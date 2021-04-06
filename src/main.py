#!/usr/bin/env python

from edge_detection import EdgeDetection
from find_centroid import findCentroid 
from pid import pid
from preprocess_img import TriangleMask
from draw_lines import Lines
import rospy

if __name__ == "__main__":
    rospy.init_node('main')
    pi = TriangleMask()
    ed = EdgeDetection()
    fc = findCentroid()
    pd = pid()
    rospy.spin()