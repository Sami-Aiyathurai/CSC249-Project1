import socket
import sys
import asyncio

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

request = "GET /%s HTTP/1.1\r\n\r\n" %(filename)

while(True):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port)) # filename ?
    client.send(request.encode())