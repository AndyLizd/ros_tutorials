#!/usr/bin/python

import rospy
import numpy as np


if __name__ == '__main__':
    rospy.init_node('my_first_python_node')
    rospy.loginfo('hello world!')

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo('hello')
        rate.sleep()

    
    
