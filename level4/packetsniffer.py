import socket
import os
import sys
import struct
import binascii

sock_created = False
sniffer_socket = 0

def analyze_udp_header(data_recv):
    udp_hdr = struct.unpack('!4H',data_recv[0:8])
    src_port = udp_hdr[0]
    dst_port = udp_hdr[1]
    length = udp_hdr[2]
    checksum = udp_hdr[3]
    data = data_recv[8:]

    print("_____________UDP HEADER_____________")
    print(f"SOURCE: %hu"% src_port)
    print(f"DESTINATION: %hu"% dst_port)
    print(f"LENGTH: %hu"% length)
    print(f"CHECKSUM: %hu"% checksum)

    return data

def analyze_tcp_header(data_recv):
    tcp_hdr = struct.unpack('!2H2I4H',data_recv[:20])
    src_port = tcp_hdr[0]
    dst_port = tcp_hdr[1]
    seq_num = tcp_hdr[2]
    ack_num = tcp_hdr[3]
    data_offset = tcp_hdr[4] >> 12
    reserved = (tcp_hdr[5] >> 6) & 0x03ff
    flags = tcp_hdr[4] & 0x003f
    window = tcp_hdr[5]
    checksum = tcp_hdr[6]
    urg_ptr = tcp_hdr[7]
    data = data_recv[20:]

    # Flags
    urg = bool(flags & 0x0020)
    ack = bool(flags & 0x0010)
    psh = bool(flags & 0x0008)
    rst = bool(flags & 0x0004)
    syn = bool(flags & 0x0002)
    fin = bool(flags & 0x0001)

    print("_____________TCP HEADER_____________")

    print(f"SOURCE: %hu"% src_port)
    print(f"DESTINATION PORT: %hu"% dst_port)
    print(f"SEQ: %u"% seq_num)
    print(f"ACK: %u"% ack_num)
    print(f"FLAGS ##:")
    print(f"URG: %d"% urg)
    print(f"ACK: %d"% ack)
    print(f"PSH: %d"% psh)
    print(f"RST: %d"% rst)
    print(f"SYN: %d"% syn)
    print(f"FIN: %d"% fin)
    print(f"WINSIZE: %hu"% window)
    print(f"CHECKSUM: %hu"% checksum)

    return data

def analyze_ip_header(data_recv):
    ip_hdr = struct.unpack('6H4s4s',data_recv[:20])
    ver = ip_hdr[0] >> 12
    ihl = (ip_hdr[0] >> 8) & 0x0f
    tos = ip_hdr[0] & 0x00ff
    tot_len = ip_hdr[1]
    ip_id = ip_hdr[2]
    flags = ip_hdr[3] >> 13
    frag_offset = ip_hdr[3] & 0x1fff
    ip_ttl = ip_hdr[4] >> 8
    ip_proto = ip_hdr[4] & 0x00ff
    checksum = ip_hdr[5]
    src_address = socket.inet_ntoa(ip_hdr[6])
    dst_address = socket.inet_ntoa(ip_hdr[7])
    data = data_recv[20:]

    print("_____________IP HEADER_____________")
    print(f"Version: %hu"% (ver))
    print(f"IHL: %hu"% (ihl))
    print(f"TOS: %hu"% (tos))
    print(f"LENGTH: %hu"% (tot_len))
    print(f"ID: %hu"% (ip_id))
    print(f"OFFSET: %hu"% (frag_offset))
    print(f"TTL: %hu"% (ip_ttl))
    print(f"PROTO: %hu"% (ip_proto))
    print(f"CHECKSUM: %hu"% (checksum))
    print(f"SOURCE IP: %s"%(src_address))
    print(f"DESTINATION IP: %s"% (dst_address))

    # if ip_proto == 6:
    #     tcp_udp = "TCP"
    # elif ip_proto == 17:
    #     tcp_udp = "UDP"
    # else:
    #     tcp_udp = "OTHER"
    return data#,tcp_udp
    


def analyzer_ether_header(data_recv):
    ip_bool = False

    eth_hdr = struct.unpack('6s6sH',data_recv[:14])
    dest_mac = binascii.hexlify(eth_hdr[0]).decode('utf-8')
    src_mac = binascii.hexlify(eth_hdr[1]).decode('utf-8')
    proto = (eth_hdr[2] >> 8)
    data = data_recv[14:]

    print("_____________ETHERNET HEADER_____________")
    print(f"Destination mac: %s:%s:%s:%s:%s:%s"% (dest_mac[0:2],dest_mac[2:4],dest_mac[4:6],dest_mac[6:8],dest_mac[8:10],dest_mac[10:12]))
    print(f"Destination mac: %s:%s:%s:%s:%s:%s"% (src_mac[0:2],src_mac[2:4],src_mac[4:6],src_mac[6:8],src_mac[8:10],src_mac[10:12]))
    print(f"Protocol : %hu" % proto)

    if proto == int(proto):
        ip_bool = True
    print(ip_bool)
    return data, ip_bool

def main():

    global sock_created
    global sniffer_socket

    if sock_created ==False:
        sniffer_socket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
        sock_created = True

    data_recv = sniffer_socket.recv(2048)
    os.system('clear')
    data_recv,ip_bool = analyzer_ether_header(data_recv)

    if ip_bool:
        data_recv =analyze_ip_header(data_recv) # data_recv,tcp_udp = 
    else: 
        return
    try:
        data_recv = analyze_tcp_header(data_recv)
        data_recv = analyze_udp_header(data_recv)
    except:
        return

    # if tcp_udp == "TCP":
    #     data_recv = analyze_tcp_header(data_recv)
    # elif tcp_udp == "UDP":
    #     data_recv = analyze_udp_header(data_recv)
    # else:
    #      return


while True:
    main()






