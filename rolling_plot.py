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
num_lines = 10

ser = serial.Serial('COM4', 921600, timeout = 1)    #set up serial port

fig, ax = plt.subplots()
ax.set_ylim(ylower,yupper)

lines = []
for i in range(num_lines):
    lines.append(ax.plot([],[])[0])

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
    for line in lines:
       line.set_data([],[])
    return lines


def animate(data):

    t = time.time()-start_time
    
    f_arr = getfloat.get_floats(ser,num_lines)
    #print(f_arr) #optional print to console of the floating data we got
    
    for i in range(0,num_lines):
        del xbuf[i][0]
        del ybuf[i][0]
        xbuf[i].append(t)
        ybuf[i].append(float(*f_arr[0]))

    ax.relim()
    ax.autoscale_view()

    for i, line in enumerate(lines):
        line.set_data(xbuf[i],ybuf[i])
    
    return lines


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
