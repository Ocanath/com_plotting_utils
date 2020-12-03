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

x = np.arange(0, bufwidth, 1)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(ylower,yupper)
xdata, ydata = [0]*bufwidth, [0]*bufwidth

#TODO: put initialization (and other parameters) in an init function and call rolling_plot outside of this file

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,

def animate(data):
    #line.set_ydata(np.sin(i/50) )  # update the data.
    #t = data
    t = time.time()-start_time
    del xdata[0]
    del ydata[0]
    
    xdata.append(t)
    ydata.append(np.sin(t*2*np.pi))
    
    ax.relim()
    ax.autoscale_view()
    
    line.set_data(xdata,ydata)
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
