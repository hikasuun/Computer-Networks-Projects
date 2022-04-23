#UDPPingerClient.py
from socket import *
import time

#create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#server socket
serverName = '127.0.0.1'
serverPort = 12000

# client sends 10 pings to the server
for x in range(10):
    #send ping and wait up to 1 sec for response
    try:
        # time of sent ping from epoch
        sentTime = time.time()
        message = 'Ping ' + str(x+1) + ': ' + str(sentTime)

        clientSocket.sendto(message.encode(), (serverName,serverPort))
        # set timeout to 1 sec
        clientSocket.settimeout(1)

        serverMessage, serverAddress = clientSocket.recvfrom(1024)
        # time of reception of ping from epoch
        receivedTime = time.time()

        print(serverMessage.decode())
        print('       RTT: ' + str(receivedTime - sentTime) + '\n')
    # if timeout elapses, print error msg
    except:
        print('Request timed out\n')

#close socket
clientSocket.close()
