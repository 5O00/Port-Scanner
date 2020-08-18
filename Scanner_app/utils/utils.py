import socket, ipaddress

def ipv6(ip: str):
    try:
        ip = ipaddress.ip_address(ip)
    except ValueError:
        return False
    
    return isinstance(ip, ipaddress.IPv6Address)


def ipv4(ip: str):
    try:
        ip = ipaddress.ip_address(ip)
    except ValueError:
        return False
    
    return isinstance(ip, ipaddress.IPv4Address)

def get_ip(ip: str):
    try:
        return socket.gethostbyname()
    except:
        print("The host is invalid")
        exit(-1)

def parse_ports(ports: str):
    if not ":" in ports:
        if ports.isdigit() and int(ports) in range(0, 65536):
            return int(ports), int(ports) 
        else:
            raise Exception(f"Invalid port {ports}")
    
    else:
        ports = ports.split(":")
        port_min, port_max = ports[0], ports[1]
        if port_min.isdigit() and port_max.isdigit():
            port_min, port_max = int(port_min), int(port_max)

            if port_min in range(0, 65536) and port_max in range(0, 65536):
                return port_min, port_max
            else:
                raise Exception(f"Invalid port {ports}")
        
        else:
            raise Exception(f"Invalid port {ports}")

