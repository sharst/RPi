import pygame
import steering

# Pygame keycodes
UP_KEY = 273
DOWN_KEY = 274
LEFT_KEY = 276
RIGHT_KEY = 275

pygame.init()
screen = pygame.display.set_mode((400,400))

steer = steering.steering(2)

state = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == UP_KEY:
                state = steering.FORW
                
            elif event.key == DOWN_KEY:
                state = steering.BACK

            elif event.key == LEFT_KEY:
                steer.steer(steering.LEFT)
                
            elif event.key == RIGHT_KEY:
                steer.steer(steering.RIGHT)
                
                
        if event.type == pygame.KEYUP:
            if event.key == UP_KEY:
                state = steering.IDLE
                
            elif event.key == DOWN_KEY:
                state = steering.IDLE
                
            elif event.key == LEFT_KEY:
                steer.steer(steering.STRAIGHT)
                
            elif event.key == RIGHT_KEY:
                steer.steer(steering.STRAIGHT)
                    
                    
                    
        if state == steering.FORW:
            steer.steer(steering.FORW)
    
        elif state == steering.BACK:
            steer.steer(steering.BACK)
    
        elif state == steering.IDLE:
            steer.steer(steering.IDLE)