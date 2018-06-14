import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
pwm=GPIO.PWM(18, 50)
pwm.start(0)
def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(18, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(2)
	GPIO.output(18, False)
	pwm.ChangeDutyCycle(0)
SetAngle(0)
time.sleep(2)
SetAngle(90)
pwm.stop()
GPIO.cleanup()
