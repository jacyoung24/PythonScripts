import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
closeSensorPin = int(sys.argv[1])
openSensorPin = int(sys.argv[2])

GPIO.setup(closeSensorPin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(openSensorPin, GPIO.IN, GPIO.PUD_UP)

closeVal = GPIO.input(closeSensorPin)
openVal = GPIO.input(openSensorPin)
if (closeVal == GPIO.LOW and openVal == GPIO.HIGH):
    print("CLOSED")
elif (closeVal == GPIO.HIGH and openVal == GPIO.LOW):
    print("OPEN")
else:
    print("STOPPED")

GPIO.cleanup()