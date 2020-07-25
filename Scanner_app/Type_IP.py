import socket, sys, time
from ServPort import ServerOnPort

Ip = ""
ip = ""

def ipv4():
    print('Scanning of the Ip : {}'.format(Ip))
    try:
        t0 = time.process_time()        
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((Ip, port))
            if result == 0:
                ServerOnPort(port, "tcp")
            sock.close()
        t1 = time.process_time() - t0
        print("Finished scanning :", t1)
    except socket.gaierror:
        print('Can\'t connect to the server')
        sys.exit()
    except socket.error:
        print('Can\'t connect to the server')
        sys.exit()


def ipv6():
    print('Scanning of the Ip ...')
    try:
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
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