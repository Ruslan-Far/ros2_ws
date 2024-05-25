from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    a = LaunchConfiguration("a")
    b = LaunchConfiguration("b")

    a_launch_arg = DeclareLaunchArgument(
        "a",
        default_value=""
    )
    b_launch_arg = DeclareLaunchArgument(
        "b",
        default_value=""
    )

    server = Node(
        package="my_cpp_service",
        executable="server",
        name="pow_two_ints_server"
    )
    
    run_client = ExecuteProcess(
        cmd=[[
            "ros2 run my_cpp_service client ",
            a,
            " ",
            b,
        ]],
        shell=True
    )

    return LaunchDescription([
        a_launch_arg,
        b_launch_arg,
        server,
        run_client,
    ])
