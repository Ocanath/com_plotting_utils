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
bufwidth = 100
num_lines = 10

fig, ax = plt.subplots()

x = np.arange(0, bufwidth, 1)
#line, = ax.plot([], [])

#line, = ax.plot(x, np.sin(x))
#lines.append(ax.plot(x,np.sin(x)))

#line1, = ax.plot(x,np.sin(x))
#line2, = ax.plot(x,np.sin(x))
lines = []
for i in range(0,num_lines):
    lines.append(ax.plot(x,np.sin(x)))

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

#def init():  # only required for blitting to give a clean slate.
    #for i in lines:
    #   lines[i].set_data(x,np.sin(x))
    #return line,
    

def animate(data):

    t = time.time()-start_time

    for i in range(0,num_lines):
        del xbuf[i][0]
        del ybuf[i][0]
        xbuf[i].append(t)
        ybuf[i].append(np.sin(t*2*np.pi - i/2))

    ax.relim()
    ax.autoscale_view()

    #line.set_data(xbuf[0],ybuf[0])
    for i in range(0,num_lines):
        line, = lines[i]
        line.set_data(xbuf[i],ybuf[i])
        


ani = animation.FuncAnimation(
    fig, animate, interval=2, blit=False, save_count=10)

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
