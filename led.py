import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23,GPIO.HIGH)
while True:
  pass
GPIO.cleanup()
