#!/usr/bin/python
import serial
import getfloat

ser = serial.Serial('COM4', 921600, timeout = 1)
print(ser.name)

xdat = [0]*500

count = 0
while (count < 500):
    f_arr = getfloat.get_floats(ser,2)
    print(f_arr)
    del xdat[0]
    xdat.append(f_arr[0])
    count = count + 1
    
ser.close()

print ("fuck off")