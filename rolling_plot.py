import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial
import getfloat

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

def animate(data):
	global xbuf
	global ybuf

	t = time.time()-start_time
	xbuf = np.roll(xbuf,1)	#roll xbuf by 1
	xbuf[0] = t	#load in new value
			
	for i in range(0,num_lines):
		ybuf[i] = np.roll(ybuf[i],1) #roll 1
		ybuf[i][0] = np.sin(t*2*np.pi + i)	#load new value

		
	ax.relim()
	ax.autoscale_view()

	for i, line in enumerate(lines):
		line.set_data(xbuf,ybuf[i])
   
	return lines


ani = animation.FuncAnimation(
	fig, animate, init_func=None, interval=1, blit=False, save_count=None)

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

