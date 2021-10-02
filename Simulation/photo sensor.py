from time import *
from physical import *
from gpio import *
from environment import Environment


ENVIRONMENT_NAME = "Visible Light"        # var ENVIRONMENT_NAME
state = LOW        # var state


def setup ():
    pinMode(0, OUTPUT)
    pinMode(A0, OUTPUT)
    setState(state)



def loop ():
    value = Environment.get(ENVIRONMENT_NAME)
    	# var value
    
    print(value)
    analogWrite(A0, value)
    if value > 20:
        setState(HIGH)
    else:
        setState(LOW)
    sleep(1)



def setState (newState):
    state = newState
    digitalWrite(0, state)
    value = Environment.get(ENVIRONMENT_NAME)
    #print(value)	# var value
   # analogWrite(A0, value)
    setDeviceProperty(getName(), "state", state)
   


if __name__ == "__main__":
    setup()
    while True:
        loop()

