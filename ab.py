#!/usr/bin/python
import pi2go, time

pi2go.init()

# Here we set the speed to 40 out of 100 - feel free to change!
speed = 80

# Here is the main body of the program - a lot of while loops and ifs!
# In order to get your head around it go through the logical steps slowly!
while True:
    if pi2go.irLeft():
        
        
      while pi2go.irLeft():
        # While the left sensor detects something - spin right
        pi2go.spinRight(speed)
      pi2go.stop()
    if pi2go.irRight():
        
        
        
        
      while pi2go.irRight():
        # While the right sensor detects something - spin left
        pi2go.spinLeft(speed)
      pi2go.stop()
    
while not (pi2go.irLeft() or pi2go.irRight()):
    if pi2go.irCentre():
      pi2go.spinRight(speed)
      time.sleep(1)
    else:
        pi2go.forward(speed)
    pi2go.stop()
    
pi2go.cleanup()
