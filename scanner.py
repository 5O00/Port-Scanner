import socket, sys, time, threading, optparse
from Check_IP import v6_or_v4
from Type_Scan import Fast_scan
from ServPort import ServerOnPort
from Type_IP import ipv4, ipv6



parser = optparse.OptionParser()
parser.add_option('-i', '--ip', action="store", dest="Ip", help="Ip adress to scan")
options, args = parser.parse_args()
Ip = options.Ip

type_ip=v6_or_v4(Ip)
if type_ip == 1:
    #On affiche le type juste pour voir si ça marche
    print("IPV4")
    ipv4()
elif type_ip == 2:
    #Pareil ici
    print("IPV6")
    ipv6()