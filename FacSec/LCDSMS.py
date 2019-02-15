import time
#lcd.crlf
import RPi.GPIO as GPIO
import requests
#import json
import random
#import time

x = 0
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
GPIO.setup(14,GPIO.OUT)
a=GPIO.input(23)
while(true):
        #x = x+1
        if(23 == TRUE):
            GPIO.output(14,1)
        else:
            GPIO.output(14,0)

random_int = random.randrange(1000,10000)
name2 = input("users name ")
phone = 0
name = "2"
tanay_ph = 9712907611
anish_ph = 9008091950
if name2 == "tanay":
    phone = tanay_ph
    name = "tanay"
    print(random_int)

elif name2 == "anish":
    phone = anish_ph
    name = "anish"
    #phone = anish_ph
    print(random_int)

else:
    print("This User Does Not Exist!")
#random_int = random.randrange(1000,10000)
r = requests.get('https://maker.ifttt.com/trigger/sendsms/with/key/cFTVBLO8YrXeBsI_8RD3AM'+'?value1='+str(random_int)+'&'+'value2='+name+"&"+'value3='+str(phone))
r.status_code
#print(random_int)
#if


GPIO.setmode(GPIO.BCM)
from RPLCD.i2c import CharLCD
#lcd.clrf()
lcd = CharLCD('PCF8574', 0x27)
lcd.crlf()
lcd.write_string("Enter the OTP")
print("Enter the OTP")
lcd.cursor_pos = (0,0)
a = input("")
print(MATRIX[i][j])
a = int(a)
lcd.clear()
lcd.crlf()
lcd.cursor_pos = (0,0)
#---------------------------------------------------------------------------------------
#KEYPAD
import RPi.GPIO as GPIO

#import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MATRIX = [[1,2,3,'A'],
          [4,5,6,'B'],
          [7,8,9,'C'],
          ['*',0,'#','D']]

ROW = [5,6,13,19]
#COL = [21,20,16,26]
COL = [26,16,20,21]


for j in range(4):
        GPIO.setup(COL[j], GPIO.OUT)
        GPIO.output(COL[j], 1)

for i in range(4):
        GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
        while(True):
#               print("its runnin")
                for j in range(4):
#                       print("first")
                        GPIO.output(COL[j], 0)
                        for i in range(4):
                                a = GPIO.input(ROW[i])
                                if a == 0:
                                        print(MATRIX[i][j])
#                                               time.sleep(0.2)
                                while GPIO.input(ROW[i]) == 0:
                                        pass
                        GPIO.output(COL[j],1)
except KeyboardInterupt:
        GPIO.cleanup()

import RPi.GPIO as GPIO

#import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MATRIX = [[1,2,3,'A'],
          [4,5,6,'B'],
          [7,8,9,'C'],
          ['*',0,'#','D']]

ROW = [5,6,13,19]
#COL = [21,20,16,26]
COL = [26,16,20,21]


for j in range(4):
        GPIO.setup(COL[j], GPIO.OUT)
        GPIO.output(COL[j], 1)

for i in range(4):
        GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
        while(True):
#               print("its runnin")
                for j in range(4):
#                       print("first")
                        GPIO.output(COL[j], 0)
                        for i in range(4):
                                a = GPIO.input(ROW[i])
                                if a == 0:
                                        print(MATRIX[i][j])
#                                               time.sleep(0.2)
                                while GPIO.input(ROW[i]) == 0:
                                        pass
                        GPIO.output(COL[j],1)
except KeyboardInterupt:
        GPIO.cleanup()


#---------------------------------------------------------------------------------------
while(true):
#YOU WERE HERE

	if(a == random_int ):
		lcd.write_string("Access Granted")
		print ("Access Granted")
		GPIO.setup(24, GPIO.OUT)
		pwm=GPIO.PWM(24, 50)
		pwm.start(0)
		def SetAngle(angle):
        		duty = angle / 18 + 2
        		GPIO.output(24, True)
       			pwm.ChangeDutyCycle(duty)
        		time.sleep(1)
        		GPIO.output(24, False)
       			pwm.ChangeDutyCycle(0)
		SetAngle(0)
		time.sleep(2)
		SetAngle(90)
		pwm.stop()
	GPIO.cleanup()

else:
	lcd.write_string("Access Denied")



