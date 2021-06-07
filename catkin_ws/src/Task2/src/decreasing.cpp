#include <ros/ros.h>
#include <std_msgs/Int32.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "decrease");
    ros::NodeHandle node;
    ros::Publisher pub = node.advertise<std_msgs::Int32>("dec", 10);
    ros::Rate rate(1);
    int count = 0;
    std_msgs::Int32 msg;

    while (ros::ok()) {
        msg.data = count;
        pub.publish(msg);
        --count;
        rate.sleep();
    }
    return 0;
}