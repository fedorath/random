import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) #Right IR sensor module
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Activation button
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left IR sensor module

GPIO.setup(26,GPIO.OUT) #Left motor control
GPIO.setup(24,GPIO.OUT) #Left motor control
GPIO.setup(19,GPIO.OUT) #Right motor control
GPIO.setup(21,GPIO.OUT) #Right motor control

 #use pwm on inputs so motors don't go too fast
GPIO.setup(26, GPIO.OUT)
1 = GPIO.PWM(26, 20)
1.start(0)

GPIO.setup(24, GPIO.OUT)
2 = GPIO.PWM(24, 20)
2.start(0)

GPIO.setup(19, GPIO.OUT)
3 = GPIO.PWM(19, 20)
3.start(0)

GPIO.setup(21, GPIO.OUT)
4 = GPIO.PWM(21, 20)
4.start(0)


#Motor stop/brake
GPIO.output(p,0) 
GPIO.output(q,0)
GPIO.output(a,0)
GPIO.output(b,0)
speed = 80
flag=0
while True:
	j=GPIO.input(13)
	if j==1: #Robot is activated when button is pressed
		flag=1
		print "Robot Activated",j
	
	while flag==1:
		i=GPIO.input(7) #Listening for output from right IR sensor
		k=GPIO.input(11) #Listening for output from left IR sensor
		if i==0: #Obstacle detected on right IR sensor
			print "Obstacle detected on Right",i 
			#Move in reverse direction
			GPIO.output(1,speed) #Left motor turns anticlockwise
			GPIO.output(2,0)  
			GPIO.output(3,speed) #Right motor turns clockwise
			GPIO.output(4,0)		
			time.sleep(1)

			#Turn robot left
			GPIO.output(1,0) #Left motor turns clockwise
			GPIO.output(2,speed)
			GPIO.output(3,speed) #Right motor turns clockwise
			GPIO.output(4,0)
			time.sleep(2)
		if k==0: #Obstacle detected on left IR sensor
			print "Obstacle detected on Left",k
			GPIO.output(1,speed)
			GPIO.output(2,0)
			GPIO.output(3,speed)
			GPIO.output(4,0)		
			time.sleep(1)

			GPIO.output(1,speed)
			GPIO.output(2,0)
			GPIO.output(3,0)
			GPIO.output(4,speed)
			time.sleep(2)

		elif i==0 and k==0:
			print "Obstacles on both sides"
			GPIO.output(1,speed)
			GPIO.output(2,0)
			GPIO.output(3,speed)
			GPIO.output(4,0)		
			time.sleep(2)

			GPIO.output(1,speed)
			GPIO.output(2,0)
			GPIO.output(3,0)
			GPIO.output(4,speed)
			time.sleep(4)
			
		elif i==1 and k==1:	#No obstacles, robot moves forward
			print "No obstacles",i
			#Robot moves forward
			GPIO.output(1,0)
			GPIO.output(2,speed)
			GPIO.output(3,0)
			GPIO.output(4,speed)
			time.sleep(0.5)
		j=GPIO.input(13)
		if j==1: #De activate robot on pushin the button
			flag=0
			print "Robot De-Activated",j
			GPIO.output(1,0)
			GPIO.output(2,0)
			GPIO.output(3,0)
			GPIO.output(4,0)
			time.sleep(1)
