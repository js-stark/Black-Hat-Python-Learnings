import socket
from termcolor import colored

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input('enter the ip address to scan')
#port= int(input('enter the port to scan'))

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("port %d is closed"%(port),'blue'))
        pass
    else:
        print(f'port %d is open'%port)


for port in range(1,10000):
    portscanner(port)
