
# Before execuing this launch file, CMakeLists.txt should be modified to include the following

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import Command

def generate_launch_description():
    moveit_config_dir = get_package_share_directory('fanuc_m710ic_support_moveit_config')
    robot_description_path = os.path.join(moveit_config_dir, 'config', 'fanuc_m710ic45m.urdf.xacro')
    robot_description_semantic_path = os.path.join(moveit_config_dir, 'config', 'fanuc_m710ic45m.srdf')
    kinematics_yaml_path = os.path.join(moveit_config_dir, 'config', 'kinematics.yaml')
    controllers_yaml_path = os.path.join(moveit_config_dir, 'config', 'ros2_controllers.yaml')

    robot_description = Command(['xacro ', robot_description_path])

    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_description_path',
            default_value=robot_description_path,
            description='Path to the URDF/XACRO file'
        ),
        DeclareLaunchArgument(
            'robot_description_semantic_path',
            default_value=robot_description_semantic_path,
            description='Path to the SRDF file'
        ),
        DeclareLaunchArgument(
            'kinematics_yaml_path',
            default_value=kinematics_yaml_path,
            description='Path to the kinematics YAML file'
        ),
        DeclareLaunchArgument(
            'controllers_yaml_path',
            default_value=controllers_yaml_path,
            description='Path to the controllers YAML file'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
            }],
        ),
        Node(
            package='moveit_ros_move_group',
            executable='move_group',
            name='move_group',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'robot_description_semantic': LaunchConfiguration('robot_description_semantic_path'),
                'robot_description_kinematics': LaunchConfiguration('kinematics_yaml_path'),
            }],
        ),
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[LaunchConfiguration('controllers_yaml_path')],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(moveit_config_dir, 'config', 'moveit.rviz')],
        ),
    ])
