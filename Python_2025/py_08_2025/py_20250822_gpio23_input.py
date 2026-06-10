import RPi.GPIO as GPIO
import time

PIN = 23

# Use BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)  # Input mode

print("Monitoring GPIO 23 (press Ctrl+C to exit)")

try:
    while True:
        if GPIO.input(PIN) == GPIO.HIGH:
            print("GPIO 23 is HIGH (voltage detected)")
        else:
            print("GPIO 23 is LOW (no voltage)")
        time.sleep(0.1)  # check every 0.5s

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()

