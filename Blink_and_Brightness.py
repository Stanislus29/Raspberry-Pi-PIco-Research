from ledclass import LED
import time

# Create LEDs
boardLed = LED("LED")  # Onboard LED
extLed = LED(21)       # External LED on GPIO 21

# Start animations
boardLed.blink(delay=0.3)       # Fast blink
extLed.fade(minP=20, maxP=80)   # Smooth breathing effect

# Main loop updates both LEDs
while True:
    boardLed.update()
    extLed.update()
    # Can do other tasks here (buttons, sensors, etc.)