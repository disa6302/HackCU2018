# server.py

import socket
import os

UDP_IP = "192.168.111.101"
UDP_PORT = 5005

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

print 'Server listening....'

filename='/home/devuser/hackcu/HackCU2018/udp_slave_node/sri.jpg'
st = os.stat(filename)

for i in range (0,3):
	sock.sendto(str(st.st_size), (UDP_IP, UDP_PORT))

	f = open(filename,'rb')
	l = f.read(1024)
	while (l):
		sock.sendto(l, (UDP_IP, UDP_PORT))
    		print('Sent ',repr(l))
    		l = f.read(1024)
	f.close()

print('Done sending')
sock.close()
