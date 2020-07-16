from utils.utils import parse_ports

import socket
import argparse


def start_scan(ip: str, ports: str, max_thread: int):
    (port_min, port_max) = parse_ports(ports)

    queue = queue.Queue()

    for i in range(port_min, port_max+1):
        queue.append(i)

    for i in range(0, max_thread):
        thread = Worker(scan_port, queue)
        thread.start()

