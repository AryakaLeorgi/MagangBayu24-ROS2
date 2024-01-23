import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.srv import TeleportAbsolute
import math

class TurtleShape(Node):

    def __init__(self):
        super().__init__('turtle_shape')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.count = 0
        self.reset_turtle()

    def reset_turtle(self):
        self.teleport_absolute(7.5, 5.0, 0.0)
        self.clear_turtlesim()

    def clear_turtlesim(self):
        clear_service = self.create_client(Empty, '/clear')
        while not clear_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for the clear service...')
        empty_request = Empty.Request()
        clear_future = clear_service.call_async(empty_request)
        rclpy.spin_until_future_complete(self, clear_future)
        self.get_logger().info('Clearing complete.')

    def teleport_absolute(self, x, y, theta):
        teleport_service = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        while not teleport_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for the teleport_absolute service...')

        request = TeleportAbsolute.Request()
        request.x = x 
        request.y = y 
        request.theta = theta  

        future = teleport_service.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info('Teleportation complete.')

    def timer_callback(self):
        msg = Twist()

        if self.count == 0:
            msg.angular.z = math.radians(180)  
            self.get_logger().info('Rotating...') 

        elif self.count % 2 == 1 and self.count < 7 and self.count > 0:
            msg.linear.x = 4.0  
            self.get_logger().info('Moving Forward...')

        elif self.count % 2 == 0 and self.count < 6 and self.count > 0:
            msg.angular.z = math.radians(-120)  
            self.get_logger().info('Rotating...') 
        
        elif self.count == 7:
            msg.angular.z = math.radians(-30)  
            self.get_logger().info('Rotating...')         
        
        elif self.count > 7 and self.count % 2 == 0:
            msg.linear.x = 6.2  
            msg.angular.z = math.radians(-178) 
            self.get_logger().info('Moving in a curved path for Half Circle...') 

        elif self.count == 9:
            msg.angular.z = math.radians(60)  
            self.get_logger().info('Rotating...')   
        
        elif self.count == 11:
            msg.angular.z = math.radians(60)  
            self.get_logger().info('Rotating...')  
        
        self.publisher.publish(msg)
        self.count += 1

        if self.count == 13:  
            self.get_logger().info('Shape completed.')
            self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    turtle_shape = TurtleShape()
    try:
        rclpy.spin(turtle_shape)

    finally:
        turtle_shape.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()