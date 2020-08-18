import argparse
from utils.utils import parse_ports

def parse_args():
    parser = argparse.ArgumentParser(
        usage="Enter usage",
        description="A simple Port Scanner")

    parser.add_argument("-i","--ip",
    help="IP/domain name to scan",
    type=str,
    required=True)

    parser.add_argument("-p","--port",
    help="Port to scan",
    type=str,
    default="0:1000")

    parser.add_argument("-t", "--thread",
    help="number of thread",
    type=int,
    required=False,
    default=30)
    
    return parser.parse_args()