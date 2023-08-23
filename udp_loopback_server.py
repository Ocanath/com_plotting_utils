import numpy as np
import socket
import threading
import time
import struct 

udp_pkt = np.zeros(2)
udp_rdy_evt = threading.Event()
kill_sig = threading.Event()

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
	global udp_rdy_evt
	global kill_sig
	
	while(kill_sig.is_set()):
		arr = recv_floatarray_pkt(server_socket)
		if(len(arr)>0 and (udp_rdy_evt.is_set() == False)):	
			udp_pkt = arr
			udp_rdy_evt.set()

	
def printloop(discard):
	global udp_pkt
	global udp_rdy_evt
	global kill_sig
	
	while(kill_sig.is_set()):
		if(udp_rdy_evt.is_set()):
			print(udp_pkt)
			udp_rdy_evt.clear()
		# time.sleep(1)

def kill_thread():
	global kill_sig
	kill_sig.set()
	input()
	kill_sig.clear()
	
if __name__ == "__main__":

	udp_server_addr = ("127.0.0.1", 4537)
	bufsize = 512
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_socket.settimeout(0.0) #make non blocking
	server_socket.bind(udp_server_addr)

	t0 = threading.Thread(target=kill_thread)
	t1 = threading.Thread(target=readloop, args=(server_socket,))
	t2 = threading.Thread(target=printloop, args=(0,))

	t0.start()
	t1.start()
	t2.start()
	   
	t0.join()
	t1.join()
	t2.join()
	
	print("done")
	




