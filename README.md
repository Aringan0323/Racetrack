# Racetrack

## Description
This program subscribes to image topics and publishes command topics to a turtlebot3 waffle model in order to drive it down a racetrack and keep it centered in the dotted white
lines. The program uses OpenCV in order to detect the edges of the dotted white lines in the center of the track and return the coordinates on the screen of the center of the
edges. The program then uses this center dot, named the centroid of the edges, to calculate an error and publish angular velocity commands to keep the centroid in the 
center of the robot's vision.

## Usage
In order to use this program, you must run the gazebo simulation world which can be found here: [Racetrack](http://cosi119r.s3-website-us-west-2.amazonaws.com/content/topics/robotics_pas/7_race_track.md/)
