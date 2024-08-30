import json
import os
import random

for so in range(533, 1293):
    chest = random.randint(414, 532)
    print("insert into chest_item values (" + str(chest) + "," + str(so) + "," + str(1) + ");")