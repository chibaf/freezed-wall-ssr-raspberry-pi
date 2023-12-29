import matplotlib.pyplot as plt
import serial
#import sys
import time
from datetime import date
import datetime
from read_m5b_class import m5loggerb

ser = serial.Serial("/dev/ttyUSB1",19200)
sport=m5loggerb()

while True:
  array=sport.read_logger(ser)
  print(array)
