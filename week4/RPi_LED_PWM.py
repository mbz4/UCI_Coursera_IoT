'''
This program uses GPIO pin 18 to control the LED. 
The PWM frequency is set to 1000 Hz, and the maximum duty cycle
 (i.e., maximum brightness) is set to 100%. The program gradually
   increases the brightness of the LED by incrementing the duty cycle from 0% to 100%, 
   with a 10 ms delay between each increment. Then it gradually decreases 
   the brightness of the LED by decrementing the duty cycle from 100% to 0%, 
   with a 10 ms delay between each decrement. Finally, it stops the PWM signal and cleans up the GPIO pins.

Note that you will need to wire the LED in series with an appropriate 
resistor to limit the current flowing through it. The value of the resistor 
will depend on the specifications of the LED and the voltage used to power the circuit.
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 18  # GPIO pin connected to the LED
freq = 1000   # PWM frequency (Hz)
max_brightness = 100  # maximum duty cycle (%)

GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, freq)
pwm.start(0)  # start with duty cycle of 0

# gradually increase brightness
for brightness in range(0, max_brightness + 1):
    pwm.ChangeDutyCycle(brightness)
    time.sleep(0.01)  # wait 10 ms

# gradually decrease brightness
for brightness in range(max_brightness, -1, -1):
    pwm.ChangeDutyCycle(brightness)
    time.sleep(0.01)  # wait 10 ms

pwm.stop()
GPIO.cleanup()