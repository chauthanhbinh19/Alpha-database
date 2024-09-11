import json
import os
import random

for so in range(533, 1293):
    chest = random.randint(414, 532)
    print("insert into chest_item values (" + str(chest) + "," + str(so) + "," + str(1) + ");")
    chest2=random.randint(414,532)
    if chest != chest2:
        print("insert into chest_item values (" + str(chest2) + "," + str(so) + "," + str(1) + ");")    