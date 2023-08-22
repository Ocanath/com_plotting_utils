import socket
import time
import struct 
import numpy as np

udp_server_addr = ("127.0.0.1", 4537)
bufsize = 512
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(0.0) #make non blocking


try:
	
	start_time = time.time()
	while(1):
		t = time.time()-start_time
		arr = [t, np.sin(t*2*np.pi/4+1),np.sin(t*2*np.pi/4+2), np.sin(t*2*np.pi/4+3) ]
		
		barr = []
		for i in range(0,len(arr)):
			b4 = struct.pack('<f',arr[i])
			for b in b4:
				barr.append(b)
		barr=bytearray(barr)
		client_socket.sendto(barr,udp_server_addr)
		# client_socket.sendto(struct.pack('<f',t), udp_server_addr)
		
		
		uparr = []
		for i in range(0,int(len(barr)/4)):
			val = struct.unpack('<f',barr[i*4:int(i*4+4)])
			uparr.append(val)
		print(uparr)
		
		time.sleep(0.02)
		
		
		
		
except KeyboardInterrupt:
	pass
