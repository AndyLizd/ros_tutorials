#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

pub = None
counter = 0

def callback_receive(msg):
    global counter
    counter += msg.data
    new_msg = Int64()
    new_msg.data = counter
    pub.publish(new_msg)

def reset_funct(is_reset):
    if is_reset.data:
        global counter
        counter = 0
        return True, 'reset counter!'
    return False, 'No reset!'


if __name__ == '__main__':

    rospy.init_node('counter')

    sub = rospy.Subscriber('/number_publisher', Int64, callback_receive)

    pub = rospy.Publisher('/number_count', Int64, queue_size = 10)
    
    serv = rospy.Service('/reset_number_count', SetBool, reset_funct)

    rospy.spin()



