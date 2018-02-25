import socket
import os

UDP_MASTER_IP = "192.168.111.101"
UDP_MASTER_PORT = 5010

UDP_IP = "192.168.111.100"
UDP_PORT = 5006

UDP_IP_RPI = "192.168.111.99"
UDP_PORT_RPI = 5009

print "UDP target IP:", UDP_MASTER_IP
print "UDP target port:", UDP_MASTER_PORT
print "UDP receive IP:", UDP_IP
print "UDP receive port:", UDP_PORT

sock_slave = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock_slave.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_slave.sendto("R", (UDP_IP_RPI, UDP_PORT_RPI))
print "Sent char"

sock_master = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock_master.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

filesize= int(sock.recv(1024))
print ("File Size\n",filesize)
filename = 'new.jpg'
with open(filename,'wb') as f:
		while (filesize>0):
				print ("file opened")
				data = sock.recv(1024)
				filesize -= 1024
				f.write(data)
filesize = 0
f.close()
print ("Successfully get the file")

sock_master.sendto("M", (UDP_MASTER_IP, UDP_MASTER_PORT))

st = os.stat(filename)
sock_master.sendto(str(st.st_size), (UDP_MASTER_IP, UDP_MASTER_PORT))

file_master = open(filename,'rb')
l = file_master.read(1024)
while (l):
		sock_master.sendto(l, (UDP_MASTER_IP, UDP_MASTER_PORT))
		print('Sent ',repr(l))
		l = file_master.read(1024)
file_master.close()

print('Done sending')
	
sock_master.close()
sock.close()


