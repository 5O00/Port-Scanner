import socket, sys
from ServPort import ServerOnPort

Ip = ""
ip = ""

def Fast_scan():
    print('Scanning of the IP : {}'.format(ip))
    try:
        for port in range(1, 100):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((Ip, port))
            if result == 0:
                ServerOnPort(port, "tcp")
            sock.close()
    except socket.gaierror:
        print('Can\'t connect to the server')
        sys.exit()
    except socket.error:
        print('Can\'t connect to the server')
        sys.exit()

