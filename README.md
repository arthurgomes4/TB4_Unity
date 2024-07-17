# TB4_Unity

This project demonstrates using the **Unity Simulation Engine** to simulate a **Clear Path Robotics Turtlebot4** with ROS2 humble.

[image here]()

## Quick Start

### Install Prerequisites
This project can be used with either docker or a native ROS2 humble installation. Unity needs to be installed natively in both cases.
* Install the [Unityhub](https://docs.unity3d.com/hub/manual/InstallHub.html#install-hub-linux), once installed, install editor version: `2022.3.1711` or newer. (older versions may also work, but no guarantees given).
* Install git. Most users will have git preinstalled but if not then install from [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

* **If using docker**: Install [docker engine](https://docs.docker.com/engine/install/ubuntu/) and perform [post-install steps](https://docs.docker.com/engine/install/linux-postinstall/). (recommended way).
* **If using ROS2 natively**: The project requires an installation of ROS2 Humble to work, although it should work on other ROS2 distros just as well. [Install humble](https://docs.ros.org/en/humble/Installation.html) if not installed already.

### Cloning, installing dependencies and building workspace
These instructions are for Linux:

**docker users**: Clone the repository an build the docker image with:
```bash
git https://github.com/arthurgomes4/TB4_Unity.git # -b <name> if using any branch

cd TB4_Unity && ./use_docker.sh --build # build the image
```

**Native ROS2 users**: Create a ROS2 workspace, clone the repo and install dependencies with the following commands:
```bash
mkdir -p ros2_ws/src

cd ros2_ws/src

git clone https://github.com/arthurgomes4/TB4_Unity.git
git clone https://github.com/Unity-Technologies/ROS-TCP-Endpoint.git -b main-ros2

sudo ./TB4_Unity/install_dependencies.sh # root required

cd .. && colcon build
```

### Open Unity Project
Open the Unity Hub and add the [tb4_project](./tb4_project/). Open the project and ensure there are no compile errors. Open the [SampleScene.unity](./tb4_project/Assets/Scenes/SampleScene.unity) and press the play button to start the simulation.

### Run ROS nodes

**docker users**: Run the container and enter the container with the [use_docker.sh](./use_docker.sh).
```bash
./use_docker.sh --run

./use_docker.sh --enter

ros2 launch tb4_pkg system.launch.py # inside the container
```

**Native ROS2 users**: Source your workspace and run the ROS nodes with the following commands:
```bash
source install/setup.bash

ros2 launch tb4_pkg system.launch.py
```
