# rpi_cam.py

import socket
import os
import time
import numpy as np
import cv2
import picamera 
from pylepton import Lepton

UDP_IP = "192.168.111.100"
UDP_PORT = 5006
UDP_IP_RPI = "192.168.111.99"
UDP_PORT_RPI = 5009
#print "UDP target IP:", UDP_IP
#print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((UDP_IP_RPI,UDP_PORT_RPI))
print "UDP RPI Waiting"
c = sock.recv(1024)
print c
sock_slave = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_slave.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#sock_slave.bind((UDP_IP,UDP_PORT)) 
print 'Server listening....'
#i = 100
#while i>0:
#	i-=1
#data = sock.recv(1024)
#c = "Ack"
if c == "R":
#	print 'Got R!!!!!!'
	for i in range (0,120):
		#sock_slave.sendto(c, (UDP_IP, UDP_PORT))
		#os.system("raspistill -w 640 -h 480 -q 8 -o ~/HackCU2018/rpi_slave_cam/name1.jpg")
	#	filename='/home/pi/HackCU2018/rpi_slave_cam/name1.jpg'
		with Lepton("/dev/spidev0.1") as l:
			a,_ = l.capture()
			cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX) # extend contrast
			np.right_shift(a, 8, a) # fit data into 8 bits
			cv2.imwrite("/home/pi/HackCU2018/name1.jpg", np.uint8(a)) # write it!
		filename='/home/pi/HackCU2018/name1.jpg'
		#filename='/home/pi/HackCU2018/udp_slave_node/sri.jpg'
		st = os.stat(filename)
		sock_slave.sendto(str(st.st_size), (UDP_IP, UDP_PORT))
		f = open(filename,'rb')
		l = f.read(1024)
		while (l):
			sock_slave.sendto(l, (UDP_IP, UDP_PORT))
#    			print('Sent ',repr(l))
    			l = f.read(1024)
		print ("\n Image Sent ",i)
		f.close()
#os.system("raspistill -w 640 -h 480 -q 8 -o ~/HackCU2018/rpi_slave_cam/name1.jpg")
#with picamera.PiCamera() as camera:
#	camera.resolution = (640,480)
#	time.sleep(0.5)
#	camera.capture("/home/pi/HackCU2018/rpi_slave_cam/name1.jpg")
#filename='/home/pi/HackCU2018/rpi_slave_cam/name1.jpg'
#st = os.stat(filename)
#sock_slave.sendto(str(st.st_size), (UDP_IP, UDP_PORT))
#f = open(filename,'rb')
#l = f.read(1024)
#while (l):
#	sock_slave.sendto(l, (UDP_IP, UDP_PORT))
#       #print('Sent ',repr(l))
#	#print ("\n Image Sent 31 ")
#        l = f.read(1024)
#print ("\n Image Sent 31 ")
#f.close()

print('Done sending')
sock_slave.close()
sock.close()
