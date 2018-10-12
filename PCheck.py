import time

import Movement



# start mission logic
def start():

    print("Starting PCheck mission")
    Movement.submerge("4")
    time.sleep(4)
    Movement.submerge("10")
    time.sleep(4)
    Movement.surface("3")
    time.sleep(4)
    Movement.submerge("5")
    time.sleep(4)
    Movement.surface("1")
    time.sleep(4)
    print("exiting PCheck")