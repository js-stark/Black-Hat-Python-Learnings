import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host= input('enter your IP address here:')
port= int(input('enter your port to scan:'))

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(f'port %d is closed'%port)
    else:
        print(f"port %d is ope192.168ned"%(port))

portscanner(port)

 