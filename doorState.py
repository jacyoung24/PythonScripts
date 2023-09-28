import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
closedPin = int(sys.argv[1])
openPin = int(sys.argv[2])
GPIO.setup(closedPin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(openPin, GPIO.IN, GPIO.PUD_UP)

if GPIO.input(closedPin):
    closed = False
else:
    closed = True

if GPIO.input(openPin):
    open = False
else:
    open = True

if closed != open:
    if closed:
        state = "CLOSED"
    elif open:
        state = "OPEN"
else:
    state = "STOPPED"

print(state)
