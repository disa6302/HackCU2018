import socket
import os
import struct
import re

UDP_IP = "192.168.111.101"
UDP_Port = 5010
UDP_MAC_IP = "10.203.140.225"
UDP_MAC_PORT = 5049
TCP_IP = "192.168.111.100"
TCP_Port = 5010
print ("Server Started")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#sock.connect((TCP_IP,TCP_Port))
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((UDP_IP, UDP_Port))
sock_mac = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock_mac.bind((UDP_MAC_IP,UDP_MAC_PORT))
#filesize = int(sock.recv(1024))
#print ("File Size \n",filesize)
i=0
sep = ' '
#data = sock.recv(1024)
#if data == "M":
for i in range(0,120):
	#data, = struct.unpack('<c',sock.recv(struct.calcsize('<c')))
	data = sock.recv(1024)
	try:
		if(data == "M"):
		#filesize = struct.unpack('<L',sock.recv(struct.calcsize('<L')))[0]
			filesize = int(sock.recv(1024))
			try:
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
			except:
				continue
	except:
		continue	
	#else:
	#	print data
sock.close()
print ("Connection Close")
for i in range(0,120):
	filename_app = 'u_received_file_%d.jpg'%(i,)
	st_app = os.stat(filename_app)
	sock_mac.sendto(str(st_app.st_size), (UDP_MAC_IP, UDP_MAC_PORT))

	file_master = open(filename_app,'rb')
	try:
		length = file_master.read(1024)
		while (length):
				sock_mac.sendto(length, (UDP_MAC_IP, UDP_MAC_PORT))
				#print('Sent ',repr(length))
				length = file_master.read(1024)
		file_master.close()
	except:
		continue
sock_mac.close()
 
