import socket
import os

UDP_IP = "192.168.111.101"
UDP_PORT = 5005
print ("Server Started")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))
while True:
	data,addr = sock.recvfrom(1024)
	print ("Recvd frm cleint :/n",data)

