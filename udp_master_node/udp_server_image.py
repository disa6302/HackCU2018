import socket
import os

UDP_IP = "192.168.111.101"
UDP_Port = 5005
print ("Server Started")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_Port))
with open('received_file','wb') as f:
	while True:
		print ("file opened")
		data = sock.recv(1024)
		if not data:
			break
		f.write(data)
f.close()
print ("Successfully get the file")
sock.close()
print ("Connection Close")
