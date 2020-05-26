#ifndef hc06joy_h
#define hc06joy_h

#include "Arduino.h"

class hc06joy {
    public:
        hc06joy(void);
        int* joyReturn(void);
    private:
        char nextChar(void);
        int getValue(void);
};

#endif