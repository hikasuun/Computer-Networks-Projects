#SMTPClient.py
from http import client
from pydoc import cli
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'gmail-smtp-in.l.google.com' # doesnt require authentication however may be flagged as spam / phishing
mailport = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,mailport))

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'

clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = "MAIL FROM:<test@mail.com>\r\n"
clientSocket.send(mailFromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('mail from 250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = "RCPT TO:<schaar.clint@gmail.com>\r\n"
clientSocket.send(rcptToCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('RCPT TO 250 reply not received')

# Send DATA command and print server response.
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('Data 250 not received')

# Send message data.
messageFrom = "From: <test@mail.com>\r\n"
messageTo = "To: <schaar.clint@gmail.com>\r\n"
messageSubject = "Subject: Test Message\r\n"

# Message ends with a single period.
clientSocket.send(messageFrom.encode())
clientSocket.send(messageTo.encode())
clientSocket.send(messageSubject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('MSG 250 not received')

# Send QUIT command and get server response.
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('End 250 not received')