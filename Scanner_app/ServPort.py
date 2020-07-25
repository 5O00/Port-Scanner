import socket

def ServerOnPort(Number_Port, Protocol):
    ServiceName = socket.getservbyport(Number_Port, Protocol)
    print("[+] port number %d : %s"%(Number_Port, ServiceName))