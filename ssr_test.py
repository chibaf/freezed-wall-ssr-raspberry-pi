import RPi.GPIO as GPIO
import datetime
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
def main():
    for i in range(100):
        now = datetime.datetime.now()
        print(now)
        print(i)
        GPIO.output(14,GPIO.HIGH)
        sleep(10)
        GPIO.output(14,GPIO.LOW)
        sleep(10)
try:
    main()
except:
    pass
GPIO.cleanup()