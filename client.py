import socket
import sys

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_host, server_port)) # filename ?

request = "GET /%s HTTP/1.1\r\n\r\n" %(filename)

client.send(request.encode())

response = client.recv(1024)
while(response):
    print(response.decode())
    response = client.recv(1024)