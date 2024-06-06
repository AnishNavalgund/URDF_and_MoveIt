import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from rclpy.clock import ROSClock
import math

class JointStatePublisher(Node):
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz
        self.joint_state = JointState()
        self.joint_state.name = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
        self.joint_state.position = [0.0] * 6  # Initialize with zeros or appropriate initial positions
        self.joint_state.velocity = [0.0] * 6  # Initialize with zeros if unknown
        self.joint_state.effort = [0.0] * 6    # Optional, depends on whether effort is being controlled
        self.counter = 0

    def timer_callback(self):
        self.joint_state.header.stamp = ROSClock().now().to_msg()
        # Oscillate positions for demonstration
        self.joint_state.position = [0.5 * math.sin(self.counter * 0.1)] * 6
        self.counter += 1
        self.publisher.publish(self.joint_state)

def main(args=None):
    rclpy.init(args=args)
    joint_state_publisher = JointStatePublisher()
    rclpy.spin(joint_state_publisher)
    joint_state_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
