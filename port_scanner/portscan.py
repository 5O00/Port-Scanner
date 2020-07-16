from utils.args import parse_args
from utils.utils import is_ipv6, is_ipv4, get_ip
from core.scan import start_scan

import socket

args = parse_args()

def main(args):
    ip = args.host
    if (is_ipv4(ip)):
        ipv = socket.AF_INET

    elif (is_ipv6(ip)):
        ipv = socket.AF_INET6

    else:
        ip = get_ip(ip)

    start_scan(ip, args.port, args.maxt)

if __name__ == "__main__":
    args = parse_args()
    main(args)