#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import message_filters

rospy.init_node("constant")

class constant:
    def __init__(self):
        self.constant = Int32()
        self.subs_inc = message_filters.Subscriber("/inc", Int32)
        self.subs_dec = message_filters.Subscriber("/dec", Int32)
        self.ts = message_filters.TimeSynchronizer([self.subs_inc, self.subs_dec], 1)
        self.ts.registerCallback(self.callback_func)
    def callback_func(self, inc, dec):
        self.constant = inc+dec

constant_obj = constant()
publisher = rospy.Publisher("/const", Int32, queue_size=1)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    publisher.publish(constant_obj.constant)
    rate.sleep()
