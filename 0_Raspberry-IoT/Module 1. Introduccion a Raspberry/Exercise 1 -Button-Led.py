import RPi.GPIO as GPIO 
import time
 
#GPIO mode BCM
GPIO.setmode(GPIO.BCM) 

#BUTTON pin 18 (BCM)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#LED pin 17 (BCM)
GPIO.setup(17,GPIO.OUT)
 
while True:

    input_state = GPIO.input(18)

    if input_state == False:
  
  		#Blink 1
  		time.sleep(0.2) 
    	GPIO.output(17,True);
		  time.sleep(0.2) 
    	GPIO.output(17,False);

    	#Blink 2
  		time.sleep(0.2) 
    	GPIO.output(17,True);
		  time.sleep(0.2) 
    	GPIO.output(17,False);

    	#Blink 3
  		time.sleep(0.2) 
    	GPIO.output(17,True);
		  time.sleep(0.2) 
    	GPIO.output(17,False);

 