import RPi.GPIO as GPIO
import time
import sys

inputModes = ["IN", "UP", "DOWN"]
outputModes = ["HIGH", "LOW"]

try:
    pin = int(sys.argv[1])
    mode = sys.argv[2].upper()
except:
    if len(sys.argv) >= 2:
        raise ValueError("Invalid parameter values...")
    print("Params: pin(int), mode(IN, UP, DOWN, HIGH, LOW)")


print(f"PIN #: {pin}")
print(f"PIN MODE: {mode}")

start_time = time.time()
GPIO.setmode(GPIO.BCM)

if mode in inputModes:
    modeNum = inputModes.index(mode)
    if modeNum == 0:
        GPIO.setup(pin, GPIO.IN)
    elif modeNum == 1:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    elif modeNum == 2:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
    
    time.sleep(1)

    print()

    while True:
        print("--- %s seconds ---" % round((time.time() - start_time),1))
        if GPIO.input(pin):
            print(f"Pin {pin} ({mode}) is HIGH")
        else:
            print(f"Pin {pin} ({mode}) is LOW")

        time.sleep(0.1)

elif mode in outputModes:
    modeNum = outputModes.index(mode)
    GPIO.setup(pin, GPIO.OUT)
    if modeNum == 0:
        print(f"Setting pin {pin} to HIGH")
        GPIO.output(pin, GPIO.HIGH)
    elif modeNum == 1:
        print(f"Setting pin {pin} to LOW")
        GPIO.output(pin, GPIO.LOW)
else:
    raise ValueError("Invalid value for pin mode.")