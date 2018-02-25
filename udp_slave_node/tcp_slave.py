import socket
import time
import os
import sys
import struct


TCP_MASTER_IP = "192.168.111.100"
TCP_MASTER_PORT = 5010

UDP_IP = "192.168.111.100"
UDP_PORT = 5006

UDP_IP_RPI = "192.168.111.99"
UDP_PORT_RPI = 5009


sock_master = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # UDP
sock_master.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_master.bind((TCP_MASTER_IP, TCP_MASTER_PORT))
sock_master.listen(1)
connection,addr = sock_master.accept()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

sock_slave = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock_slave.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

for i in range (0,5):
	sock_slave.sendto("R", (UDP_IP_RPI, UDP_PORT_RPI))
	print "Sent char"


	filesize= int(sock.recv(1024))
	print ("File Size\n",filesize)
	filename = 'new.jpg'
	with open(filename,'wb') as f:
			while (filesize>0):
					data = sock.recv(1024)
					filesize -= 1024
					f.write(data)
	filesize = 0
	f.close()	
	print ("Successfully get the file")
	
	#character = "M"
	#connection.send(character.encode())

	st = os.stat(filename)
	size = st.st_size
	#sep = ' '
	#val = str(size) + sep # sep = ' ' or sep = `\n`
	#print val
	connection.send(str(size))
	print "sent size"
	c = connection.recv(1024)
	print "recv ack"
	#print (struct.pack('<L', size))
	#connection.send(struct.pack('<L', size))
	#connection.flush()
	time.sleep(0.005)
	file_master = open(filename,'rb')
	l = file_master.read(1024)
	while (l):
			connection.send(l)
			#print('Sent',repr(l))
			l = file_master.read(1024)
	file_master.close()
	print("Sent image\n",i)

print('Done sending')
	
connection.close()
sock.close()


