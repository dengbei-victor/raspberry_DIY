import RPi.GPIO as GPIO
import time                             
GPIO.setmode(GPIO.BCM)       
GPIO.setup(18,GPIO.OUT)         

pwm= GPIO.PWM(18,5) # 第二个参数是频率  每秒闪烁5次
duty_cycle = 50  #占空比 单位时间内高电平的比例
pwm.start(duty_cycle)

time.sleep(10)

GPIO.cleanup()

# pwm= GPIO.PWM(18,1)
# duty_cycle = 50
#每个脉冲的时间/宽度为1秒
#开启的时间百分比为50％
#它关闭的时间百分比是50％
#开启时间为0.5秒
#关机时间为0.5秒
