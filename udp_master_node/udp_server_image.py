import socket
import os
import struct
import re

UDP_IP = "192.168.111.101"
UDP_Port = 5010
TCP_IP = "192.168.111.100"
TCP_Port = 5010
print ("Server Started")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#sock.connect((TCP_IP,TCP_Port))
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((UDP_IP, UDP_Port))
#filesize = int(sock.recv(1024))
#print ("File Size \n",filesize)
i=0
sep = ' '
#data = sock.recv(1024)
#if data == "M":
for i in range(0,60):
	#data, = struct.unpack('<c',sock.recv(struct.calcsize('<c')))
	data = sock.recv(1024)
	if(data == "M"):
	#buf = ''
        #while sep not in buf:
	#	buf += sock.recv(1)
	#print buf
	#re.split('\s+',buf)
	
	#filesize = struct.unpack('<L',sock.recv(struct.calcsize('<L')))[0]
		filesize = int(sock.recv(1024))
	#ack = 'ack'
	#sock.send(ack)
		print ("File Size ",filesize)
		print ("File Number \n",i)
		filename = 'u_received_file_%d.jpg'%(i,)
		print filename
		with open(filename,'wb') as f:
			while (filesize>0):
			#print ("file opened")
				datab = sock.recv(1024)
				filesize -= 1024
			#if not data:
			#	break
				f.write(datab)
		filesize = 0
		f.close()
		print ("Successfully get the file")
	#else:
	#	print data
sock.close()
print ("Connection Close")
