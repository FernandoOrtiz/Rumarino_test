# Class to control the movement of the AUV
import time
import SerialCom


# Submerge the AUV to the desired depth
def submerge(depth):
    print("submerging to: " + depth)
    SerialCom.send(depth)


# Surface de desired feet
def surface(depth):
    print("going up: " + depth + " feet")
    SerialCom.send(depth)


# Move forward at a base 40% speed
def forward(seconds):
    print("moving at: 40%")
    # SerialCom.write0()
    # SerialCom.write1()
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Move forward at the desired speed
def forward_at(speed, seconds):
    print("moving at: " + speed)
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Move backward at a base 40% speed
def backward(seconds):
    print("Backing up at: 40%")
    # SerialCom.write0()
    # SerialCom.write1()
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Move backward at the desired speed speed
def backward_at(speed, seconds):
    print("Backing up at: " + speed)
    count = 0
    while count < seconds:
        time.sleep(1)
        align()
        count += 1


# Rotates the entered angles COUNTER-CLOCKWISE
def left(angle):
    print("moving left " + str(angle) + " degrees")


# Rotates the entered angles CLOCKWISE
def right(angle):
    print("moving right " + str(angle) + " degrees")




# Stop AUV
def stop():
    print("stopping")
    seconds = 10
    count = 0
    while count < seconds:
        time.sleep(1)
        count += 1


# Get depth from the pressure sensor
def get_depth():
    return 4.0


