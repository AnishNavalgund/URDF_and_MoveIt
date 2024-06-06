import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the package share directory
    pkg_share = get_package_share_directory('fanuc_m710ic_support')

    # Define the path to the URDF file
    default_urdf_path = os.path.join(pkg_share, 'urdf', 'm710ic45m.urdf')

    # Read the URDF file content
    try:
        with open(default_urdf_path, 'r') as file:
            robot_description_content = file.read()
    except Exception as e:
        raise RuntimeError("Failed to read URDF file: {}".format(e))

    # Define the path to the RViz configuration file
    default_rviz_config_path = os.path.join(pkg_share, 'rviz', 'robot_config.rviz')

    return LaunchDescription([
        # Node to launch RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', default_rviz_config_path],
            output='screen'),

        # Node to launch robot_state_publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='both',
            parameters=[{'robot_description': robot_description_content}],
        ),
    ])

