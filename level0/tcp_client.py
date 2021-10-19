import socket

target_host=input('Enter the target server IP address')
target_port=int(input('Enter the target server port'))
#socket.setdefaulttimeout(2)

# Creating the socket object

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connecting the client

client.connect((target_host,target_port))

# Send some data

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# recieve some data

response = client.recv(4096)

print(response.decode())
client.close()





