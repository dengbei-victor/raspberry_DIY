import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # 设置模式
GPIO.setup(23,GPIO.OUT) # 输出 trig
GPIO.setup(24,GPIO.IN)  # 输入 echo
GPIO.setup(13,GPIO.OUT) 
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)



while True:
     pulse_start = 0
     pulse_stop = 0
     duration = 0
     distance = 0

     GPIO.output(23,GPIO.LOW)
     time.sleep(0.1) 
     GPIO.output(23,GPIO.HIGH)
     time.sleep(0.000010)
     GPIO.output(23,GPIO.LOW)

     while GPIO.input(24)==0:
         pulse_start = time.time()

     while GPIO.input(24)==1:
         pulse_stop = time.time()

     duration = pulse_stop - pulse_start # 接收的脉冲时间

     distance = duration*17150.0    # 34300=Distance/Time
     distance = round(distance,2)   
     if(distance < 10):
         GPIO.output(13,GPIO.HIGH)
         GPIO.output(19,GPIO.LOW)
         GPIO.output(26,GPIO.LOW)
     elif(distance < 20):
         GPIO.output(13,GPIO.LOW)
         GPIO.output(19,GPIO.HIGH)
         GPIO.output(26,GPIO.LOW) 
     elif(distance < 30):
         GPIO.output(13,GPIO.LOW)
         GPIO.output(19,GPIO.LOW)
         GPIO.output(26,GPIO.HIGH)
     else:
         GPIO.output(13,GPIO.LOW)
         GPIO.output(19,GPIO.LOW)
         GPIO.output(26,GPIO.LOW)     
     print ("distance " + str(distance)) 

     time.sleep(0.2)
