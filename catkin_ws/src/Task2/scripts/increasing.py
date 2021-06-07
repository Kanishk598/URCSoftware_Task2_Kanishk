#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64


inc = 0
rospy.init_node("increasing")
rate = rospy.Rate(1)
publisher = rospy.Publisher("/inc", Int64)

while not rospy.is_shutdown():
    publisher.publish(inc)
    inc += 1
    rate.sleep()
