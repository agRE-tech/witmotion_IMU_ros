
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('witmotion_ros'),
        'config',
        'wt901.yml'
        )
        
    node=Node(
        package = 'witmotion_ros',
        executable = 'witmotion_ros_node',
        parameters = [config],
        arguments=['--ros-args', '--log-level', "debug"]

    )

    ld.add_action(node)
    return ld