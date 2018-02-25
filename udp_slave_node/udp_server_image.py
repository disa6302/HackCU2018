import socket
import os

UDP_IP = "192.168.111.100"
UDP_Port = 5005
print ("Server Started")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_Port))
#filesize = int(sock.recv(1024))
#print ("File Size \n",filesize)
#i=0
for i in range(3):
	filesize= int(sock.recv(1024))
	print ("File Size\n",filesize)
	filename = 'received_file_%d.jpg'%(i,)
	with open(filename,'wb') as f:
		while (filesize>0):
			print ("file opened")
			data = sock.recv(1024)
			filesize -= 1024
			#if not data:
			#	break
			f.write(data)
	filesize = 0
	f.close()
	print ("Successfully get the file")
sock.close()
print ("Connection Close")
