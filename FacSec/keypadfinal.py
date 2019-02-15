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
