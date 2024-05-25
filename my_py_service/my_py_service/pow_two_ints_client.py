import sys

from my_interfaces.srv import PowTwoInts
import rclpy
from rclpy.node import Node

class PowTwoIntsClientAsync(Node):

    def __init__(self):
        super().__init__("pow_two_ints_client")
        self.cli = self.create_client(PowTwoInts, "pow_two_ints")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = PowTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    pow_two_ints_client = PowTwoIntsClientAsync()
    response = pow_two_ints_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    pow_two_ints_client.get_logger().info(
        'Result of pow_two_ints: for 2^%d + 3^%d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.c))

    pow_two_ints_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
