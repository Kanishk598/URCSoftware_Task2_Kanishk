cmake_minimum_required(VERSION 2.8.3)
project(Task2)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

## Declare ROS messages and services
#add_message_files(FILES Num.msg)
#add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(increase src/increasing.cpp)
target_link_libraries(increase ${catkin_LIBRARIES})
add_dependencies(increase task2_generate_messages_cpp)

add_executable(decrease src/decreasing.cpp)
target_link_libraries(decrease ${catkin_LIBRARIES})
add_dependencies(decrease task2_generate_messages_cpp)

add_executable(constant src/constant.cpp)
target_link_libraries(constant ${catkin_LIBRARIES})
add_dependencies(constant task2_generate_messages_cpp)
