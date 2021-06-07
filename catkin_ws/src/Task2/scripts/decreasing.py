#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32


dec = Int32()
rospy.init_node("decreasing")
rate = rospy.Rate(1)
publisher = rospy.Publisher("/dec", Int32, queue_size=5)

while not rospy.is_shutdown():
    publisher.publish(dec)
    dec.data -= 1
    rate.sleep()
