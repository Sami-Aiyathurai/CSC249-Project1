import socket
import sys

#print(sys.argv)
server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_host, server_port)) # filename ?

request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % filename

client.send(request.encode())
response = client.recv(1024)
print("test")
print(response.decode())