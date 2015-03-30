# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 8000              # The same port as used by the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
print 'Escribe la temperatura: '
pres=input()
server.sendall('---' + 'Temperatura: ' + repr(pres) + '---')
data = server.recv(1024)
server.close()
print 'Received', repr(data)
