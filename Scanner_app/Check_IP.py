import socket

def v6_or_v4(IP):
    try:
        socket.inet_aton(IP)
        return 1
    except OSError:
        try:
            socket.inet_pton(socket.AF_INET6, IP)
            return 2
        except OSError:
            print("Unvalid IP")

