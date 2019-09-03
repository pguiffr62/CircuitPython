# CircuitPython Demo - Cap Touch Multiple Pins
# Example does NOT work with Trinket M0!

import time
import board
import touchio
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
angle = 5
# Create a servo object, my_servo.

touch_A3 = touchio.TouchIn(board.A3)  # Not a touch pin on Trinket M0!
touch_A2 = touchio.TouchIn(board.A2)  # Not a touch pin on Trinket M0!

my_servo = servo.Servo(pwm)

while True:
    if touch_A3.value:
        if angle < 180:
            angle = angle+5
        my_servo.angle = angle
        time.sleep(0.05)
        print("Touched A3!")
    if touch_A2.value:
        if angle > 0:
            angle = angle - 5
        my_servo.angle = angle
        time.sleep(0.05)
        print("Touched A2!")