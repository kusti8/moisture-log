#!/usr/bin/python2
import serial
from time import sleep, strftime, time
import csv
#import matplotlib.pyplot as plt
ser = serial.Serial('/dev/ttyACM1', 9600)
sleep(2)
log = open("moisture.csv", "wt")
writer = csv.writer(log)

def get_moisture(num):
    ser.write(str(num))
    sleep(1)
    return ser.readline().strip()

def write(moistures):
    writer.writerow( (strftime("%Y-%m-%d %H:%M:%S"), moistures[0], moistures[1], moistures[2], moistures[3], moistures[4]) )

while True:
    ms = []
    for i in range(5):
        ms.append(get_moisture(i))
    write(ms)
    print "Done with one"
    sleep(5)
