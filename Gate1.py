# Gate1 Mission

import time

import Movement



# start mission logic
def start():

    print("Starting Gate1 mission")
    # Submerge the AUV to 4 feet
    Movement.submerge("6")
    time.sleep(4)
    # Full 40% forward
    Movement.forward(9)

    print("exiting Gate1")

