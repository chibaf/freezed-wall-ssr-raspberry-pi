import sys
import time
import smbus
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

i2c = smbus.SMBus(1)
address = 0x5c

if __name__ == '__main__':
  try:
    while 1:
# センサsleep解除
  try:
    i2c.write_i2c_block_data(address,0x00,[])
  except:
    pass
# 読み取り命令
  time.sleep(0.003)
  i2c.write_i2c_block_data(address,0x03,[0x00,0x04])
# データ受取
  time.sleep(0.015)
  block = i2c.read_i2c_block_data(address,0,6)
  humidity = float(block[2] << 8 | block[3])/10
  temperature = float(block[4] << 8 | block[5])/10

  print('温度={0:0.1f}℃ 湿度={1:0.1f}%'.format(temperature, humidity))
  time.sleep(1) 

  if(temperature>=28):
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(26,GPIO.LOW)
  elif(temperature<28):
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(12,GPIO.LOW)

  except KeyboardInterrupt:
    sys.exit(0)