#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(message):
	rospy.loginfo(message.data)

rospy.init_node('listener')
sub = rospy.Subscriber('chat', String, callback)
rospy.spin()
