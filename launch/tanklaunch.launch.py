from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    tank_sdf = '/home/ajr/ros2_ws/src/ros2tank/simulation/tank.sdf'
    rviz_config_dir = os.path.join(get_package_share_directory('ros2tank'), '')
    rviz_config_file = os.path.join(rviz_config_dir, 'rvizconfig.rviz')


    print(f"Looking for tank.sdf at: {tank_sdf}")

    gazebo = ExecuteProcess(
        cmd=['ign', 'gazebo', '-r', tank_sdf],
        output='screen'
    )

    # Configure RViz
    package_name = 'ros2tank'  # replace with your actual package name
    rviz_config_dir = os.path.join(get_package_share_directory(package_name), 'rviz')
    rviz_config_file = os.path.join(rviz_config_dir, 'tank_lidar.rviz')

    rviz_node = Node(
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    arguments=['-d', rviz_config_file],
    output='screen'
)

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/lidar/points@sensor_msgs/msg/PointCloud2@ignition.msgs.PointCloudPacked'],
        output='screen'
    )

# Launch tf tree
    tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', '1', 'tank/chassis/gpu_lidar', 'base_link'],
        output='screen'
    )

    # Add control node
    control_node = Node(
        package='ros2tank',
        executable='control',
        name='control',
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(gazebo)
    ld.add_action(rviz_node)
    ld.add_action(bridge)
    ld.add_action(tf_node)
    ld.add_action(control_node)

    return ld