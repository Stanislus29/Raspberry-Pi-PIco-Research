

Here’s the **updated Markdown file** with **applications for blink and PWM control (for external LEDs only)** added. I’ve also included explanations so learners and engineers can see how these methods extend the same class design.

---

# LED Control with Raspberry Pi Pico (MicroPython)

## 1. Overview

**Purpose**
Control LEDs on the Raspberry Pi Pico using MicroPython:

* Turn on the on-board LED (`"LED"`).
* Turn on an external LED on GPIO pin 21.
* Demonstrate **blink** and **PWM brightness control** for the external LED.

**Hardware Involved**

* Raspberry Pi Pico board.
* On-board LED (built-in).
* External LED connected to GPIO 21 (with resistor).

**Key Concept**

* Use `Pin` and `PWM` classes from `machine` module for GPIO control.
* Implement OOP for scalability (blink, brightness control).

---

## 2. High-Level Design (Object-Oriented Concept)

**Class: `LED`**

* Represents one LED (on-board or external).
* Handles initialization, ON/OFF, blinking, and brightness (PWM).

**Main Application**

* Creates objects for onboard and external LEDs.
* Turns both ON, but demonstrates **blink** and **PWM** features only on external LED.

---

## 3. Code Layers

### Hardware Abstraction Layer (HAL)

* Uses `machine.Pin` and `machine.PWM` to interface with hardware.

### Logic / Control Layer

* Methods for ON/OFF, blink, and PWM brightness control.

### Application Layer

* Instantiates LED objects and applies control logic.

---

## 4. Flow Explanation

1. Create LED objects (onboard and external).
2. Turn both ON.
3. Blink external LED (toggle ON/OFF repeatedly).
4. Adjust external LED brightness using PWM.

---

## 5. Scalability & Modifications

* Blink speed and PWM duty cycle can be modified easily.
* Class can be reused for multiple external LEDs by instantiating with different pins.
* AI algorithms can call blink or PWM methods for dynamic visual feedback.

---

## 6. Educational Notes

* **Beginners**: Introduces blinking and brightness control concepts.
* **Engineers**: Shows how OOP keeps code modular and scalable.

---

## Original Code (Functional Style)

```python
from machine import Pin 

BoardLed = Pin("LED", Pin.OUT)
BoardLed.value(1)

led = Pin(21, Pin.OUT)
led.value(1)
```

---

## Object-Oriented Rewrite (Extended with Blink and PWM)

```python
from machine import Pin, PWM
import time

class LED:
    def __init__(self, pin_id):
        self.pin = Pin(pin_id, Pin.OUT)
        self.pwm = None  # Initialize PWM object as None

    # Turn LED ON
    def turn_on(self):
        self.pin.value(1)
    
    # Turn LED OFF
    def turn_off(self):
        self.pin.value(0)

    # Blink LED a given number of times
    def blink(self, times=5, delay=0.5):
        for _ in range(times):
            self.turn_on()
            time.sleep(delay)
            self.turn_off()
            time.sleep(delay)

    # Enable PWM mode for brightness control
    def enable_pwm(self):
        self.pwm = PWM(self.pin)
        self.pwm.freq(1000)  # Set PWM frequency to 1kHz

    # Set LED brightness (0 to 100%)
    def set_brightness(self, percent):
        if self.pwm is None:
            self.enable_pwm()
        duty = int(65535 * (percent / 100))  # Scale to 16-bit duty cycle
        self.pwm.duty_u16(duty)

    # Disable PWM and return to normal ON/OFF mode
    def disable_pwm(self):
        if self.pwm:
            self.pwm.deinit()
            self.pwm = None

# Application Layer
if __name__ == "__main__":
    # Create onboard and external LEDs
    onboard_led = LED("LED")
    external_led = LED(21)

    # Turn both LEDs ON
    onboard_led.turn_on()
    external_led.turn_on()

    # Blink external LED
    external_led.blink(times=3, delay=0.3)

    # Use PWM to fade external LED brightness
    external_led.set_brightness(20)  # Dim to 20%
    time.sleep(1)
    external_led.set_brightness(80)  # Brighten to 80%
    time.sleep(1)
    external_led.disable_pwm()       # Back to normal mode
```

---

## Explanation of Object-Oriented Rewrite

### Why Use OOP Here?

* **Encapsulation**: Each LED’s logic (ON/OFF, blink, PWM) is kept inside one class.
* **Scalability**: Easily add more LEDs or features without rewriting main program.
* **Reusability**: Same class works for any GPIO pin.

---

### Code Walkthrough

#### **Class Initialization**

```python
def __init__(self, pin_id):
    self.pin = Pin(pin_id, Pin.OUT)
    self.pwm = None
```

* Initializes a pin for output.
* `self.pwm` starts as `None` (only used if brightness control is needed).

---

#### **Blink Method**

```python
def blink(self, times=5, delay=0.5):
    for _ in range(times):
        self.turn_on()
        time.sleep(delay)
        self.turn_off()
        time.sleep(delay)
```

* Toggles the LED ON/OFF multiple times.
* `times` → how many blinks; `delay` → speed of each blink.

---

#### **PWM Brightness Control**

```python
def enable_pwm(self):
    self.pwm = PWM(self.pin)
    self.pwm.freq(1000)

def set_brightness(self, percent):
    if self.pwm is None:
        self.enable_pwm()
    duty = int(65535 * (percent / 100))
    self.pwm.duty_u16(duty)
```

* Uses **Pulse Width Modulation (PWM)** for brightness.
* `percent` converts to duty cycle (0–65535).
* Frequency set to 1kHz for smooth dimming.

---

#### **Disable PWM**

```python
def disable_pwm(self):
    if self.pwm:
        self.pwm.deinit()
        self.pwm = None
```

* Stops PWM and returns to normal ON/OFF mode.

---

## What is `self` and `self.pin.value`?

### `self`

* Refers to the **current object** created from the class.
* Allows each LED object to have its own pin and methods.
* Example: `external_led.turn_on()` → `self` = `external_led`.

### `self.pin.value`

* `self.pin` is the `Pin` object tied to that LED.
* `.value(1)` sets pin **HIGH (ON)**, `.value(0)` sets pin **LOW (OFF)**.
* Encapsulates hardware control inside the class.

---

## Benefits of This Design

* **Modular**: Add blink or brightness to any LED easily.
* **Reusable**: Copy the `LED` class to other projects.
* **Clean**: Main program only calls high-level methods (`turn_on`, `blink`, `set_brightness`).
* **Scalable**: Add more LEDs or sensors without changing class internals.

---

Do you want me to **add a diagram for PWM duty cycle** (showing how brightness is controlled) in this Markdown file?
And should I **separate onboard LED logic** entirely from external LEDs (e.g., in its own class) to make it crystal clear for learners?