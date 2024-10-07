import json
import os
import random

for so in range(533, 1293):
    chest = random.randint(414, 532)
    print("insert into chest_item values (" + str(chest) + "," + str(so) + "," + str(1) + ");")
    chest2=random.randint(414,532)
    if chest != chest2:
        print("insert into chest_item values (" + str(chest2) + "," + str(so) + "," + str(1) + ");") 

# def get_story(character):
#     stories = {
#         "Aegis": [
#             "Story Aegis 1",
#             "Story Aegis 2",
#             "Story Aegis 3",
#             "Story Aegis 4",
#             "Story Aegis 5",
#             "Story Aegis 6",
#             "Story Aegis 7",
#             "Story Aegis 8",
#             "Story Aegis 9",
#             "Story Aegis 10"
#         ],
#         "Domanus":[
#             "Story Domanus 1",
#             "Story Domanus 2",
#             "Story Domanus 3",
#             "Story Domanus 4",
#             "Story Domanus 5",
#             "Story Domanus 6",
#             "Story Domanus 7",
#             "Story Domanus 8",
#             "Story Domanus 9",
#             "Story Domanus 10"
#         ],
#     }
#     if character in stories:
#         return random.choice(stories[character])

# story = get_story("Domanus")
# print(story)