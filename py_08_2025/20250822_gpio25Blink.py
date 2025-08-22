import RPi.GPIO as GPIO
import time

# Use BCM numbering (GPIO25 = Pin 22)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

print("Blinking LED on GPIO 25. Press Ctrl+C to stop.")

try:
    while True:
        GPIO.output(25, GPIO.HIGH)  # LED ON
        time.sleep(2)               # 1 second
        GPIO.output(25, GPIO.LOW)   # LED OFF
        time.sleep(2)               # 1 second

except KeyboardInterrupt:
    print("\nExiting program...")

finally:
    GPIO.cleanup()  # Reset GPIO settings

