#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class MultiRobotCoordinator(Node):
    def __init__(self):
        super().__init__('coordinator_node')

        # Parameters
        self.timeout = 2.0
        self.queue_size = 10
        self.sync_frequency = 1.0  # Hz

        # Log startup
        self.get_logger().info(
            f"Coordinator Active | Timeout: {self.timeout}s | "
            f"Queue: {self.queue_size} | Freq: {self.sync_frequency}Hz"
        )

        # Timer (calls callback every 1 second)
        timer_period = 1.0 / self.sync_frequency
        self.timer = self.create_timer(timer_period, self.sync_callback)

    def sync_callback(self):
        self.get_logger().info("Coordinating Robot 1 and Robot 2...")


def main(args=None):
    rclpy.init(args=args)

    node = MultiRobotCoordinator()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down coordinator node...")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()