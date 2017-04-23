import RPi.GPIO as GPIO
import time
from Adafruit_PWM_Servo_Driver import PWM
from sgh_PCF8591P import sgh_PCF8591P

GPIO.setwarnings(False)
PGNone = 0
PGFull = 1
PGLite = 2
PGType = PGNone


irFL = 7
irFR = 11
irMID = 15

L1 = 26
L2 = 24
R1 = 19
R2 = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(irFR, GPIO.IN) #Right IR sensor module
GPIO.setup(irMID, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Activation button
GPIO.setup(irFL, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left IR sensor module

speed = 40

try:
    pwm = PWM(0x40, debug = False)
    pwm.setPWMFreq(60)  # Set frequency to 60 Hz
except:
    PGType = PGLite
	
    #use pwm on inputs so motors don't go too fast
    GPIO.setup(L1, GPIO.OUT)
    p = GPIO.PWM(L1, 20)
    p.start(0)

    GPIO.setup(L2, GPIO.OUT)
    q = GPIO.PWM(L2, 20)
    q.start(0)

    GPIO.setup(R1, GPIO.OUT)
    a = GPIO.PWM(R1, 20)
    a.start(0)

    GPIO.setup(R2, GPIO.OUT)
    b = GPIO.PWM(R2, 20)
    b.start(0)


pcfADC = None # ADC object
try:
    pcfADC = sgh_PCF8591P(1) #i2c, 0x48)
except:
    PGType = PGLite



flag=0
while True:
	j=GPIO.input(irMID)
	if j==1: #Robot is activated when button is pressed
		flag=1
		print "Robot Activated",j
	
	while flag==1:
		i=GPIO.input(irFL) #Listening for output from right IR sensor
		k=GPIO.input(irFR) #Listening for output from left IR sensor
		if i==0: #Obstacle detected on right IR sensor
			print "Obstacle detected on Right",i 
			#Move in reverse direction
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(speed)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			q.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)

			#Turn robot left
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(speed)
    			a.ChangeDutyCycle(speed)
    			b.ChangeDutyCycle(0)
    			q.ChangeFrequency(speed + 5)
    			a.ChangeFrequency(speed + 5)
		if k==0: #Obstacle detected on left IR sensor
			print "Obstacle detected on Left",k
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(speed)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			q.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)
			
    			p.ChangeDutyCycle(speed)
    			q.ChangeDutyCycle(0)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			p.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)

		elif i==0 and k==0:
			print "Obstacles on both sides"
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(speed)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			q.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)

    			p.ChangeDutyCycle(speed)
    			q.ChangeDutyCycle(0)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			p.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)
			
		elif i==1 and k==1:	#No obstacles, robot moves forward
			print "No obstacles",i
			#Robot moves forward
    			p.ChangeDutyCycle(speed)
    			q.ChangeDutyCycle(0)
    			a.ChangeDutyCycle(speed)
    			b.ChangeDutyCycle(0)
   			p.ChangeFrequency(speed + 5)
    			a.ChangeFrequency(speed + 5)
		j=GPIO.input(irMID)
		if j==1: #De activate robot on pushin the button
			flag=0
			print "Robot De-Activated",j
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(0)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(0)
