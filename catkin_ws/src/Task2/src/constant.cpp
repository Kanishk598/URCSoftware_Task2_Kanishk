#include "ros/ros.h"
#include "std_msgs/Int32.h"

std_msgs::Int32 inc;
std_msgs::Int32 dec;
std_msgs::Int32 constant;


void inc_callback(std_msgs::Int32 message)
{
    inc.data = message.data;
}
void dec_callback(std_msgs::Int32 message)
{
    dec.data = message.data;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "constant");
    ros::NodeHandle nh;

    ros::Subscriber sub_inc = nh.subscribe("inc", 10, inc_callback);
    ros::Subscriber sub_dec = nh.subscribe("dec", 10, dec_callback);
    ros::Publisher pub_const = nh.advertise<std_msgs::Int32>("const", 10);

    ros::Rate rate(1);
    while (ros::ok())
    {
        constant.data = inc.data + dec.data;
        pub_const.publish(constant);
        rate.sleep();
    }

    return 0;
}

