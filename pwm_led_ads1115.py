# Raspberry Pi 3 – LED brightness control using potentiometer + ADS1115
# Wiring:
#   ADS1115:
#       VDD -> 3.3V
#       GND -> GND
#       SCL -> GPIO3
#       SDA -> GPIO2
#       A0 -> Potentiometer center pin
#   Potentiometer:
#       Left pin -> 3.3V
#       Right pin -> GND
#       Center pin -> A0 on ADS1115
#   LED:
#       Anode -> 330Ω resistor -> GPIO18 (PWM)
#       Cathode -> GND
# Description:
#   Reads the potentiometer’s analog voltage via the ADS1115 ADC.
#   Maps the 16-bit digital value to a PWM duty cycle (0–100%) on GPIO18.
#   Adjusts LED brightness smoothly based on potentiometer position.s

import time
import board
import busio
import RPi.GPIO as GPIO
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS

# Pin setup
LED_PIN = 18  # PWM pin for LED brightness

# Setup GPIO for PWM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize PWM at 1000Hz frequency
pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)  # start with LED off

# Initialize I2C communication for ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
channel = AnalogIn(ads, ADS.P0)  # Read from A0

try:
    print("Starting PWM control with potentiometer (Ctrl+C to stop)...")
    while True:
        # Read potentiometer value (0–65535 from ADS1115)
        value = channel.value

        # Convert to duty cycle (0–100%)
        duty_cycle = (value / 65535) * 100
        pwm.ChangeDutyCycle(duty_cycle)

        print(f"Potentiometer: {value:5d} -> LED brightness: {duty_cycle:5.1f}%")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO cleaned up. Goodbye!")
