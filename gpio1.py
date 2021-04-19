import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
# set up pins
red = 16
green = 12
blue = 25
outputs = (red, green, blue)
gp.setup(outputs, gp.OUT)

topButton = 13
botButton = 26
inputs = (topButton, botButton)
gp.setup(inputs, gp.IN)

c = 0
while True:
    #print str(gp.gpio_function(green))
    
    gp.output((red,green), gp.LOW)
    gp.output(blue, gp.HIGH)
    time.sleep(.1)
    gp.output((red,green), gp.HIGH)
    gp.output(blue, gp.LOW)
    time.sleep(.2)
    c += 1
    

gp.cleanup()
