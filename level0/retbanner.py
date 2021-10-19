import socket
import codecs

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return 

def main():
    ip = input('enter the ip to scan')
    for x in range(1,100):
        banner = retBanner(ip,x)
        if banner:
            print(ip,"is open the port",x,'and with banner:',banner)


main() 









