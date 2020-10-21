# Passive Infrared 红外被动   passive 被动
import time 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN) 
GPIO.setup(23,GPIO.OUT)
try:
    while True:
        if GPIO.input(24) == 1: 
            GPIO.output(23,GPIO.HIGH)
        else: 
            GPIO.output(23,GPIO.LOW)
       # print(GPIO.input(24))
    time.sleep(1)
finally:
    GPIO.cleanup()
