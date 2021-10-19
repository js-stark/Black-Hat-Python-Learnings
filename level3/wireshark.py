import socket
from struct import *

def eth_addr(a,mac):
    print(f" %s (%.2x:%.2x:%.2x:%.2x:%.2x:%.2x)" %(mac,a[0], a[1], a[2], a[3], a[4], a[5]))
    

try:
    s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0003))

except Exception as e:
    print("Error on creating Socket object....: ",e)
    exit(0)

while True:
    packet = s.recvfrom(65535)
    packet = packet[0]
    eth_length = 14
    eth_header =packet[:eth_length]

    eth = unpack('6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])

    eth_addr(packet[6:12],"SOURCE     :")
    eth_addr(packet[0:6],"DESTINATION:")
    print(' PROTOCOL   : ',str(eth_protocol))
    print("_________________________________________")





