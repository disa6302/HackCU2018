import socket
import os

UDP_IP = "10.203.140.225"
UDP_Port = 5049
print ("Server Started")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((UDP_IP, UDP_Port))
#filesize = int(sock.recv(1024))
#print ("File Size \n",filesize)
i=0
#data = sock.recv(1024)
#if data == "M":
for i in range(0,120):
	filesize= int(sock.recv(1024))
	print ("File Size\n",filesize)
	filename = '/Users/abhi/Downloads/hackcu/Photo-Gallery/static/video/u_received_file_%d.jpg'%(i,)
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
