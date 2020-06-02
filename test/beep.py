import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #using BOARD interface


GPIO_IO=11 #bind GPIO

GPIO.setup(GPIO_IO,GPIO.OUT)

loop = 10

for i in range(0,loop):
	GPIO.output(GPIO_IO,GPIO.HIGH) #mute
	time.sleep(3)
	GPIO.output(GPIO_IO,GPIO.LOW) #beep
	time.sleep(0.1)


GPIO.cleanup()