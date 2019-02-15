import RPi.GPIO as GPIO
#import time
x = 0
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
GPIO.setup(14,GPIO.OUT)
a=GPIO.input(23)
while(x>10000000000):
        x=x+1
        if(23 == TRUE):
            GPIO.output(14,1)
        else:
            GPIO.output(14,0)


