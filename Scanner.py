import socket
import sys

Ip = input('Enter the Ip : ')
print('Scanning of the Ip ...')
try:
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((Ip, port))
        if result == 0:
            print('+ Port '+ port + ' open')
        sock.close()
except socket.gaierror:
    print('Can\'t connect to the server')
    sys.exit()
except socket.error:
    print('Can\'t connect to the server')
    sys.exit()

print('Scan finish')