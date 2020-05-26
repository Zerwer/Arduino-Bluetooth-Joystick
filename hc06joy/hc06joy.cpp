#include "Arduino.h"
#include "hc06joy.h"

hc06joy::hc06joy(){
    Serial.begin(9600);
}

// Function to get next send character and keep trying until one is received
char hc06joy::nextChar() {
  if(Serial.available()) return Serial.read();
  else nextChar();
}

// Function loops adding characters to a string until end comma is found, string is returned as an int
int hc06joy::getValue() {
  String val;
  while(true){
    char charVal = nextChar();
    if(charVal != ',' && charVal != '}') val+=charVal;
    else break; 
  }
  return val.toInt();
}

// Loop until begin packet character is found
// Then get values for each section
// Verify that end packet character is send and print results
int* hc06joy::joyReturn() {
  if(nextChar() == '{') {
    int retVal[] = {getValue(), getValue(), getValue(), -1};
    int realLast = getValue(); // arduino not reading last value properly
    retVal[3] = realLast;

    return retVal;
  } 
  joyReturn();
}