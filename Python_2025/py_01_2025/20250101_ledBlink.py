import RPi.GPIO as GPIO
import time

# Use BCM numbering
LED_PIN_12 = 12
LED_PIN_16 = 16
LED_PIN_17 = 17
LED_PIN_20 = 20
LED_PIN_21 = 21

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_12, GPIO.OUT)
GPIO.setup(LED_PIN_16, GPIO.OUT)
GPIO.setup(LED_PIN_17, GPIO.OUT)
GPIO.setup(LED_PIN_20, GPIO.OUT)
GPIO.setup(LED_PIN_21, GPIO.OUT)

print("Blinking LED... Press Ctrl+C to stop")

try:
    while True:
        GPIO.output(LED_PIN_12, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN_12, GPIO.LOW)   # Turn LED off
        time.sleep(1)                    # Wait 1 second

        GPIO.output(LED_PIN_16, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN_16, GPIO.LOW)   # Turn LED off
        time.sleep(1)                    # Wait 1 second

        GPIO.output(LED_PIN_17, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN_17, GPIO.LOW)   # Turn LED off
        time.sleep(1)                    # Wait 1 second

        GPIO.output(LED_PIN_20, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN_20, GPIO.LOW)   # Turn LED off
        time.sleep(1)                    # Wait 1 second

        GPIO.output(LED_PIN_21, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN_21, GPIO.LOW)   # Turn LED off
        time.sleep(1)                    # Wait 1 second

except KeyboardInterrupt:
    print("\nExiting and cleaning up...")
    GPIO.cleanup()


