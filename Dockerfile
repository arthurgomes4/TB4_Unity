FROM ros:humble-ros-base

# set frontend noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Prevent hash mismatch error for apt-get update, qqq makes the terminal quiet while downloading pkgs
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && apt-get update -yqqq

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

# create a ROS workspace
ARG ROS2_WS=/root/ros2_ws
RUN mkdir -p ${ROS2_WS}/src

# copy the contents of repo
COPY . ${ROS2_WS}/src

# clone the tcp endpoint repo
RUN cd ${ROS2_WS}/src && git clone https://github.com/Unity-Technologies/ROS-TCP-Endpoint.git -b ROS2v0.7.0

# build the workspace
SHELL ["/bin/bash", "-c"]

RUN cd ${ROS2_WS} && source /opt/ros/${ROS_DISTRO}/setup.sh && colcon build

# copy the ROS paths to the bashrc
RUN echo "source ${ROS2_WS}/install/setup.bash" >> /root/.bashrc