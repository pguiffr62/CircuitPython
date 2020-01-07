# Circuitpython Assignments

### 2019-2020 // Engineering 3  


## LED Fade
#### Description 
The Goal of this assignment was to connect a metor express board and wiring an LED to a 220 resistor and have it Fade in and out of brightness. I wired an LED to my Metro board connecting the LED to a 220 resistor and coded it with a new language curcuit python to have it fade in and out. I used duty cycles and PWM in my code in order for it to work.  

#### Fritzing 
<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/fade.jpg" width="350">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35) 

#### Lessons Learned
Learning this new code came with difficulties. I had to learn how to write 'while true' statements which are similar to 'if then' statements in java script. I had to import libraries such as Pulsio and Digitalio in order for the code to opperate. I had to incorporate PWM and duty cycles which were very difficult. 

PWM is important for the code to function. Here is a fun link [Circuitpython PWM link](https://learn.adafruit.com/circuitpython-essentials/circuitpython-pwm)

Understanding Duty cycles and how they fit into PWM is crucial heres another helpful link  [Circuitpython dutycycle link](https://circuitpython.readthedocs.io/en/3.x/shared-bindings/pulseio/PWMOut.html)


## Servo 
#### Description 
The purpose of this assignment was to wire a Servo to a Metro express board and code it useing circuitpython to sweep from 180 to 0 degrees and have it controlled by two wires that when one is touched it will move. you will need to use imports such as 'pulsio' 'touchio'. You also need to incorportate PWMout. I used pulsio to create a PWMout object on pin A2. I used touchio to create an object for servo. I then used a "while true' statement to have the servo spin one way if it is above an angle of 180 and the other direction if the angle is below 180.

#### Fritzing 
<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/servo.jpg" width="350">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35) 

#### Lessons Learned
 I started my code by incorporating pulsio into my code which was a new library for me. I had trouble with the 'if' statements in this, I learned that I had to contain all of the information about the angle under my object for touchio and its pin to specify when one wire was touched it would move in one dirrection and when the other was touched it would move in the other. 

## LCD
#### Description 
In this assignment I had to wire a button and an LCD with backpack to my Metro and when the button is pressed it displays the amount of button presses on an LCD Screen as well as in the serial monitor. Using my java code  from last year I modeled my python code off of it. 

#### Fritzing 
<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/lcdcount.jpg" width="350">


Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35) 

#### Lessons Learned
I had difficulties only extracting certain parts that I needed from a library. I used this [video](https://www.youtube.com/watch?v=yoW2jHoVdug) to learn how to unzip files and extract certain documents. 


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


