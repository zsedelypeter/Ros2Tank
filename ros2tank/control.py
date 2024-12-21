# filepath: /home/ajr/ros2_ws/src/ros2tank/ros2tank/control.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Control(Node):
    def __init__(self):
        super().__init__('control')
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.loop_count = 0
        self.timer = self.create_timer(0.1, self.loop)

    def loop(self):
        cmd_msg = Twist()
        if self.loop_count < 20:
            cmd_msg.linear.x = 0.5
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 40:
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = 0.5
        else:
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = 0.0
            self.loop_count = 0
        self.cmd_pub.publish(cmd_msg)
        self.loop_count += 1

def main(args=None):
    rclpy.init(args=args)
    control = Control()
    rclpy.spin(control)
    control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()