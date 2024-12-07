from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    tank_sdf='/home/ajr/ros2_ws/src/ros2tank/simulation/tank.sdf'


    print(f"Looking for tank.sdf at: {tank_sdf}")

    gazebo = ExecuteProcess(
        cmd=['ign', 'gazebo', '-r', tank_sdf],
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(gazebo)

    return ld