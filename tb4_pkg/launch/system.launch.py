from  launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    endpoint_file_path = PathJoinSubstitution([FindPackageShare('ur5e_pkg'), 'launch', 'endpoint.launch.py'])
    rviz_file = PathJoinSubstitution([FindPackageShare('ur5e_pkg'), 'launch', 'rviz.launch.py'])

    endpoint_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(endpoint_file_path)
    )

    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rviz_file)
    )

    return LaunchDescription([
        endpoint_launch,
        rviz_launch
        ])