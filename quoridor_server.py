from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Listening for moves...')
    
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    print(message)