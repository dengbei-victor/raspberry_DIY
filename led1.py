import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
while True:
    for i in range(3):
        GPIO.output(23, GPIO.HIGH)
        sleep(.5)
        GPIO.output(23, GPIO.LOW)
        sleep(.5)
    sleep(1)
GPIO.cleanup()
