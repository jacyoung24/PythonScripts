import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
pin_to_circuit = int(sys.argv[1])
sens = int(sys.argv[2])

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while ((GPIO.input(pin_to_circuit) == GPIO.LOW) and count < 2 * sens):
        count += 1

    return count

value = rc_time(pin_to_circuit)
if value < sens:
    print("true")
else:
    print("false")

GPIO.cleanup()

