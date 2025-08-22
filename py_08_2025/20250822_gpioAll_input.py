import RPi.GPIO as GPIO
import time
import os

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

# Pins to monitor
PINS = [23, 25]

# Setup pins as input
for pin in PINS:
    GPIO.setup(pin, GPIO.IN)

print("Monitoring GPIO 23 and 25 (press Ctrl+C to exit)")

try:
    while True:
        # Clear the console (works on Linux / macOS / Raspberry Pi)
        os.system("clear")

        print("GPIO Status Monitor\n---------------------")
        for pin in PINS:
            state = GPIO.input(pin)
            status = "HIGH (voltage detected)" if state == GPIO.HIGH else "LOW  (no voltage)"
            print(f"GPIO {pin}: {status}")
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()

