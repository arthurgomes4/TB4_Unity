from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    
    # declare the ip and port arguements
    ip_arg = DeclareLaunchArgument('ip', default_value='127.0.0.1')
    port_arg = DeclareLaunchArgument('port', default_value='10000')

    # Launch the ros_tcp_endpoint node
    ros_tcp_endpoint_node = Node(
        package='ros_tcp_endpoint',
        executable='default_server_endpoint',
        output='screen',
        parameters=[
            {'ROS_IP': LaunchConfiguration('ip')},
            {'ROS_TCP_PORT': LaunchConfiguration('port')}
        ]
    )

    # robot state pub for TF
    pkg_turtlebot4_description = FindPackageShare('turtlebot4_description')
    xacro_file_path = PathJoinSubstitution([pkg_turtlebot4_description,
                                       'urdf','lite', 'turtlebot4.urdf.xacro'])
        
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {'use_sim_time': True},
            {'robot_description': Command([
                'xacro', ' ', xacro_file_path, ' ',
                'gazebo:=ignition', ' ',
                'namespace:=', '/'])}
        ],
        remappings=[
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static')
        ]
    )

    return LaunchDescription([
        ip_arg,
        port_arg,
        ros_tcp_endpoint_node,
        robot_state_publisher
    ])