# Raspberry Pi 3 – Temperature-based LED control using DHT22 sensor
# Wiring:
#   DHT22 sensor:
#       VCC (Power) -> 5V
#       GND -> GND
#       DATA -> GPIO17
#   LED1 (Normal temperature indicator):
#       Anode -> 330Ω resistor -> GPIO20
#       Cathode -> GND
#   LED2 (High temperature indicator):
#       Anode -> 330Ω resistor -> GPIO21
#       Cathode -> GND
# Description:
#   Reads temperature and humidity from the DHT22 sensor.
#   If temperature < 25°C: LED1 turns ON.
#   If temperature ≥ 25°C: LED2 turns ON.
#   Demonstrates sensor reading and conditional GPIO output.

import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Pin configuration
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17         # Signal pin for DHT22
LED1_PIN = 20        # e.g., green LED
LED2_PIN = 21        # e.g., red LED

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)

# Temperature threshold (°C)
TEMP_THRESHOLD = 25.0

try:
    print("Starting temperature monitoring... (Press Ctrl+C to stop)")
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print(f"Temp={temperature:.1f}°C  Humidity={humidity:.1f}%")

            if temperature < TEMP_THRESHOLD:
                # Normal temperature
                GPIO.output(LED1_PIN, GPIO.HIGH)
                GPIO.output(LED2_PIN, GPIO.LOW)
            else:
                # High temperature
                GPIO.output(LED1_PIN, GPIO.LOW)
                GPIO.output(LED2_PIN, GPIO.HIGH)
        else:
            print("Sensor failure. Check wiring or try again.")

        time.sleep(2)  # read every 2 seconds

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.output(LED1_PIN, GPIO.LOW)
    GPIO.output(LED2_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleaned up.")
