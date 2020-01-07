# circuitpython

### 2019-2020 // Engineering 3 // All pictures are from Tim Wiessman's github page

## LED Fade
# Description 
The Goal of this assignment was to wire an LED to Fade in and out of brightness. I wired a metro board express to get an LED to fade in and out by using curcuit python. Learning this new code came with difficulties assignment just because I had never used curcuit python before and figureing it out was difficult, especially the duty cycles. 

# Fritzing 
<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/fade.jpg" width="350">

# Lessons Learned
PWM is important for the code to function. Here is a fun link [Circuitpython PWM link](https://learn.adafruit.com/circuitpython-essentials/circuitpython-pwm)

Understanding Duty cycles and how they fit into PWM is crucial heres another helpful link  [Circuitpython dutycycle link](https://circuitpython.readthedocs.io/en/3.x/shared-bindings/pulseio/PWMOut.html)


## Servo 
The goal of this assignment was to have a Servo sweep from 180 to 0 degrees using two wires to control the movements dirrection and when the wires are touched. This assignment was pretty simple with the exeption of pulsio which was a new and slightly difficult concept for me to grasp. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/servo.jpg" width="350">


## LCD
The Goal of this assignment was to display the amount of button presses on an LCD Screen. To use the LCD screen it requires you  using a button to have an LCD read the amount of counts. Using my code from last year this assignment wasn't too difficult it did teach me how to only extract certain parts that I needed from a library. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/lcdcount.jpg" width="350">


## Photo Interrupter
Using a photo interupter wired to a Metro Board Express I counted the amount of times the sensors were interrupted using the serial monitor. I had problems with it printing the vaule continuously and not every 4 seconds. I fixed this by creating a variable equal to 4 and using another variable with the code time.time to solve my problem. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/photointerrupter.jpg" width="350">


## Distance Sensor
In this assignment I wired up a distance sensor to sense the distance of an object from it, much like in our ultrasonic robot project from freshmen year. However there was the aditional challenge in this assignment to have the Neopixel on the Metro to light up. When the object was detected close it was red and the farther away it got it went through the rainbow, very pretty! This required me to use mapping in my code which wasnt that hard but new so I had to do a lot of googling of how to represent each color in my code. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/ultrasonicsensor.jpg" width="350">


## Classes, Objects, and Modules 
Here I had to make a class that would set variables and functions that would make prexisiting code on canvas to work. This code enabled two RBG LEDs to fade through all colors of rainbow, once again pretty! Making classes was difficult and hard to get used to but once I figured out what to put in def_int_ i was good. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/rgb.jpg" width="350">


## Hello vs Code
I wrote simple Hello world code into a new program called VS Code and committed and pushed it to Git Hub straight from there. It was difficult to learn how to git add and commit but once I realized how to connect Git Hub and Vs code it was simple simple click the plus sign to add my code and ctrl enter with a comment of what I did to commit to my git hub repository. 


## Fancy LED
This combined both the Hello vs Code and Classes, Objects and Modules assignments. This assignment was to wire 6 leds to turn on id a specific order(alternate, chase, blink, sparkle). There was exisiting code in canvas which I hade to make a class code for. The ussage of for statements for repeated code helped to clean up code. 


<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/fancyLED.jpg" width="350">


