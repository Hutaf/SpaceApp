from time import *
from gpio import *
from environment import Environment


ENVIRONMENT_NAME = "Wind Speed"        # var ENVIRONMENT_NAME
value  = 0      # var value


def loop ():
    global value

    value = Environment.get(ENVIRONMENT_NAME)
    print(value)
    analogWrite(A0, value)
    if value >= 0.001:
        analogWrite(A0, 1000)
    else:
        analogWrite(A0, 0)
    delay(1000)



if __name__ == "__main__":
#    setup()
    while True:
        loop()
        sleep(0)

