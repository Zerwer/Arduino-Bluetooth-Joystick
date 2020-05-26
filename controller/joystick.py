# Very simple controller to illustrate how to send commands to arduino
# The last integer in the packet is not used and is intended for a potentiometer
from tkinter import *
import serial

width = 200
height = 200
pressed = []

# Fill device name here
# Example: /dev/tty.HC-06
device = ''

# Connects to HC-06 at a baud rate of 9600
s = serial.Serial(port=device, baudrate=9600)

root = Tk()
root.geometry(str(width)+'x'+str(height))
root.title('Joystick')

display_area = Canvas(root, width=width, height=height)
display_area.pack()


# Sends a packet based on what keys are pressed
def send_packet(pressed_keys):
    joyX = 0
    joyY = 0
    joyZ = 0
    pot =0

    if 'W' in pressed_keys:
        joyY += 1

    if 'S' in pressed_keys:
        joyY -= 1

    if 'O' in pressed_keys:
        joyZ += 1

    if 'A' in pressed_keys:
        joyX -= 1

    if 'D' in pressed_keys:
        joyX += 1

    msg = '{' + str(joyX) + ',' + str(joyY) + ',' + str(joyZ) + ',' + str(pot) + '} '
    s.write(bytes(msg, 'utf-8'))


# Function used to draw the inputs and there current state
def draw_joystick(pressed_keys):
    display_area.delete('all')

    if 'W' in pressed_keys: display_area.create_text(width/2, (height/2)-(height/5), font='Arial 20', text='W')
    else: display_area.create_text(width/2, (height/2)-(height/5), font='Arial 20', text='w')

    if 'O' in pressed_keys: display_area.create_text(width/2, height/2, font='Arial 20', text='O')
    else: display_area.create_text(width/2, height/2, font='Arial 20', text='o')

    if 'S' in pressed_keys: display_area.create_text(width/2, (height/2)+(height/5), font='Arial 20', text='S')
    else: display_area.create_text(width/2, (height/2)+(height/5), font='Arial 20', text='s')

    if 'D' in pressed_keys: display_area.create_text((width/2)+(width/5), height/2, font='Arial 20', text='D')
    else: display_area.create_text((width/2)+(width/5), height/2, font='Arial 20', text='d')

    if 'A' in pressed_keys: display_area.create_text((width/2)-(width/5), height/2, font='Arial 20', text='A')
    else: display_area.create_text((width/2)-(width/5), height/2, font='Arial 20', text='a')


# All the events for each key
def forward(event):
    if 'W' in pressed:
        pressed.remove('W')
        draw_joystick(pressed)
    else:
        pressed.append('W')
        draw_joystick(pressed)

    send_packet(pressed)


def backward(event):
    if 'S' in pressed:
        pressed.remove('S')
        draw_joystick(pressed)
    else:
        pressed.append('S')
        draw_joystick(pressed)

    send_packet(pressed)

def left(event):
    if 'A' in pressed:
        pressed.remove('A')
        draw_joystick(pressed)
    else:
        pressed.append('A')
        draw_joystick(pressed)

    send_packet(pressed)

def right(event):
    if 'D' in pressed:
        pressed.remove('D')
        draw_joystick(pressed)
    else:
        pressed.append('D')
        draw_joystick(pressed)

    send_packet(pressed)

# Bind keys and draw controller
draw_joystick(pressed)
root.bind('<w>', forward)
root.bind('<s>', backward)
root.bind('<a>', left)
root.bind('<d>', right)
root.mainloop()
