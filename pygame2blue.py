import pygame
import BluetoothConnection

# Steering codes
FORWARD = "F"
BACK = "B"
LEFT = "L"
RIGHT = "R"
STRAIGHT = "S"
IDLE = "I"

# Pygame keycodes
UP_KEY = 273
DOWN_KEY = 274
LEFT_KEY = 276
RIGHT_KEY = 275

pygame.init()
screen = pygame.display.set_mode((400,400))

conn = BluetoothConnection.BluetoothConnection()
conn.createServer()

state = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == UP_KEY:
                conn.sendData(FORWARD)
                
            elif event.key == DOWN_KEY:
                conn.sendData(BACK)

            elif event.key == LEFT_KEY:
                conn.sendData(LEFT)
                
            elif event.key == RIGHT_KEY:
                conn.sendData(RIGHT)
                
                
        if event.type == pygame.KEYUP:
            if event.key == UP_KEY:
                conn.sendData(IDLE)
                
            elif event.key == DOWN_KEY:
                conn.sendData(IDLE)
                
            elif event.key == LEFT_KEY:
                conn.sendData(STRAIGHT)
                
            elif event.key == RIGHT_KEY:
                conn.sendData(STRAIGHT)
                    
                    
