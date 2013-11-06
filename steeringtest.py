import steering
import time

steer = steering.steering()


commands = [(100,0),(50,0),(0,0),(-50,0),(0,0),(100,100),(50,0),(100,-100)]

for command in commands:
    steer.steer(command)
    time.sleep(3)


print "Done."
