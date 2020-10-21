import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
try:
    while True:
        for i in range(9, 12):
            GPIO.output(i, GPIO.HIGH)
            sleep(1)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()
