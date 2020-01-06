#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

if __name__ == '__main__':

    rospy.init_node('num_pub', anonymous=True)
    pub = rospy.Publisher('/number_publisher', Int64, queue_size = 10)
    
    publish_frequency = rospy.get_param('/number_publish_frequency')
    rate = rospy.Rate(publish_frequency)

    number = rospy.get_param('/number_to_publish')

    rospy.set_param('/another_param', 'hello')

    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = number
        pub.publish(msg)
        rate.sleep()


