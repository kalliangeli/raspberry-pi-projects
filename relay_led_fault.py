# Raspberry Pi 3 – Control Relay and LED (Fault indicator)
# Wiring:
#   Relay module:
#       VCC -> 5V
#       GND -> GND
#       IN -> GPIO17
#   LED (Fault indicator):
#       Anode -> 330Ω resistor -> GPIO4
#       Cathode -> GND
# Description:
#   Simulates a fault condition that activates a relay and lights an LED.
#   Demonstrates digital output control for both relay and LED.

import RPi.GPIO as GPIO
import time

# Pin configuration
RELAY_PIN = 17  # Signal pin to control the relay
LED_PIN = 4     # LED indicator for fault

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initially everything OFF
GPIO.output(RELAY_PIN, GPIO.LOW)
GPIO.output(LED_PIN, GPIO.LOW)

def activate_fault():
    """Simulate a fault condition (turn ON relay and LED)."""
    print("Fault detected! Activating relay and LED...")
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    GPIO.output(LED_PIN, GPIO.HIGH)

def clear_fault():
    """Clear the fault (turn OFF relay and LED)."""
    print("Fault cleared. Turning off relay and LED.")
    GPIO.output(RELAY_PIN, GPIO.LOW)
    GPIO.output(LED_PIN, GPIO.LOW)

try:
    print("System running. Press Ctrl+C to exit.")
    while True:
        # Normal state
        clear_fault()
        time.sleep(5)

        # Simulate a fault condition
        activate_fault()
        time.sleep(3)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.output(RELAY_PIN, GPIO.LOW)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleaned up. Goodbye!")
