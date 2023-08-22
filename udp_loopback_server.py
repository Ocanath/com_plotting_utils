import numpy as np
import socket
import threading
import time
import struct 

udp_pkt = np.zeros(2)
event = threading.Event()

def recv_floatarray_pkt(soc):
	arr = np.array([])
	try:
		pkt,addr = soc.recvfrom(bufsize)

		for i in range(0,int(len(pkt)/4)):
			val = struct.unpack('<f',pkt[i*4:int(i*4+4)])
			arr = np.append(arr,val)
	except:
		pass
	return arr

def readloop(soc):
	global udp_pkt
	global event
	try:
		while(1):
			arr = recv_floatarray_pkt(server_socket)
			if(len(arr)>0 and (event.is_set() == False)):	
				udp_pkt = arr
				event.set()
			# time.sleep(1)	#socket queues up received packets
	except KeyboardInterrupt:
		pass
	
def printloop(discard):
	global udp_pkt
	global event
	try: 
		while(1):
			if(event.is_set()):
				print(udp_pkt)
				event.clear()
			time.sleep(1)
	except KeyboardInterrupt:
		pass


if __name__ == "__main__":

	udp_server_addr = ("127.0.0.1", 4537)
	bufsize = 512
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_socket.settimeout(0.0) #make non blocking
	server_socket.bind(udp_server_addr)


	t1 = threading.Thread(target=readloop, args=(server_socket,))
	t2 = threading.Thread(target=printloop, args=(0,))

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
	print("done")
	




