#!/usr/bin/env python3
#coding utf-8

import rospy
from std_msgs.msg import String
from datetime import datetime, timezone

rospy.init_node('speaker')
pub = rospy.Publisher('chat', String, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
	send_word = String()
	message = input('送りたいメッセージを入力してEnterを押してね。終わりたい時は Ctrl+c を入力した後Enterを押してね。\n')
	time_stamp = rospy.get_time()
	time = str(datetime.fromtimestamp(time_stamp))
	send_word = message + ' [送信時刻: ' + time + ']'
	pub.publish(send_word)
	rate.sleep()
