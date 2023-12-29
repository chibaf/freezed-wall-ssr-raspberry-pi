import matplotlib.pyplot as plt
import serial
import sys
import time
from datetime import date
from read_m5_class import m5logger
from read_m5b_class import m5loggerb

data0=[0]*20
data=[data0]*100

#ser1 = serial.Serial("/dev/ttyUSB0",115200)
#ser2 = serial.Serial("/dev/ttyUSB1",19200)
ser1 = serial.Serial(sys.argv[1],sys.argv[2])
#ser2 = serial.Serial("/dev/tty.usbserial-0201C4A4",19200)
sport1=m5logger()
#sport2=m5loggerb()

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn=str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")

start = time.time()
while True:
  ttime=time.time()-start
  if ttime<0.001:
    ttime=0.0
  try:
    array1=sport1.read_logger(ser1)
#    array2=sport2.read_logger(ser2)
    array=array1 #+array2
    if len(array)==10:
      data.pop(-1)
      data.insert(0,array)
      rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
      x=range(0, 100, 1)
      plt.clf()
      plt.ylim(-10,100)
      line1,=plt.plot(x,rez[0],label="L1")
      line2,=plt.plot(x,rez[1],label="L2")
      line3,=plt.plot(x,rez[2],label="L3")
      line4,=plt.plot(x,rez[3],label="L4")
      line5,=plt.plot(x,rez[4],label="L5")
      line6,=plt.plot(x,rez[5],label="L6")
      line7,=plt.plot(x,rez[6],label="L7")
      line8,=plt.plot(x,rez[7],label="L8")
      line9,=plt.plot(x,rez[8],label="L9")
      line10,=plt.plot(x,rez[9],label="L10")
#      line11,=plt.plot(x,rez[10],label="L11")
#      line12,=plt.plot(x,rez[11],label="L12")
#      line13,=plt.plot(x,rez[12],label="L13")
#      line14,=plt.plot(x,rez[13],label="L14")
#      line15,=plt.plot(x,rez[14],label="L15")
#      line16,=plt.plot(x,rez[15],label="L16")
#      line17,=plt.plot(x,rez[16],label="L17")
#      line18,=plt.plot(x,rez[17],label="L18")
#      line19,=plt.plot(x,rez[18],label="L19")
#      line20,=plt.plot(x,rez[19],label="L20")
      plt.legend(handles=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]) #,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20])
      plt.pause(0.1)
      if len(array)==10:
        st=time.strftime("%Y %b %d %H:%M:%S", time.localtime())
        ss=str(time.time()-int(time.time()))
        rttime=round(ttime,2)
        strg=str(st+ss[1:5])+","+str(rttime)+","+str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+","+str(array[8])+","+str(array[9])
         #+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+","+str(array[8])+","+str(array[9])+","+str(array[10])+","+str(array[11])+","+str(array[12])+","+str(array[13])+","+str(array[14])+","+str(array[15])+","+str(array[16])+","+str(array[17])+","+str(array[18])+","+str(array[19])
        f.write(strg+"\n")
        print(strg)
      else:
        f.write(str(array)+"\n")
  except KeyboardInterrupt:
    print ('exiting')
    f.close()
    break
ser1.close()
f.close()
exit()
