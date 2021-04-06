# Racetrack

## Description
This program subscribes to image topics and publishes command topics to a turtlebot3 waffle model in order to drive it down a racetrack and keep it centered in the dotted white
lines. The program uses OpenCV in order to detect the edges of the dotted white lines in the center of the track and return the coordinates on the screen of the center of the
edges. The program then uses this center dot, named the centroid of the edges, to calculate an error and publish angular velocity commands to keep the centroid in the 
center of the robot's vision.

## Usage
In order to use this program, you must run the gazebo simulation world which can be found here: [Racetrack](http://cosi119r.s3-website-us-west-2.amazonaws.com/content/topics/robotics_pas/7_race_track.md/)

* Once you have run the simulation, run the launch file provided in the launch folder with the following command: <code>roslaunch (PACKAGE_NAME) racetrack.launch</code>.
* The robot will then follow the dashed white line around the track.
* Optionally, you may look at the lines drawn by the Hough Lines algorithm by concurrently running the command <code> rosrun (PACKAGE_NAME) draw_lines.launch</code>, and subscribing to the topic <code>/line_overlay</code> in rviz.

## Video link
[Demonstration](https://drive.google.com/file/d/1D29quLxCBVsaLuOplft5w5oRcnpH0hVZ/view?usp=sharing)