#!/bin/bash

# install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-humble-rviz2 \
    ros-humble-ros2-control \
    ros-humble-joint-state-publisher-gui \
    ros-humble-controller-manager \
    ros-humble-joint-state-broadcaster \
    ros-humble-robot-state-publisher \
    ros-humble-urdf \
    ros-humble-xacro \
    ros-humble-rosbridge-suite \
    ros-humble-joint-state-publisher \
    ros-humble-ros2-controllers \
    ros-humble-topic-based-ros2-control \
    ros-humble-turtlebot4-description \
    ros-humble-irobot-create-control

RUN apt-get update -y && pip install rospkg jsonpickle