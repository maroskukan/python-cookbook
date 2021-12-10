import time

hungry = True
# I need a pizza!

while hungry:

    print("Opening the front door")
    front_door = open("front_door.txt", "r")

    if "Pizza Guy" in front_door:
        print("Pizza is here!")
        hungry = False
    else:
        print("Pizza is not here yet")

    print("Closing the front door")
    front_door.close()

    time.sleep(1)
