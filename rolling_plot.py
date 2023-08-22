import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial
import getfloat
import socket
import struct 

start_time = time.time()

ylower = -2
yupper = 2
bufwidth = 200
num_lines = 3

fig, ax = plt.subplots()
ax.set_ylim(ylower,yupper)

lines = []
for i in range(num_lines):
	lines.append(ax.plot([],[])[0])

xbuf = np.zeros(bufwidth)
ybuf = np.zeros((num_lines, bufwidth))
last_udp_pkt = np.zeros(128)

udp_server_addr = ("127.0.0.1", 4537)
bufsize = 512
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.settimeout(0.0) #make non blocking
server_socket.bind(udp_server_addr)


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


def animate(data):
	global xbuf
	global ybuf
	global server_socket
	global last_udp_pkt
	
	arr = recv_floatarray_pkt(server_socket)
	if(len(arr)>0):
		last_udp_pkt = arr
	
	t = time.time()-start_time
	xbuf = np.roll(xbuf,1)	#roll xbuf by 1
	xbuf[0] = last_udp_pkt[0]	#load in new value
	
	
	for i in range(0,num_lines):
		ybuf[i] = np.roll(ybuf[i],1) #roll 1
		# ybuf[i][0] = np.sin(t*2*np.pi + i)	#load new value
		ybuf[i][0] = last_udp_pkt[i+1]	#load new value

	ax.relim()
	ax.autoscale_view()

	for i, line in enumerate(lines):
		line.set_data(xbuf,ybuf[i])
   
	return lines


ani = animation.FuncAnimation(
	fig, animate, init_func=None, interval=1, blit=False, save_count=None, cache_frame_data=False,repeat=False)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()

