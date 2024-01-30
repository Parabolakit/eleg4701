#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import sys
import rospy
import math  # TODO 1: import math to use atan2() easily.
from geometry_msgs.msg import Twist  # TODO 2: import all message types you need.
from turtlesim.msg import Pose
from my_pkg.msg import Mypose

ROBOT_X = 0.0
ROBOT_Y = 0.0
ROBOT_T = 0.0

def pose_callback(pose):
    global ROBOT_X, ROBOT_Y, ROBOT_T

    rospy.loginfo("Robot 2 X = %f: Y=%f: Z = %f\n", pose.x, pose.y, pose.theta)
    ROBOT_X = pose.x  # TODO 3: assign the robot pose to the global variables.
    ROBOT_Y = pose.y
    ROBOT_T = pose.theta

def myPose_callback(myPose):
    global vel
    diff_x = ROBOT_X - myPose.x
    diff_y = ROBOT_Y - myPose.y
    angle_to_other_robot = math.atan2(diff_y, diff_x)

    # TODO 4: The speed is controlled by the difference between the poses of the two robots to achieve following. 
    # Hints:   1. P-control: Use k times the position difference between the X and Y axis to control the x linear speed. 
    #          2. Make the angle of the robot2 always face the other robot. 
    #          3. Think about how to calculate the difference of two angles using atan2()
    k = 1  # Proportional gain
    linear_speed = k * math.sqrt(diff_x**2 + diff_y**2)
    angular_speed = k * (angle_to_other_robot - ROBOT_T)

    vel.linear.x = linear_speed
    vel.angular.z = angular_speed

def follow_turtle():
    rospy.init_node('follow_turtle')  # TODO 5: initialize node 'follow_turtle'

    pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)  # TODO 6: define a publisher: topic name is '/turtle2/cmd_vel'.

    rospy.Subscriber('/turtle1/Mypose', Mypose, myPose_callback)  # TODO 7: define a subscriber: topic name is '/turtle1/Mypose'.
    rospy.Subscriber('/turtle2/pose', Pose, pose_callback)  # TODO 8: define a subscriber: topic name is '/turtle2/pose'.

    global vel
    vel = Twist()  # TODO 9: initialize the variable vel with the message type.

    rate = rospy.Rate(10)       
    while not rospy.is_shutdown():
        pub.publish(vel)  # Publish vel.
        rate.sleep()

if __name__ == '__main__':
    try:
        follow_turtle()
    except rospy.ROSInterruptException:
        pass
