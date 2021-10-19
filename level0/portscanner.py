import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='192.168.43.109'
port=445

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(f'port %d is closed'%port)
    else:
        print(f"port %d is opened"%(port))

#portscanner(port)
import sys
print(len(sys.argv))






