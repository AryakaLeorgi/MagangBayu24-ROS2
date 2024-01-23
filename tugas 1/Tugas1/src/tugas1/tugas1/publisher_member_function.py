import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class MathPublisher(Node):
    def __init__(self):
        super().__init__('math_publisher')
        self.publisher_ = self.create_publisher(String, 'math_problem', 10)
        self.timer = self.create_timer(1, self.publish_math_problem)

    def publish_math_problem(self):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        num3 = random.randint(1, 1000)
        operators = ['+', '-', '*', '/', '%']
        opr1 = random.choice(operators)
        opr2 = random.choice(operators)
        math_problem = f"{num1} {opr1} {num2} {opr2} {num3}"
        msg = String()
        msg.data = math_problem
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {math_problem}")

def main(args=None):
    rclpy.init(args=args)
    math_publisher = MathPublisher()
    rclpy.spin(math_publisher)
    math_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
