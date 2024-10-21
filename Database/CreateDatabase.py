import json
import os
import random

# for so in range(533, 1300):
#     chest = random.randint(414, 532)
#     with open('test.txt', 'a') as file:
#         file.write("insert into chest_item values (" + str(chest) + "," + str(so) + "," + str(1) + ");\n")
#     chest2=random.randint(414,532)
#     if chest != chest2:
#         with open('test.txt', 'a') as file:
#             file.write("insert into chest_item values (" + str(chest2) + "," + str(so) + "," + str(1) + ");\n") 
def create_campaign ():
    Equipment=[
        "Amnitus_Equipment","Angelis_Equipment","Bellion_Equipment","Benzamin_Equipment","Celestial_Blood",
        "Celestial_Body","Celestial_Equipment","Ceverus_Equipment","Delius_Equipment","Domitius_Equipment",
        "Etherium_Equipment","Everlyn_Equipment","EvilFruit_Equipment","Extra_Equipment","Faltus_Equipment",
        "Fealan_Equipment","Gamma_Equipment","Gem_Equipment","Hagoro_Equipment","Hakalite_Equipment",
        "Heatherus_Equipment","Ignis_Equipment","Ivitus_Equipment","Karis_Equipment","Karmus_Equipment",
        "Lotus_Equipment","Luminius_Equipment","Macus_Equipment","Morganis_Equipment","Mythical_Object",
        "Nimigazin_Equipment","Omonitus_Equipment","Pet_Equipment","Qiyantus_Equipment","Rainbow_Equipment",
        "Redvenger_Equipment","Retanic_Equipment","Souls_Equipment","Support_Equipment","Syncroharon_Equipment",
        "Uni_Equipment","Zodiac_Equipment","Zpower_Equipment","Pet","Monster","Military","Collaboration",
        "CollborationEquipment","Book","Captain","Card"
    ]
    Data=[
        "Pet","Monster","Military","Collaboration","CollborationEquipment","Book","Captain","Card"
    ]
    count=1
    level=0
    strength_multiplier=1
    description="Complete challenging quests and defeat powerful enemies to obtain this legendary weapon. Only those who demonstrate exceptional skill and perseverance will be worthy of wielding it."
    is_active="true"
    for equipment in Equipment:
        for i in range (100):
            with open('campaign.txt', 'a') as file:
                if "Equipment" in equipment:
                    file.write("insert into campaigns values ("+ str(count)+ ",'Chapter "+ str(i+1)+"','"+ str("Equipment")+"','"
                        + str(equipment)+"','"+ str("Normal") +"',"+str(level)+",'"+ str(description) +"');\n")
                else:
                    file.write("insert into campaigns values ("+ str(count)+ ",'Chapter "+ str(i+1)+"','"+ str(equipment)+"','"
                        + str(equipment)+"','"+ str("Normal") +"',"+str(level)+",'"+ str(description) +"');\n")
                strength_multiplier=i
                level=i
                enemies = random.sample(range(1, 40001), 6) 
                enemy1, enemy2, enemy3, enemy4, enemy5, enemy6 = enemies
                items = random.sample(range(533, 1300), 4) 
                item1, item2, item3, item4 = items
                # Normal
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(1)+ ",'Chapter "+ str(i+1)+"','"+ str("Eloria")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(1)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(1)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(1)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(1)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(1)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(1)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(1)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(1)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(1)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(1)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(2)+ ",'Chapter "+ str(i+1)+"','"+ str("Drakthar Ridge")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.1) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(2)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(2)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(2)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(2)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(2)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(2)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(2)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(2)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(2)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(2)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(3)+ ",'Chapter "+ str(i+1)+"','"+ str("Sylvanveil")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.2) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(3)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(3)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(3)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(3)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(3)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(3)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(3)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(3)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(3)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(3)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(4)+ ",'Chapter "+ str(i+1)+"','"+ str("Arkanis")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.3) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(4)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(4)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(4)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(4)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(4)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(4)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(4)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(4)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(4)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(4)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(5)+ ",'Chapter "+ str(i+1)+"','"+ str("Valkoria")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.4) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(5)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(5)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(5)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(5)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(5)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(5)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(5)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(5)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(5)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(5)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(6)+ ",'Chapter "+ str(i+1)+"','"+ str("Zephyros")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.5) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(6)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(6)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(6)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(6)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(6)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(6)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(6)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(6)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(6)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(6)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(7)+ ",'Chapter "+ str(i+1)+"','"+ str("Crimson Marsh")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.6) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(7)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(7)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(7)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(7)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(7)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(7)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(7)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(7)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(7)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(7)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(8)+ ",'Chapter "+ str(i+1)+"','"+ str("Frostholm")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.7) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(8)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(8)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(8)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(8)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(8)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(8)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(8)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(8)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(8)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(8)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(9)+ ",'Chapter "+ str(i+1)+"','"+ str("Astrador")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.8) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(9)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(9)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(9)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(9)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(9)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(9)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(9)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(9)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(9)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(9)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(10)+ ",'Chapter "+ str(i+1)+"','"+ str("Nytheria")+"','"+ str("Normal")+"',"
                    + str(level)+","+ str(strength_multiplier+0.9) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(10)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(10)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(10)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(10)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(10)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(10)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(10)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(10)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(10)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(10)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                # Hard
                strength_multiplier=strength_multiplier*2
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(11)+ ",'Chapter "+ str(i+1)+"','"+ str("Eloria")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(11)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(11)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(11)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(11)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(11)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(11)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values("+str(count)+","+str(11)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values("+str(count)+","+str(11)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values("+str(count)+","+str(11)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values("+str(count)+","+str(11)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(12)+ ",'Chapter "+ str(i+1)+"','"+ str("Drakthar Ridge")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.1) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(12)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(12)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(12)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(12)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(12)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(12)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(12)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(12)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(12)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(12)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(13)+ ",'Chapter "+ str(i+1)+"','"+ str("Sylvanveil")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.2) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(13)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(13)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(13)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(13)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(13)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(13)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(13)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(13)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(13)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(13)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(14)+ ",'Chapter "+ str(i+1)+"','"+ str("Arkanis")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.3) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(14)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(14)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(14)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(14)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(14)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(14)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(14)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(14)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(14)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(14)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(15)+ ",'Chapter "+ str(i+1)+"','"+ str("Valkoria")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.4) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(15)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(15)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(15)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(15)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(15)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(15)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(15)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(15)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(15)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(15)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(16)+ ",'Chapter "+ str(i+1)+"','"+ str("Zephyros")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.5) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(16)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(16)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(16)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(16)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(16)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(16)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(16)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(16)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(16)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(16)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(17)+ ",'Chapter "+ str(i+1)+"','"+ str("Crimson Marsh")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.6) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(17)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(17)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(17)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(17)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(17)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(17)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(17)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(17)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(17)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(17)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(18)+ ",'Chapter "+ str(i+1)+"','"+ str("Frostholm")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.7) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(18)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(18)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(18)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(18)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(18)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(18)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(18)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(18)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(18)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(18)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(19)+ ",'Chapter "+ str(i+1)+"','"+ str("Astrador")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.8) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(19)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(19)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(19)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(19)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(19)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(19)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(19)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(19)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(19)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(19)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(20)+ ",'Chapter "+ str(i+1)+"','"+ str("Nytheria")+"','"+ str("Hard")+"',"
                    + str(level+5)+","+ str(strength_multiplier+0.9) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(20)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(20)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(20)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(20)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(20)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(20)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(20)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(20)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(20)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(20)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                # Expert
                strength_multiplier=strength_multiplier*2
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(21)+ ",'Chapter "+ str(i+1)+"','"+ str("Eloria")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(21)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(21)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(21)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(21)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(21)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(21)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(21)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(21)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(21)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(21)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(22)+ ",'Chapter "+ str(i+1)+"','"+ str("Drakthar Ridge")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.1) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(22)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(22)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(22)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(22)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(22)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(22)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(22)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(22)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(22)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(22)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(23)+ ",'Chapter "+ str(i+1)+"','"+ str("Sylvanveil")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.2) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(23)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(23)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(23)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(23)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(23)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(23)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(23)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(23)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(23)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(23)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(24)+ ",'Chapter "+ str(i+1)+"','"+ str("Arkanis")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.3) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(24)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(24)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(24)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(24)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(24)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values("+str(count)+","+str(24)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(24)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(24)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(24)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(24)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(25)+ ",'Chapter "+ str(i+1)+"','"+ str("Valkoria")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.4) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(25)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(25)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(25)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(25)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(25)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(25)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(25)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(25)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(25)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(25)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(26)+ ",'Chapter "+ str(i+1)+"','"+ str("Zephyros")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.5) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(26)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(26)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(26)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(26)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(26)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(26)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(26)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(26)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(26)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(26)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(27)+ ",'Chapter "+ str(i+1)+"','"+ str("Crimson Marsh")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.6) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(27)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(27)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(27)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(27)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(27)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(27)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(27)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(27)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(27)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(27)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(28)+ ",'Chapter "+ str(i+1)+"','"+ str("Frostholm")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.7) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(28)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(28)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(28)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(28)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(28)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(28)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(28)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(28)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(28)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(28)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(29)+ ",'Chapter "+ str(i+1)+"','"+ str("Astrador")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.8) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(29)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(29)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(29)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(29)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(29)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(29)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(29)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(29)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(29)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(29)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(30)+ ",'Chapter "+ str(i+1)+"','"+ str("Nytheria")+"','"+ str("Expert")+"',"
                    + str(level+10)+","+ str(strength_multiplier+0.9) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(30)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(30)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(30)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(30)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(30)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(30)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(30)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(30)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(30)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(30)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                # Master
                strength_multiplier=strength_multiplier*2
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(31)+ ",'Chapter "+ str(i+1)+"','"+ str("Eloria")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(31)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(31)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(31)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(31)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(31)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(31)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(31)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(31)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(31)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(31)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(32)+ ",'Chapter "+ str(i+1)+"','"+ str("Drakthar Ridge")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.1) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(32)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(32)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(32)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(32)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(32)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(32)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(32)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(32)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(32)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(32)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(33)+ ",'Chapter "+ str(i+1)+"','"+ str("Sylvanveil")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.2) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(33)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(33)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(33)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(33)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(33)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(33)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(33)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(33)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(33)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(33)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(34)+ ",'Chapter "+ str(i+1)+"','"+ str("Arkanis")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.3) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(34)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(34)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(34)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(34)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(34)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(34)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(34)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(34)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(34)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(34)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(35)+ ",'Chapter "+ str(i+1)+"','"+ str("Valkoria")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.4) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(35)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(35)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(35)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(35)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(35)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(35)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(35)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(35)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(35)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(35)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(36)+ ",'Chapter "+ str(i+1)+"','"+ str("Zephyros")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.5) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(36)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(36)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(36)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(36)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(36)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(36)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(36)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(36)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(36)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(36)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(37)+ ",'Chapter "+ str(i+1)+"','"+ str("Crimson Marsh")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.6) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(37)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(37)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(37)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(37)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(37)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(37)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(37)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(37)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(37)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(37)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(38)+ ",'Chapter "+ str(i+1)+"','"+ str("Frostholm")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.7) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(38)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(38)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(38)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(38)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(38)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(38)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(38)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(38)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(38)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(38)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(39)+ ",'Chapter "+ str(i+1)+"','"+ str("Astrador")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.8) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(39)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(39)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(39)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(39)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(39)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(39)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(39)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(39)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(39)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(39)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_details values ("+ str(count)+ ","+ str(40)+ ",'Chapter "+ str(i+1)+"','"+ str("Nytheria")+"','"+ str("Master")+"',"
                    + str(level+15)+","+ str(strength_multiplier+0.9) +","+str(is_active)+",'"+ str(description) +"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(40)+","+str(enemy1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(40)+","+str(enemy2)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(40)+","+str(enemy3)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(40)+","+str(enemy4)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(40)+","+str(enemy5)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_detail_cards values ("+str(count)+","+str(40)+","+str(enemy6)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(40)+","+str(item1)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(40)+","+str(item2)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(40)+","+str(item3)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
                file.write("insert into campaign_rewards values ("+str(count)+","+str(40)+","+str(item4)+","+str(1)+",'Chapter "+ str(i+1)+"');\n")
        
        count=count+1

def create_quest():
    Equipment=[
        "Amnitus_Equipment","Angelis_Equipment","Bellion_Equipment","Benzamin_Equipment","Celestial_Blood",
        "Celestial_Body","Celestial_Equipment","Ceverus_Equipment","Delius_Equipment","Domitius_Equipment",
        "Etherium_Equipment","Everlyn_Equipment","EvilFruit_Equipment","Extra_Equipment","Faltus_Equipment",
        "Fealan_Equipment","Gamma_Equipment","Gem_Equipment","Hagoro_Equipment","Hakalite_Equipment",
        "Heatherus_Equipment","Ignis_Equipment","Ivitus_Equipment","Karis_Equipment","Karmus_Equipment",
        "Lotus_Equipment","Luminius_Equipment","Macus_Equipment","Morganis_Equipment","Mythical_Object",
        "Nimigazin_Equipment","Omonitus_Equipment","Pet_Equipment","Qiyantus_Equipment","Rainbow_Equipment",
        "Redvenger_Equipment","Retanic_Equipment","Souls_Equipment","Support_Equipment","Syncroharon_Equipment",
        "Uni_Equipment","Zodiac_Equipment","Zpower_Equipment","Pet","Monster","Military","Collaboration",
        "CollborationEquipment","Book","Captain","Card"
    ]
    count=1
    for equipment in Equipment:
        with open('quests.txt', 'a') as file:
            file.write("Insert into quests values ("+str(count)+",'Sweep campaigns 10 times','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",1000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Sweep campaigns 20 times','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",2000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Sweep campaigns 30 times','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",3000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Sweep campaigns 40 times','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",4000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Sweep campaigns 50 times','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",5000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Log in for today','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",1000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Summon one hero','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",1000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade equipment level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",4000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Open 5 chests','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",20000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade skills one','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade heroes level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade pets level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade monsters level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade books level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade captains level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade military level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade spell level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade collaborations level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1
            file.write("Insert into quests values ("+str(count)+",'Upgrade collaboration equipments level','',1,true);\n")
            file.write("Insert into quest_rewards values ("+str(43)+","+str(count)+",10000);\n")
            count=count+1

# create_campaign()
create_quest()
