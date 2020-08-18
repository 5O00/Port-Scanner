from utils.arguments import parse_args
from utils.utils import ipv4, ipv6, get_ip
from scan import start_scan
import socket

args = parse_args()

def main(args):
    ip = args.host
    if (ipv4(ip)):
        ipv = socket.AF_INET
    
    elif(ipv6(ip)):
        ipv = socket.AF_INET6
    
    else:
        ipv = get_ip(ip)
    
    start_scan(ip, args.ports, args.maxt)

if __name__ == "__main__":
    args = parse_args()
    main(args)

