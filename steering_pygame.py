import pygame
import numpy as np

# GPIO Pinouts
FORW_PIN = 11
BACK_PIN = 10
LEFT_PIN = 8
RIGHT_PIN = 7

# States
FORW = 1
BACK = 2
IDLE = 3
LEFT = 4
RIGHT = 5
STRAIGHT = 6


class steering(object):
    
    def __init__(self, velocity):
        self.state = IDLE
        self.velocity = velocity
    
        self.cnt = 0
        pygame.init()
        
        self.screen = pygame.display.set_mode((800,800))
        self.position = [100,100]
        self.image = pygame.image.load("car.png")
            
    def setVelocity(self, velocity):
        self.velocity = velocity
    
    def steer(self, commando):
        self.cnt += 1
        if commando == LEFT:
            if self.cnt % self.velocity == 0:
                self.image = pygame.transform.rotate(self.image, -1)
            
        elif commando == RIGHT:
            if self.cnt % self.velocity == 0:
                self.image = pygame.transform.rotate(self.image, 1)
            
        elif commando == FORW:
            if self.cnt % self.velocity == 0:
                self.position[0] += 1
        
        elif commando == BACK:
            self.position[0] -= 1
        
        self.screen.fill((255,255,255))
        self.screen.blit(self.image, (self.position))
        pygame.display.flip()
            
            
        
