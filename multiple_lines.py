import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial
import getfloat

start_time = time.time()

port = 'COM4'
baud = 921600
timeout = 1
ylower = -2
yupper = 2
bufwidth = 500
num_lines = 2

fig, ax = plt.subplots()

x = np.arange(0, bufwidth, 0.01)
#line, = ax.plot([], [])
line, = ax.plot(x, np.sin(x))
#lines = []
#lines.append(ax.plot(x,np.sin(x)))
#for i in range(0,num_lines):
#	lobj = ax.plot(x,np.sin(x))
#	lines.append(lobj)

ax.set_ylim(ylower,yupper)

xbuf = []
ybuf = []
for i in range(0,num_lines):
	xbuf.append([])
	ybuf.append([])
for i in range(0, num_lines):
	for j in range(0,bufwidth):
		xbuf[i].append(0)
		ybuf[i].append(0)

def init():  # only required for blitting to give a clean slate.
	#for i in lines:
	#	lines[i].set_data(x,np.sin(x))
	return line,

def animate(data):
	t = time.time()-start_time

	del xbuf[0][0]
	del ybuf[0][0]
	xbuf[0].append(t)
	ybuf[0].append(np.sin(t*2*np.pi))

	del xbuf[1][0]
	del ybuf[1][0]
	xbuf[1].append(t)
	ybuf[1].append(np.sin(t*2*np.pi - 1.2))

	ax.relim()
	ax.autoscale_view()

	line.set_data(xbuf[0],ybuf[0])
	#for i in range(0,num_lines):
	#	lines[i].set_data(xbuf[lnum],ybuf[lnum])
	#lines[0].set_data(xbuf[0],ybuf[0])
	
	return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)

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
    
ser.close()
