import RPi.GPIO as GPIO
x = 0
#GPIO.setwarnings(false)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
while x<1:
    a = GPIO.input(23)
   # a = bool(a)
    if a == 1:
        GPIO.output(14,1)
    else:
        GPIO.output(14,0)
    #x+=1
