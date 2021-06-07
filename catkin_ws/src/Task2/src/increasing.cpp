#include <ros/ros.h>
#include <std_msgs/Int64.h>

int main()
{
    ros::NodeHandle nh;
    ros::init("increasing");
    ros::Publisher pub = nh.advertise<std_msgs::Int64>("inc", 1);
    std_msgs::Int64 inc = 0;
    ros::Rate rate(1);
    while (ros::ok())
    {
        pub.publish(inc);
        ++inc;
        rate.sleep();
    } 
    return 0;
}