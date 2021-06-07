#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32


inc = Int32()
rospy.init_node("increasing")
rate = rospy.Rate(1)
publisher = rospy.Publisher("/inc", Int32, queue_size=5)
while not rospy.is_shutdown():
    print("Inc: ", inc)
    publisher.publish(inc)
    inc.data += 1
    rate.sleep()
