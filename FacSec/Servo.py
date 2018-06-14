import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(24,GPIO.OUT)

try:
	while True:
		GPIO.output(24,1)
		time.sleep(0.0015)
		GPIO.output(24,0)

		time.sleep(0)

except KeyboardInterrupt:
	GPIO.cleanup()
