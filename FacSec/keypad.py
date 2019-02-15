from pad4pi import rpi_gpio
import time

# Setup Keypad
KEYPAD = [
        [1,2,3,"A"],
        [4,5,6,"B"],
        [7,8,9,"C"],
        ["*",0,"#","D"]
]


ROW_PINS = [19,21,23,29] 
COL_PINS = [31,33,35,37] 

factory = rpi_gpio.KeypadFactory()


keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)



def printKey(key):
  print(key)
  if (key=="1"):
    print("number")
  elif (key=="A"):
    print("letter")


keypad.registerKeyPressHandler(printKey)

try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()
