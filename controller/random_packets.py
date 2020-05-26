# Run to test in arduino is receiving correct data from the controller
# Will send random integers and if working properly both the arduino and controller will read the same
import serial
import time
import random

# Fill device name here
# Example: /dev/tty.HC-06
device = ''

# Connects to HC-06 at a baud rate of 9600
s = serial.Serial(port=device, baudrate=9600)

# {JoyX,JoyY,JoyZ,Pot}
# Loop sending random bits
while True:
    joyX = str(random.randrange(-256, 256))
    joyY = str(random.randrange(-256, 256))
    joyZ = str(random.randrange(0, 2))
    pot = str(random.randrange(0, 256))
    msg = '{'+joyX+','+joyY+','+joyZ+','+pot+'} '

    print(msg)
    s.write(bytes(msg, 'utf-8'))
    time.sleep(1)
