#!/usr/bin/env python 

import rospy
from rospy_tutorials.srv import AddTwoInts


def handle_add_two_ints(req):
    result = req.a + req.b
    rospy.loginfo('sum of ' + str(req.a) + ' and '+ str(req.b) + ' is ' + str(result))
    return result


if __name__ == '__main__':

    rospy.init_node('add_two_ints_server')
    rospy.loginfo('Add two ints server node created')

    service = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    rospy.loginfo('Service has been started')

    rospy.spin()

    
    


