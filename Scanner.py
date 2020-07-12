import socket
import sys
import time 
import threading
import argparse


def ServerOnPort(Number_Port, Protocol):
    ServiceName = socket.getservbyport(Number_Port, Protocol)
    print("[+] port number %d : %s"%(Number_Port, ServiceName))


def ipv4():
    Ip = input('Enter the Ip : ')
    print('Scanning of the Ip ...')
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
    Ip = input('Enter the Ip : ')
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


buffer = False
while buffer == False:
    type_ip = int(input("Choose a type of IP : \n" +"1. IPV4\n" + "2. IPV6\n"))
    if type_ip == 1 or type_ip == 2:
        buffer = True


if type_ip == 1:
    ipv4()
elif type_ip == 2:
    ipv6()