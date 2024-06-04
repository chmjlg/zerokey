import os
from typing import Final, List

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchContext, LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch_ros.descriptions import ParameterFile
from nav2_common.launch import ReplaceString, RewrittenYaml


def launch_setup(context: LaunchContext):
    
    zk_pose_node = Node(
        package="pose",
        executable="zkPose",
        name="pose",
        output="screen",
    )

    return [zk_pose_node]


def generate_launch_description() -> LaunchDescription:
    ld = LaunchDescription()
    ld.add_action(OpaqueFunction(function=launch_setup))
    return ld