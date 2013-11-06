import steering as steering

import BluetoothConnection

FORWARD = "F"
BACK = "B"
LEFT = "L"
RIGHT = "R"
STRAIGHT = "S"
IDLE = "I"
SLOW = "2"
FAST = "1"

steer = steering.steering(2)

state = None

conn = BluetoothConnection.BluetoothConnection()
conn.createClient('10:C6:1F:1E:AE:C4', 3)


while True:
    data = conn.receiveData(4)
    
    print data

    """
    if comm == FORWARD:
        state = steering.FORW
        
    elif comm == BACK:
        state = steering.BACK
    
    elif comm == IDLE:
        state = steering.IDLE

    elif comm == LEFT:
        steer.steer(steering.LEFT)
        
    elif comm == RIGHT:
        steer.steer(steering.RIGHT)
        
    elif comm == STRAIGHT:
        steer.steer(steering.STRAIGHT)
    
    elif comm == SLOW:
        steer.setVelocity(2)
    
    elif comm == FAST:
        steer.setVelocity(1)
        
    
    if state == steering.FORW:
        steer.steer(steering.FORW)

    elif state == steering.BACK:
        steer.steer(steering.BACK)

    elif state == steering.IDLE:
        steer.steer(steering.IDLE)
    """