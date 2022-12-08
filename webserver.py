from socket import *
import sys # In order to terminate the program
from threading import *

class MyThread(Thread):
    def __init__(self, address, socket):
        Thread.__init__(self)
        self.connectionSocket = socket
        #self.addr = address
        print("__init__()")

    def run(self):
        print("run()")
        message = ""
        #while True:
        try:
            message = self.connectionSocket.recv(1024).decode()
            print(message)
            filename = message.split()[1]
            print("filename = ")
            print(filename)
            f = open(filename[1:])
            outputdata = f.read()
            self.connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            for i in range(0, len(outputdata)):
                self.connectionSocket.send(outputdata[i].encode())
            self.connectionSocket.send("\r\n".encode())
            self.connectionSocket.close()
        except IOError:
            self.connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n".encode())
            self.connectionSocket.close()



serverSocket = socket(AF_INET, SOCK_STREAM)

# -------------
# Fill in start
# -------------

  # TODO: Assign a port number
  #       Bind the socket to server address and server port
  #       Tell the socket to listen to at most 1 connection at a time
#Client needs to be its own object (make a class for client connections?)

PORT = 5050
# SERVER = gethostbyname(gethostbyname())
# ADDRESS = (SERVER,PORT)

serverSocket.bind(('', PORT))
print('Ready to serve...') 
# -----------
# Fill in end
# -----------
threads = []
serverSocket.listen(1)

while True:
    
    # Establish the connection
    print("testing webserver.py...")
    # print(serverSocket)
    # -------------
    # Fill in start
    # -------------
    conSocket, addr = serverSocket.accept() # TODO: Set up a new connection from the client
    print("accepted connection...")
    # -----------
    # Fill in end
    # -----------

    new_thread = MyThread(addr, conSocket)
    new_thread.start()
    threads.append(new_thread)

serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data