# server.py

import socket

UDP_IP = "192.168.111.101"
UDP_PORT = 5005

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

print 'Server listening....'

filename='/data/pastaveg_640x480.jpg'
f = open(filename,'rb')
l = f.read(1024)
while (l):
    sock.sendto(l, (UDP_IP, UDP_PORT))
    print('Sent ',repr(l))
    l = f.read(1024)
f.close()

print('Done sending')
sock.close()
