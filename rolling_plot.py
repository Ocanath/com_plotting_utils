import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial
import getfloat

start_time = time.time()

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-2,2)
xdata, ydata = [0]*623, [0]*623

#TODO: put initialization (and other parameters) in an init function and call rolling_plot outside of this file
ser = serial.Serial('COM4', 921600, timeout = 1)


def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,

def animate(data):
    #line.set_ydata(np.sin(i/50) )  # update the data.
    t = time.time()-start_time


    del xdata[0]
    del ydata[0]
    xdata.append(t)
    
    f_arr = getfloat.get_floats(ser,2)
    print (f_arr)
    #ydata.append(f_arr[0])   #for now, only first element is plotted. add more later
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
