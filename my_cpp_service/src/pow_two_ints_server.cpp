#include "rclcpp/rclcpp.hpp"
#include "my_interfaces/srv/pow_two_ints.hpp"

#include <memory>
#include <cmath>

void my_pow(const std::shared_ptr<my_interfaces::srv::PowTwoInts::Request> request,
          std::shared_ptr<my_interfaces::srv::PowTwoInts::Response> response)
{
  response->c = std::pow(2, request->a) + std::pow(3, request->b);
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Incoming request\na: %ld" " b: %ld",
                request->a, request->b);
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "sending back response: [%ld]", (long int)response->c);
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("pow_two_ints_server");

  rclcpp::Service<my_interfaces::srv::PowTwoInts>::SharedPtr service =
    node->create_service<my_interfaces::srv::PowTwoInts>("pow_two_ints", &my_pow);

  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready to pow two ints.");

  rclcpp::spin(node);
  rclcpp::shutdown();
}