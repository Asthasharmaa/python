#!/usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#only for receiver
s.bind(("192.168.10.192",7777))
for i in range(1000):
 print s.recvfrom(1000)
 print data
s.sendto("hmmmm",data[1])

