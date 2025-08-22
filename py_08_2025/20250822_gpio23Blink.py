import RPi.GPIO as GPIO
import time

# Use BCM numbering (GPIO25 = Pin 22)
# Use BCM numbering (GPIO24 = Pin 18)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

print("Blinking LED on GPIO 23. Press Ctrl+C to stop.")

try:
    while True:
        GPIO.output(23, GPIO.HIGH)  # LED ON
        time.sleep(1)               # 1 second
        GPIO.output(23, GPIO.LOW)   # LED OFF
        time.sleep(1)               # 1 second

except KeyboardInterrupt:
    print("\nExiting program...")

finally:
    GPIO.cleanup()  # Reset GPIO settings

