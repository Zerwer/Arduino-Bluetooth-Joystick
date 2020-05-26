#include <hc06joy.h>

// This initiates serial port with HC-06
hc06joy joy;

void setup()
{
}

// Read packet, this will show up in the serial monitor
void loop() 
{
  joy.joyReturn();
}
