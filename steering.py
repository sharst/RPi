import RPi.GPIO as GPIO
import numpy as np

# GPIO Pinouts
FORW_PIN = 17
BACK_PIN = 4
LEFT_PIN = 3
RIGHT_PIN = 18


class steering(object):
    
    
    def __init__(self, velocity):
        
        GPIO.setmode(GPIO.BCM)
    
        for pin in [FORW_PIN, BACK_PIN, LEFT_PIN, RIGHT_PIN]:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 1)
        
        self.f = GPIO.PWM(FORW_PIN, 50)
        self.b = GPIO.PWM(BACK_PIN, 50)
        self.l = GPIO.PWM(LEFT_PIN, 50)
        self.r = GPIO.PWM(RIGHT_PIN, 50)
        
        self.f.start(0)
        self.b.start(0)
        self.l.start(0)
        self.r.start(0)
        
    
    def steer(self, commando):
        if commando[0] == 0:
            self.f.changeDutyCycle(0)
            self.b.changeDutyCycle(0)
        
        elif commando[0] < 0:
            self.f.changeDutyCycle(0)
            self.b.changeDutyCycle(-commando[0])
        
        elif commando[0] > 0:
            self.b.changeDutyCycle(0)
            self.f.changeDutyCycle(commando[0])
            
        
        if commando[1] == 0:
            self.l.changeDutyCycle(0)
            self.r.changeDutyCycle(0)
        
        elif commando[1] < 0:
            self.r.changeDutyCycle(0)
            self.l.changeDutyCycle(-commando[0])
        
        elif commando[1] > 0:
            self.l.changeDutyCycle(0)
            self.r.changeDutyCycle(commando[0])
                
        
