# Class gives a simple control to steering the RC car.
# call steering.steer([a,b]), where -100<=(a,b)<=100.
# and a gives the direction and b the forward/backward command.
 
import RPi.GPIO as GPIO
import numpy as np

# GPIO Pinouts
FORW_PIN = 18
BACK_PIN = 14 
LEFT_PIN = 4 
RIGHT_PIN = 17 


class steering(object):
    
    
    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
    
        for pin in [FORW_PIN, BACK_PIN]:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 1)
        for pin in [LEFT_PIN, RIGHT_PIN]:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        
        self.f = GPIO.PWM(FORW_PIN, 50)
        self.b = GPIO.PWM(BACK_PIN, 50)
        self.l = GPIO.PWM(LEFT_PIN, 50)
        self.r = GPIO.PWM(RIGHT_PIN, 50)
        
        self.f.start(0)
        self.b.start(0)
        self.l.start(0)
        self.r.start(0)
        
    
    def steer(self, commando):
        if commando[1] == 0:
            print "Standing."
            self.f.ChangeDutyCycle(0)
            self.b.ChangeDutyCycle(0)
        
        elif commando[1] < 0:
            print "Going BACK with vel " + repr(-commando[1])
            self.f.ChangeDutyCycle(0)
            self.b.ChangeDutyCycle(-commando[1])
        
        elif commando[1] > 0:
            print "Goind FORW with vel " + repr(commando[1])
            self.b.ChangeDutyCycle(0)
            self.f.ChangeDutyCycle(commando[1])
            
        
        if commando[0] == 0:
            print "Straight"
            self.l.ChangeDutyCycle(0)
            self.r.ChangeDutyCycle(0)
        
        elif commando[0] < 0:
            print "Right with " + repr(-commando[0])
            self.l.ChangeDutyCycle(0)
            self.r.ChangeDutyCycle(-commando[0])
        
        elif commando[0] > 0:
            print "Left with " + repr(commando[0])
            self.r.ChangeDutyCycle(0)
            self.l.ChangeDutyCycle(commando[0])
                
        
