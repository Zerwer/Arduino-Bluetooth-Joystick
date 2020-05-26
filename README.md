# Arduino-Bluetooth-Joystick
An arduino library and python script to send bluetooth joystick signals to an arduino.
Made for teaching students new to arduino how to build and remotely control one without too much complexity.

# Wiring
Just connect the following and you will be able to read the HC-06 data from the arduino serial interface:  
HC-06 - Arduino  
RXD - TX0  
TXD - RX0  
GND - GND  
VCC - 5V  
      
# Example
1. Wire the HC-06 to arduino
2. Install the hc06joy.zip as an arduino library
3. Build the example receiver to an arduino uno from the hc06joy library and open serial monitor on computer.
4. On the same or another computer open bluetooth settings and connect to HC-06.
5. Open controller/random_packets.py and set the device (Usually in /dev/).
6. Run random_packets.py and see if the controller and receiver match.
