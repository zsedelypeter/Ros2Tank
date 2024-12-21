import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class Control(Node):
    def __init__(self):
        super().__init__('control')
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.trt_pub = self.create_publisher(Float64, 'cmd_turret', 10)
        self.loop_count = 0
        self.timer = self.create_timer(0.1, self.loop)

    def loop(self):
        trt_msg = Float64()
        trt_msg.data = 0.5
        cmd_msg = Twist()
        cmd_msg.linear.x = 0.0
        cmd_msg.angular.z = 0.0
        self.trt_pub.publish(trt_msg)
        self.cmd_pub.publish(cmd_msg)

def main(args=None):
    rclpy.init(args=args)
    control = Control()
    rclpy.spin(control)
    control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()