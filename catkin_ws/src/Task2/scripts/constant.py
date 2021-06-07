#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import message_filters

rospy.init_node("constant")

class constant:
    def __init__(self):
        self.constant = Int32()
        self.subs_inc = rospy.Subscriber("/inc", Int32, self.callback_inc)
        self.subs_dec = rospy.Subscriber("/dec", Int32, self.callback_dec)
    def callback_inc(self, inc):
        self.constant.data = inc.data
        print("inc: ", self.constant)
    def callback_dec(self, dec):
        self.constant.data = self.constant.data + dec.data
        print("inc+dec: ", self.constant)

constant_obj = constant()
publisher = rospy.Publisher("/const", Int32, queue_size=1)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    publisher.publish(constant_obj.constant)
    print("published data is: ", constant_obj.constant)
    rate.sleep()
