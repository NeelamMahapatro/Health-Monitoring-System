#!/usr/bin/python

import serial

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)
ser1 =serial.Serial('/dev/ttyACM1', 115200, 8, 'N', 1, timeout=5)

while True:
    data = ser.readline()
    time.sleep(1)

