import numpy as np
import socket
import threading
import time
import struct 

udp_server_addr = ("127.0.0.1", 4537)
bufsize = 512
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.settimeout(0.0) #make non blocking
server_socket.bind(udp_server_addr)

try:
	while(1):
		try:
			pkt,addr = server_socket.recvfrom(bufsize)
			arr = []
			for i in range(0,int(len(pkt)/4)):
				val = struct.unpack('<f',pkt[i*4:int(i*4+4)])
				arr.append(val)
			print(arr)
		except:
			pass
		# time.sleep(1)	#socket queues up received packets
except KeyboardInterrupt:
	pass

