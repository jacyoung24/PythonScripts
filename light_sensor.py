#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import sys

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
# if no argument is given, use pin 4
if len(sys.argv) < 2:
    pin_to_circuit = 16
else:
    pin_to_circuit = int(sys.argv[1])

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        print(rc_time(pin_to_circuit))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
