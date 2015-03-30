#!/usr/bin/env python 
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import select 
import socket 
import time
import sys
 

host = '' 
host1 = ''
port = 8000
port1 = 8080
backlog = 5 
size = 1024 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host,port)) 
server.listen(backlog)
webserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
webserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

input = [webserver] 

running = 1 
while running:
	inputready,outputready,exceptready = select.select(input,[],[]) 
	for s in inputready:
		if s == webserver: 
		# Manejo del webserver socket 
#-----------------------------------------------------------------
			class myHandler(BaseHTTPRequestHandler):
					
				def do_GET(self):
						#Revisa la pagina HTML almacenada
					self.path="/index.html"
					mimetype='text/html'
					sendReply = True
#------------------------------------------------------------------------		
					client, address = server.accept()
					input.append(client)
					data = client.recv(size)
					print 'Datos:', data
					client.close()
#------------------------------------------------------------------------		
					client, address = server.accept()
					input.append(client)
					data1 = client.recv(size)
					print 'Datos:', data1
					client.close()
#------------------------------------------------------------------------
					client, address = server.accept()
					input.append(client)
					data2 = client.recv(size)
					print 'Datos:', data2
					client.close()
#------------------------------------------------------------------------
						#Abre el archivo html y lo envia
					f = open(curdir + sep + self.path) 
					self.send_response(200)
					self.send_header('Tipo de contenido',mimetype)
					self.end_headers()
					self.wfile.write(f.read())
					self.wfile.write(data)
					self.wfile.write(data1)
					self.wfile.write(data2)
					f.close()
					return
			try:
				#Crea el web server
				webserver = HTTPServer((host, port1), myHandler)
				print 'Inicio en el puerto ' , port1
				#Espera a futuras solicitudes
				webserver.serve_forever()
				webserver.socket.close()
				webserver.close()

			except KeyboardInterrupt:
				print '^C Recibido, Gracias por usar este servicio'
				webserver.socket.close()

#-----------------------------------------------------------------
		else:  
			input.remove(s) 
server.close()
webserver.close()
