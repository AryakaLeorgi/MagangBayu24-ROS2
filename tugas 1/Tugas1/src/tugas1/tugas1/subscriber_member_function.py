import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MathSubscriber(Node):
    def __init__(self):
        super().__init__('math_subscriber')
        self.subscription = self.create_subscription(
            String,
            'math_problem',
            self.calculate_math_problem,
            10
        )

    def calculate_math_problem(self, msg):
        math_problem = msg.data
        result = eval(math_problem)
        self.get_logger().info(f"Received: {math_problem} = {result}")

def main(args=None):
    rclpy.init(args=args)
    math_subscriber = MathSubscriber()
    rclpy.spin(math_subscriber)
    math_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
