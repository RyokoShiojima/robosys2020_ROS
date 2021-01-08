#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from googletrans import Translator

translator = Translator()

def trans_english(message):
	rospy.loginfo('送られてきたメッセージ:' + message.data + '\n\n翻訳結果:' + translator.translate(message.data, src='ja', dest='en').text)

rospy.init_node('listener')
sub = rospy.Subscriber('chat', String, trans_english)
rospy.spin()
