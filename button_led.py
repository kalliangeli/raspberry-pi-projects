# Raspberry Pi 3 – LED (GPIO 17) controlled by push button (GPIO 27)
# Wiring:
#   LED anode -> 330Ω resistor -> GPIO17
#   LED cathode -> GND
#   Button one side -> 3V3
#   Button other side -> GPIO27   (internal pull-down enabled)
# Description:
#   Turns the LED on while the push button is pressed.
#   Demonstrates digital input/output handling using RPi.GPIO.

import RPi.GPIO as GPIO
import time

LED_PIN = 17       # BCM numbering
BUTTON_PIN = 27    # BCM numbering

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # LED output
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

    # Button input with internal pull-down (reads HIGH when pressed)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # optional: software debounce helper
    DEBOUNCE_S = 0.02     # 20 ms
    last_state = GPIO.input(BUTTON_PIN)

    print("Running. Press the button to light the LED. Ctrl+C to exit.")
    try:
        while True:
            state = GPIO.input(BUTTON_PIN)

            # simple debounce: only act on stable changes
            if state != last_state:
                time.sleep(DEBOUNCE_S)
                state = GPIO.input(BUTTON_PIN)

            # LED follows button: ON while pressed
            GPIO.output(LED_PIN, GPIO.HIGH if state else GPIO.LOW)

            last_state = state
            time.sleep(0.005)  # small loop delay
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()
        print("\nCleaned up GPIO. Bye!")

if __name__ == "__main__":
    main()
