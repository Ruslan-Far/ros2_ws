from my_interfaces.srv import PowTwoInts

import rclpy
from rclpy.node import Node


class PowTwoIntsServer(Node):

    def __init__(self):
        super().__init__("pow_two_ints_server")
        self.srv = self.create_service(PowTwoInts, "pow_two_ints", self.pow_two_ints_callback)

    def pow_two_ints_callback(self, request, response):
        response.c = 2 ** request.a + 3 ** request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main(args=None):
    rclpy.init(args=args)

    pow_two_ints_server = PowTwoIntsServer()

    rclpy.spin(pow_two_ints_server)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
