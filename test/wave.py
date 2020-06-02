import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

TRIG=10
ECHO=8

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,True)#发送Trig信号，持续0.0001s
time.sleep(0.0001)
GPIO.output(TRIG,False)

#等待低电平结束
while GPIO.input(ECHO)==0:
	pass

pulse_start=time.time()

#等待高电平结束


while GPIO.input(ECHO)==1:
	pass

pulse_end=time.time()

pulse_duration=pulse_end-pulse_start

#距离=时间*速度/2
#声速:343m/s
distance=pulse_duration*17150
distance=round(distance,2)
print("Distance:{}cm".format(distance))

GPIO.cleanup()