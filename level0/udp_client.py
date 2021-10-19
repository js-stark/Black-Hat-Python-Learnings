import socket

target_host=input('Enter the target host IP address')
target_port=int(input('Enter the target port'))
## Create the socket object

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

## send some data

client.sendto(b"AAABBBCCC",(target_host,target_port))

## recieve some data

data,addr = client.recvfrom(4096)

print(data.decode())
client.close()