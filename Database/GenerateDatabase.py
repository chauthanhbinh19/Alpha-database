import json
import os
import random

def calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                    speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality):
    weight_health = 1
    weight_physical_attack = 1.5
    weight_physical_defense = 1.2
    weight_magical_attack = 1.5
    weight_magical_defense = 1.2
    weight_chemical_attack = 1.5
    weight_chemical_defense = 1.2
    weight_atomic_attack = 1.5
    weight_atomic_defense = 1.2
    weight_mental_attack = 1.5
    weight_mental_defense = 1.2
    weight_speed = 1.5
    weight_critical_rate = 1.2
    weight_critical_damage = 1.5
    weight_armor_penetration = 1.2
    weight_avoid = 1.2
    weight_absorbs_damage = 1.2
    weight_regenerate_vitality = 1.2

    power=(
        health*weight_health+
        physical_attack*weight_physical_attack+
        physical_defense*weight_physical_defense+
        magical_attack*weight_magical_attack+
        magical_defense*weight_magical_defense+
        chemical_attack*weight_chemical_attack+
        chemical_defense*weight_chemical_defense+
        atomic_attack*weight_atomic_attack+
        atomic_defense*weight_atomic_defense+
        mental_attack*weight_mental_attack+
        mental_defense*weight_mental_defense+
        speed*weight_speed+
        critical_rate*weight_critical_rate+
        critical_damage*weight_critical_damage+
        armor_penetration*weight_armor_penetration+
        avoid*weight_avoid+
        absorbs_damage*weight_absorbs_damage+
        regenerate_vitality*weight_regenerate_vitality
    )
    return power

def create_cards_database():
    cards_dir="Cards"
    card_list = []
    id=1
    card_name=""
    health=1000000
    physical_attack=100000
    physical_defense=100000
    magical_attack=100000
    magical_defense=100000
    chemical_attack=100000
    chemical_defense=100000
    atomic_attack=100000
    atomic_defense=100000
    mental_attack=100000
    mental_defense=100000
    speed=10000
    critical_rate=0
    critical_damage=40000
    armor_penetration=10000
    avoid=0
    absorbs_damage=50000
    regenerate_vitality=3000
    mana=100
    rare="SR"
    clan=""
    price=100000
    price_unit="Chasmic_Blue_Crystalyte"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into cards values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")

                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        health=2000000
                        physical_attack=200000
                        physical_defense=200000
                        magical_attack=200000
                        magical_defense=200000
                        chemical_attack=200000
                        chemical_defense=200000
                        atomic_attack=200000
                        atomic_defense=200000
                        mental_attack=200000
                        mental_defense=200000
                        mana=200
                        rare="SSR"
                        price=500000
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into cards values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name,extension=os.path.splitext(file_name)
                        health=5000000
                        physical_attack=500000
                        physical_defense=500000
                        magical_attack=500000
                        magical_defense=500000
                        chemical_attack=500000
                        chemical_defense=500000
                        atomic_attack=500000
                        atomic_defense=500000
                        mental_attack=500000
                        mental_defense=500000
                        mana=500
                        rare="UR"
                        price=1000000
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into cards values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        health=10000000
                        physical_attack=1000000
                        physical_defense=1000000
                        magical_attack=1000000
                        magical_defense=1000000
                        chemical_attack=1000000
                        chemical_defense=1000000
                        atomic_attack=1000000
                        atomic_defense=1000000
                        mental_attack=1000000
                        mental_defense=1000000
                        mana=1000
                        rare="LG"
                        price=5000000
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into cards values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                        id=id+1

def create_books_database():
    cards_dir="Book"
    card_list = []
    id=1
    card_name=""
    health=20000000
    physical_attack=5000000
    physical_defense=5000000
    magical_attack=5000000
    magical_defense=5000000
    chemical_attack=5000000
    chemical_defense=5000000
    atomic_attack=5000000
    atomic_defense=5000000
    mental_attack=5000000
    mental_defense=5000000
    speed=50000
    critical_rate=0
    critical_damage=1000000
    armor_penetration=1500000
    avoid=0
    absorbs_damage=500000
    regenerate_vitality=500000
    mana=100
    rare="LG"
    price=2000000
    price_unit="Chasmic_Blue_Crystalyte"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                
                    power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                    print("insert into books values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                    id=id+1

def create_army_database():
    cards_dir="Army"
    card_list = []
    id=1
    card_name=""
    health=20000000
    physical_attack=5000000
    physical_defense=5000000
    magical_attack=5000000
    magical_defense=5000000
    chemical_attack=5000000
    chemical_defense=5000000
    atomic_attack=5000000
    atomic_defense=5000000
    mental_attack=5000000
    mental_defense=5000000
    speed=50000
    critical_rate=0
    critical_damage=1000000
    armor_penetration=1500000
    avoid=0
    absorbs_damage=500000
    regenerate_vitality=500000
    mana=100
    rare="LG"
    price=2000000
    price_unit="Chasmic_Blue_Crystalyte"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                    print("insert into army values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + dir_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                    id=id+1

def create_skills_database():
    cards_dir="Skill"
    card_list = []
    id=1
    card_name=""
    health=10000000
    physical_attack=2000000
    physical_defense=2000000
    magical_attack=2000000
    magical_defense=2000000
    chemical_attack=2000000
    chemical_defense=2000000
    atomic_attack=2000000
    atomic_defense=2000000
    mental_attack=2000000
    mental_defense=2000000
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    price=1000000
    price_unit="Chasmic_Purple_Crystalyte"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                    print("insert into skills values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + dir_name + "',"  + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                    id=id+1

def create_collaboration_equipments_database():
    cards_dir="CollborationEquipment"
    card_list = []
    id=1
    card_name=""
    health=1000000
    physical_attack=100000
    physical_defense=100000
    magical_attack=100000
    magical_defense=100000
    chemical_attack=100000
    chemical_defense=100000
    atomic_attack=100000
    atomic_defense=100000
    mental_attack=100000
    mental_defense=100000
    speed=10000
    critical_rate=0
    critical_damage=40000
    armor_penetration=10000
    avoid=0
    absorbs_damage=50000
    regenerate_vitality=3000
    mana=100
    rare="SR"
    clan=""
    price=100000
    price_unit="Chasmic_Blue_Crystalyte"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["MR","LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        name=name.encode('latin1', 'ignore').decode('latin1')
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")

                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.encode('latin1', 'ignore').decode('latin1')
                        health=2000000
                        physical_attack=500000
                        physical_defense=200000
                        magical_attack=500000
                        magical_defense=200000
                        chemical_attack=500000
                        chemical_defense=200000
                        atomic_attack=500000
                        atomic_defense=200000
                        mental_attack=500000
                        mental_defense=200000
                        mana=200
                        rare="SSR"
                        price=500000
                        name=name.replace("_"," ")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name,extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.encode('latin1', 'ignore').decode('latin1')
                        health=5000000
                        physical_attack=1000000
                        physical_defense=500000
                        magical_attack=1000000
                        magical_defense=500000
                        chemical_attack=1000000
                        chemical_defense=500000
                        atomic_attack=1000000
                        atomic_defense=500000
                        mental_attack=1000000
                        mental_defense=500000
                        mana=500
                        rare="UR"
                        price=1000000
                        name=name.replace("_"," ")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.encode('latin1', 'ignore').decode('latin1')
                        health=10000000
                        physical_attack=2000000
                        physical_defense=1500000
                        magical_attack=2000000
                        magical_defense=1500000
                        chemical_attack=2000000
                        chemical_defense=1500000
                        atomic_attack=2000000
                        atomic_defense=1500000
                        mental_attack=2000000
                        mental_defense=1500000
                        mana=1000
                        rare="LG"
                        price=5000000
                        name=name.replace("_"," ")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                        id=id+1
            if "MR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.encode('latin1', 'ignore').decode('latin1')
                        health=20000000
                        physical_attack=3000000
                        physical_defense=2000000
                        magical_attack=3000000
                        magical_defense=2000000
                        chemical_attack=3000000
                        chemical_defense=2000000
                        atomic_attack=3000000
                        atomic_defense=2000000
                        mental_attack=3000000
                        mental_defense=2000000
                        mana=1000
                        rare="LG"
                        price=5000000
                        name=name.replace("_"," ")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                        id=id+1

def create_bosses_database():
    cards_dir="Boss"
    card_list = []
    id=1
    card_name=""
    health=10000000000
    physical_attack=200000000
    physical_defense=200000000
    magical_attack=200000000
    magical_defense=200000000
    chemical_attack=200000000
    chemical_defense=200000000
    atomic_attack=200000000
    atomic_defense=200000000
    mental_attack=200000000
    mental_defense=200000000
    speed=1
    critical_rate=0
    critical_damage=100
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    price=10000000
    price_unit="Chasmic_Grey_Crystalyte"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    card = {
                        "id":id,
                        "SkillName":name,
                        "SkillNameImage": file_name,
                        "Health": health,
                        "PhysicalAttack": physical_attack,
                        "PhysicalDefense": physical_defense,
                        "MagicalAttack": magical_attack,
                        "MagicalDefense": magical_defense,
                        "ChemicalAttack": chemical_attack,
                        "ChemicalDefense": chemical_defense,
                        "AtomicAttack": atomic_attack,
                        "AtomicDefense": atomic_defense,
                        "MentalAttack": mental_attack,
                        "MentalDefense": mental_defense,
                        "Speed": speed,
                        "CriticalRate": critical_rate,
                        "CriticalDamage": critical_damage,
                        "ArmorPenetration": armor_penetration,
                        "Avoid": avoid,
                        "AbsorbsDamage": absorbs_damage,
                        "RegenerateVitality": regenerate_vitality,
                        "Mana": mana,
                        "Rare": rare,
                        "Type": dir_name,
                        "Price": price,
                        "PriceUnit":price_unit,
                        "Path":path
                    }
                    card_list.append(card)
                    id=id+1
    with open("bosses_database.json", "w") as json_file:
        json.dump(card_list, json_file)

def create_pets_database():
    cards_dir="Pet"
    card_list = []
    id=1
    card_name=""
    health=10000000
    physical_attack=1500000
    physical_defense=1500000
    magical_attack=1500000
    magical_defense=1500000
    chemical_attack=1500000
    chemical_defense=1500000
    atomic_attack=1500000
    atomic_defense=1500000
    mental_attack=1500000
    mental_defense=1500000
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    price=10000000
    price_unit="Ancient_Rune_Crystal_Fire"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                    print("insert into pets values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + dir_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")

                    id=id+1

def create_symbols_database():
    cards_dir="Symbol"
    card_list = []
    id=1
    card_name=""
    health=30000000
    physical_attack=3500000
    physical_defense=3500000
    magical_attack=3500000
    magical_defense=3500000
    chemical_attack=3500000
    chemical_defense=3500000
    atomic_attack=3500000
    atomic_defense=3500000
    mental_attack=3500000
    mental_defense=3500000
    per_health=10
    per_physical_attack=10
    per_physical_defense=10
    per_magical_attack=10
    per_magical_defense=10
    per_chemical_attack=10
    per_chemical_defense=10
    per_atomic_attack=10
    per_atomic_defense=10
    per_mental_attack=10
    per_mental_defense=10
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    price=10000000
    price_unit="Ancient_Rune_Crystal_Dark"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                    print("insert into symbols values (" + str(id) + ",'" + name + "','" + path + "','"+dir_name+"'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'');")

                    id=id+1

def create_medals_database():
    cards_dir="Medal"
    card_list = []
    id=1
    card_name=""
    health=30000000
    physical_attack=3500000
    physical_defense=3500000
    magical_attack=3500000
    magical_defense=3500000
    chemical_attack=3500000
    chemical_defense=3500000
    atomic_attack=3500000
    atomic_defense=3500000
    mental_attack=3500000
    mental_defense=3500000
    per_health=10
    per_physical_attack=10
    per_physical_defense=10
    per_magical_attack=10
    per_magical_defense=10
    per_chemical_attack=10
    per_chemical_defense=10
    per_atomic_attack=10
    per_atomic_defense=10
    per_mental_attack=10
    per_mental_defense=10
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
                
                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into medals values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'');")

                id=id+1
    
def create_achievements_database():
    cards_dir="Achievement"
    card_list = []
    id=1
    card_name=""
    health=10000000
    physical_attack=2000000
    physical_defense=2000000
    magical_attack=2000000
    magical_defense=2000000
    chemical_attack=2000000
    chemical_defense=2000000
    atomic_attack=2000000
    atomic_defense=2000000
    mental_attack=2000000
    mental_defense=2000000
    per_health=10
    per_physical_attack=10
    per_physical_defense=10
    per_magical_attack=10
    per_magical_defense=10
    per_chemical_attack=10
    per_chemical_defense=10
    per_atomic_attack=10
    per_atomic_defense=10
    per_mental_attack=10
    per_mental_defense=10
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
                
                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into achievements values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'');")
                id=id+1
    
def create_titles_database():
    cards_dir="Title"
    card_list = []
    id=1
    card_name=""
    health=10000000
    physical_attack=2000000
    physical_defense=2000000
    magical_attack=2000000
    magical_defense=2000000
    chemical_attack=2000000
    chemical_defense=2000000
    atomic_attack=2000000
    atomic_defense=2000000
    mental_attack=2000000
    mental_defense=2000000
    per_health=10
    per_physical_attack=10
    per_physical_defense=10
    per_magical_attack=10
    per_magical_defense=10
    per_chemical_attack=10
    per_chemical_defense=10
    per_atomic_attack=10
    per_atomic_defense=10
    per_mental_attack=10
    per_mental_defense=10
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")

                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into titles values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'');")
                id=id+1

def create_monster_database():
    cards_dir="Monster"
    card_list = []
    id=1
    card_name=""
    health=100000000
    physical_attack=30000000
    physical_defense=20000000
    magical_attack=30000000
    magical_defense=20000000
    chemical_attack=30000000
    chemical_defense=20000000
    atomic_attack=30000000
    atomic_defense=20000000
    mental_attack=30000000
    mental_defense=20000000
    per_health=10
    per_physical_attack=10
    per_physical_defense=10
    per_magical_attack=10
    per_magical_defense=10
    per_chemical_attack=10
    per_chemical_defense=10
    per_atomic_attack=10
    per_atomic_defense=10
    per_mental_attack=10
    per_mental_defense=10
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")

                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into monsters values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + "none" + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")
                id=id+1

def create_borders_database():
    cards_dir="Border"
    card_list = []
    id=1
    card_name=""
    health=10000000
    physical_attack=2000000
    physical_defense=2000000
    magical_attack=2000000
    magical_defense=2000000
    chemical_attack=2000000
    chemical_defense=2000000
    atomic_attack=2000000
    atomic_defense=2000000
    mental_attack=2000000
    mental_defense=2000000
    per_health=10
    per_physical_attack=10
    per_physical_defense=10
    per_magical_attack=10
    per_magical_defense=10
    per_chemical_attack=10
    per_chemical_defense=10
    per_atomic_attack=10
    per_atomic_defense=10
    per_mental_attack=10
    per_mental_defense=10
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into borders values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'');")
                id=id+1

def create_currencies_database():
    cards_dir="Currency"
    card_list = []
    id=1
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
                print("insert into currency values (" + str(id) + ",'" + name + "','" + path + "');")
                id=id+1

def create_items_database():
    cards_dir="Item"
    card_list = []
    id=1
    card_name=""
    price=10000000
    price_unit="Ancient_Rune_Crystal_Light"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    print("insert into items values (" + str(id) + ",'" + name + "','" + path + "','" + dir_name + "'," + str(1000) + ",'');")
                    id=id+1

def create_equipments_database():
    cards_dir="Equipment"
    card_list = []
    id=1
    card_name=""
    health=10000000000
    physical_attack=200000000
    physical_defense=150000000
    magical_attack=200000000
    magical_defense=150000000
    chemical_attack=200000000
    chemical_defense=150000000
    atomic_attack=200000000
    atomic_defense=150000000
    mental_attack=200000000
    mental_defense=150000000
    speed=1000000
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    price=100000
    price_unit=""
    path=""
    special_health=10000000000
    special_physical_attack=200000000
    special_physical_defense=150000000
    special_magical_attack=200000000
    special_magical_defense=150000000
    special_chemical_attack=200000000
    special_chemical_defense=150000000
    special_atomic_attack=200000000
    special_atomic_defense=150000000
    special_mental_attack=200000000
    special_mental_defense=150000000
    special_speed=1000000
    for root, dirs, files in os.walk(cards_dir):
        current_dir = os.path.basename(root)
        current_name=""
        current_name = os.path.basename(os.path.dirname(root))
        for dir_name in dirs:
            current_dir = os.path.join(root, dir_name)
            for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith(".png"):
                        name, extension = os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        set1_folder_name = os.path.basename(os.path.dirname(current_dir))
                        name=name.replace("_"," ")
                        name=name.encode('latin1', 'ignore').decode('latin1')
                        if "SR" in dir_name:
                            health=20000000
                            physical_attack=1000000
                            physical_defense=500000
                            magical_attack=1000000
                            magical_defense=500000
                            chemical_attack=1000000
                            chemical_defense=500000
                            atomic_attack=1000000
                            atomic_defense=500000
                            mental_attack=1000000
                            mental_defense=500000
                            variables = {
                                'special_health': 20000000,
                                'special_physical_attack': 1000000,
                                'special_physical_defense': 500000,
                                'special_magical_attack': 1000000,
                                'special_magical_defense': 500000,
                                'special_chemical_attack': 1000000,
                                'special_chemical_defense': 500000,
                                'special_atomic_attack': 1000000,
                                'special_atomic_defense': 500000,
                                'special_mental_attack': 1000000,
                                'special_mental_defense': 500000,
                                'special_speed': 5000000
                            }
                            selected_variables = random.sample(list(variables.keys()), 2)
                            for var in variables:
                                if var not in selected_variables:
                                    variables[var] = 0
                            power = calculate_power(health, physical_attack, physical_defense, magical_attack, magical_defense, chemical_attack, chemical_defense, atomic_attack, atomic_defense, mental_attack, mental_defense,
                                                    speed, critical_rate, critical_damage, armor_penetration, avoid, absorbs_damage, regenerate_vitality)
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + current_name + "','" + dir_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
                                "," + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense)
                                + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration)
                                + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + 
                                "," + str(list(variables.values())[0]) + ","+ str(list(variables.values())[1]) + "," + str(list(variables.values())[2]) + "," + str(list(variables.values())[3]) + "," + str(list(variables.values())[4]) + "," + str(list(variables.values())[5]) + "," + str(list(variables.values())[6])
                                + "," + str(list(variables.values())[7]) + "," + str(list(variables.values())[8]) + "," + str(list(variables.values())[9]) + "," + str(list(variables.values())[10]) + "," + str(list(variables.values())[11]) + ",'');")
                            id += 1
                        elif "SSR" in dir_name:
                            health=50000000
                            physical_attack=2500000
                            physical_defense=1000000
                            magical_attack=2500000
                            magical_defense=1000000
                            chemical_attack=2500000
                            chemical_defense=1000000
                            atomic_attack=2500000
                            atomic_defense=1000000
                            mental_attack=2500000
                            mental_defense=1000000
                            variables = {
                                'special_health': 50000000,
                                'special_physical_attack': 2500000,
                                'special_physical_defense': 1000000,
                                'special_magical_attack': 2500000,
                                'special_magical_defense': 1000000,
                                'special_chemical_attack': 2500000,
                                'special_chemical_defense': 1000000,
                                'special_atomic_attack': 2500000,
                                'special_atomic_defense': 1000000,
                                'special_mental_attack': 2500000,
                                'special_mental_defense': 1000000,
                                'special_speed': 10000000
                            }
                            selected_variables = random.sample(list(variables.keys()), 2)
                            for var in variables:
                                if var not in selected_variables:
                                    variables[var] = 0
                            power = calculate_power(health, physical_attack, physical_defense, magical_attack, magical_defense, chemical_attack, chemical_defense, atomic_attack, atomic_defense, mental_attack, mental_defense,
                                                    speed, critical_rate, critical_damage, armor_penetration, avoid, absorbs_damage, regenerate_vitality)
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + current_name + "','" + dir_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
                                "," + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense)
                                + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration)
                                + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + 
                                "," + str(list(variables.values())[0]) + ","+ str(list(variables.values())[1]) + "," + str(list(variables.values())[2]) + "," + str(list(variables.values())[3]) + "," + str(list(variables.values())[4]) + "," + str(list(variables.values())[5]) + "," + str(list(variables.values())[6])
                                + "," + str(list(variables.values())[7]) + "," + str(list(variables.values())[8]) + "," + str(list(variables.values())[9]) + "," + str(list(variables.values())[10]) + "," + str(list(variables.values())[11]) + ",'');")
                            id += 1
                        elif "UR" in dir_name:
                            health=100000000
                            physical_attack=5000000
                            physical_defense=2500000
                            magical_attack=5000000
                            magical_defense=2500000
                            chemical_attack=5000000
                            chemical_defense=2500000
                            atomic_attack=5000000
                            atomic_defense=2500000
                            mental_attack=5000000
                            mental_defense=2500000
                            variables = {
                                'special_health': 100000000,
                                'special_physical_attack': 5000000,
                                'special_physical_defense': 2500000,
                                'special_magical_attack': 5000000,
                                'special_magical_defense': 2500000,
                                'special_chemical_attack': 5000000,
                                'special_chemical_defense': 2500000,
                                'special_atomic_attack': 5000000,
                                'special_atomic_defense': 2500000,
                                'special_mental_attack': 5000000,
                                'special_mental_defense': 2500000,
                                'special_speed': 50000000
                            }
                            selected_variables = random.sample(list(variables.keys()), 2)
                            for var in variables:
                                if var not in selected_variables:
                                    variables[var] = 0
                            power = calculate_power(health, physical_attack, physical_defense, magical_attack, magical_defense, chemical_attack, chemical_defense, atomic_attack, atomic_defense, mental_attack, mental_defense,
                                                    speed, critical_rate, critical_damage, armor_penetration, avoid, absorbs_damage, regenerate_vitality)
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + current_name + "','" + dir_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
                                "," + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense)
                                + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration)
                                + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + 
                                "," + str(list(variables.values())[0]) + ","+ str(list(variables.values())[1]) + "," + str(list(variables.values())[2]) + "," + str(list(variables.values())[3]) + "," + str(list(variables.values())[4]) + "," + str(list(variables.values())[5]) + "," + str(list(variables.values())[6])
                                + "," + str(list(variables.values())[7]) + "," + str(list(variables.values())[8]) + "," + str(list(variables.values())[9]) + "," + str(list(variables.values())[10]) + "," + str(list(variables.values())[11]) + ",'');")
                            id += 1
                        elif "LG" in dir_name:
                            health=500000000
                            physical_attack=10000000
                            physical_defense=5000000
                            magical_attack=10000000
                            magical_defense=5000000
                            chemical_attack=10000000
                            chemical_defense=5000000
                            atomic_attack=10000000
                            atomic_defense=5000000
                            mental_attack=10000000
                            mental_defense=5000000
                            variables = {
                                'special_health': 500000000,
                                'special_physical_attack': 10000000,
                                'special_physical_defense': 5000000,
                                'special_magical_attack': 10000000,
                                'special_magical_defense': 5000000,
                                'special_chemical_attack': 10000000,
                                'special_chemical_defense': 5000000,
                                'special_atomic_attack': 10000000,
                                'special_atomic_defense': 5000000,
                                'special_mental_attack': 10000000,
                                'special_mental_defense': 5000000,
                                'special_speed': 100000000
                            }
                            selected_variables = random.sample(list(variables.keys()), 2)
                            for var in variables:
                                if var not in selected_variables:
                                    variables[var] = 0
                            if "Souls_Equipment" in current_name or "Gem_Equipment" in current_name:
                                if "lv1" in name:
                                    health=50000000
                                    physical_attack=1000000
                                    physical_defense=500000
                                    magical_attack=1000000
                                    magical_defense=500000
                                    chemical_attack=1000000
                                    chemical_defense=500000
                                    atomic_attack=1000000
                                    atomic_defense=500000
                                    mental_attack=1000000
                                    mental_defense=500000
                                elif "lv2" in name:
                                    health=80000000
                                    physical_attack=3000000
                                    physical_defense=1500000
                                    magical_attack=3000000
                                    magical_defense=1500000
                                    chemical_attack=3000000
                                    chemical_defense=1500000
                                    atomic_attack=3000000
                                    atomic_defense=1500000
                                    mental_attack=3000000
                                    mental_defense=1500000
                                elif "lv3" in name:
                                    health=150000000
                                    physical_attack=5000000
                                    physical_defense=2500000
                                    magical_attack=5000000
                                    magical_defense=2500000
                                    chemical_attack=5000000
                                    chemical_defense=2500000
                                    atomic_attack=5000000
                                    atomic_defense=2500000
                                    mental_attack=5000000
                                    mental_defense=2500000
                                elif "lv4" in name:
                                    health=350000000
                                    physical_attack=8000000
                                    physical_defense=5000000
                                    magical_attack=8000000
                                    magical_defense=5000000
                                    chemical_attack=8000000
                                    chemical_defense=5000000
                                    atomic_attack=8000000
                                    atomic_defense=5000000
                                    mental_attack=8000000
                                    mental_defense=5000000
                                elif "lv5" in name:
                                    health=600000000
                                    physical_attack=10000000
                                    physical_defense=5000000
                                    magical_attack=10000000
                                    magical_defense=5000000
                                    chemical_attack=10000000
                                    chemical_defense=5000000
                                    atomic_attack=10000000
                                    atomic_defense=5000000
                                    mental_attack=10000000
                                    mental_defense=5000000
                                elif "lv6" in name:
                                    health=1000000000
                                    physical_attack=40000000
                                    physical_defense=25000000
                                    magical_attack=40000000
                                    magical_defense=25000000
                                    chemical_attack=40000000
                                    chemical_defense=25000000
                                    atomic_attack=40000000
                                    atomic_defense=25000000
                                    mental_attack=40000000
                                    mental_defense=25000000
                                elif "lv7" in name:
                                    health=5000000000
                                    physical_attack=90000000
                                    physical_defense=50000000
                                    magical_attack=90000000
                                    magical_defense=50000000
                                    chemical_attack=90000000
                                    chemical_defense=50000000
                                    atomic_attack=90000000
                                    atomic_defense=50000000
                                    mental_attack=90000000
                                    mental_defense=50000000
                            power = calculate_power(health, physical_attack, physical_defense, magical_attack, magical_defense, chemical_attack, chemical_defense, atomic_attack, atomic_defense, mental_attack, mental_defense,
                                                    speed, critical_rate, critical_damage, armor_penetration, avoid, absorbs_damage, regenerate_vitality)
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + current_name + "','" + dir_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
                                "," + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense)
                                + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration)
                                + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + 
                                "," + str(list(variables.values())[0]) + ","+ str(list(variables.values())[1]) + "," + str(list(variables.values())[2]) + "," + str(list(variables.values())[3]) + "," + str(list(variables.values())[4]) + "," + str(list(variables.values())[5]) + "," + str(list(variables.values())[6])
                                + "," + str(list(variables.values())[7]) + "," + str(list(variables.values())[8]) + "," + str(list(variables.values())[9]) + "," + str(list(variables.values())[10]) + "," + str(list(variables.values())[11]) + ",'');")
                            id += 1
                        elif "MR" in dir_name:
                            health=1000000000
                            physical_attack=20000000
                            physical_defense=15000000
                            magical_attack=20000000
                            magical_defense=15000000
                            chemical_attack=20000000
                            chemical_defense=15000000
                            atomic_attack=20000000
                            atomic_defense=15000000
                            mental_attack=20000000
                            mental_defense=15000000
                            variables = {
                                'special_health': 1000000000,
                                'special_physical_attack': 20000000,
                                'special_physical_defense': 15000000,
                                'special_magical_attack': 20000000,
                                'special_magical_defense': 15000000,
                                'special_chemical_attack': 20000000,
                                'special_chemical_defense': 15000000,
                                'special_atomic_attack': 20000000,
                                'special_atomic_defense': 15000000,
                                'special_mental_attack': 20000000,
                                'special_mental_defense': 15000000,
                                'special_speed': 200000000
                            }
                            selected_variables = random.sample(list(variables.keys()), 2)
                            for var in variables:
                                if var not in selected_variables:
                                    variables[var] = 0
                            power = calculate_power(health, physical_attack, physical_defense, magical_attack, magical_defense, chemical_attack, chemical_defense, atomic_attack, atomic_defense, mental_attack, mental_defense,
                                                    speed, critical_rate, critical_damage, armor_penetration, avoid, absorbs_damage, regenerate_vitality)
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + current_name + "','" + dir_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
                                "," + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense)
                                + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration)
                                + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + 
                                "," + str(list(variables.values())[0]) + ","+ str(list(variables.values())[1]) + "," + str(list(variables.values())[2]) + "," + str(list(variables.values())[3]) + "," + str(list(variables.values())[4]) + "," + str(list(variables.values())[5]) + "," + str(list(variables.values())[6])
                                + "," + str(list(variables.values())[7]) + "," + str(list(variables.values())[8]) + "," + str(list(variables.values())[9]) + "," + str(list(variables.values())[10]) + "," + str(list(variables.values())[11]) + ",'');")
                            id += 1

def create_collaboration_database():
    cards_dir="Collaboration"
    card_list = []
    id=1
    card_name=""
    health=10000000
    physical_attack=2000000
    physical_defense=2000000
    magical_attack=2000000
    magical_defense=2000000
    chemical_attack=2000000
    chemical_defense=2000000
    atomic_attack=2000000
    atomic_defense=2000000
    mental_attack=2000000
    mental_defense=2000000
    per_health=40
    per_physical_attack=40
    per_physical_defense=40
    per_magical_attack=40
    per_magical_defense=40
    per_chemical_attack=40
    per_chemical_defense=40
    per_atomic_attack=40
    per_atomic_defense=40
    per_mental_attack=40
    per_mental_defense=40
    speed=1
    critical_rate=0
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="LG"
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into collaborations values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'');")
                id=id+1      

def create_cards_trade():
    cards_dir="Cards"
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        
                        
                        print("insert into card_trade values (" + str(id) + "," + str(7) + "," + str(200) + ");")

                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        
                        print("insert into card_trade values (" + str(id) + "," + str(7) + "," + str(500) + ");")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name,extension=os.path.splitext(file_name)
                        
                        print("insert into card_trade values (" + str(id) + "," + str(7) + "," + str(1000) + ");")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        
                        print("insert into card_trade values (" + str(id) + "," + str(7) + "," + str(2000) + ");")
                        id=id+1

def create_book_trade():
    cards_dir="Book"
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                
                    print("insert into book_trade values (" + str(id) + "," + str(37) + "," + str(2000) + ");")
                    id=id+1

def create_army_trade():
    cards_dir="Army"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    print("insert into army_trade values (" + str(id) + "," + str(48) + "," + str(2000) + ");")
                    id=id+1

def create_skills_trade():
    cards_dir="Skill"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    print("insert into skill_trade values (" + str(id) + "," + str(8) + "," + str(2000) + ");")
                    id=id+1

def create_collaboration_equipments_trade():
    cards_dir="CollborationEquipment"
    card_list = []
    id=1
    
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["MR","LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        
                        print("insert into collaboration_equipment_trade values (" + str(id) + "," + str(36) + "," + str(200) + ");")

                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        
                        print("insert into collaboration_equipment_trade values (" + str(id) + "," + str(36) + "," + str(500) + ");")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name,extension=os.path.splitext(file_name)
                        print("insert into collaboration_equipment_trade values (" + str(id) + "," + str(36) + "," + str(1000) + ");")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        print("insert into collaboration_equipment_trade values (" + str(id) + "," + str(36) + "," + str(2000) + ");")
                        id=id+1
            if "MR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        print("insert into collaboration_equipment_trade values (" + str(id) + "," + str(36) + "," + str(5000) + ");")
                        id=id+1

def create_pets_trade():
    cards_dir="Pet"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    print("insert into pet_trade values (" + str(id) + "," + str(51) + "," + str(5000) + ");")

                    id=id+1

def create_symbols_trade():
    cards_dir="Symbol"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            dir_name = os.path.basename(current_dir)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
            
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    
                    print("insert into symbol_trade values (" + str(id) + "," + str(52) + "," + str(2000) + ");")

                    id=id+1

def create_medals_trade():
    cards_dir="Medal"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
                
                print("insert into medal_trade values (" + str(id) + "," + str(36) + "," + str(2000) + ");")

                id=id+1

def create_achievements_trade():
    cards_dir="Achievement"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
                
                print("insert into achievement_trade values (" + str(id) + "," + str(33) + "," + str(2000) + ");")
                id=id+1

def create_titles_trade():
    cards_dir="Title"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")

                print("insert into title_trade values (" + str(id) + "," + str(6) + "," + str(2000) + ");")
                id=id+1

def create_borders_trade():
    cards_dir="Border"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                print("insert into border_trade values (" + str(id) + "," + str(35) + "," + str(2000) + ");")
                id=id+1

def create_items_trade():
    cards_dir="Item"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            current_dir =os.path.join(root,dir_name)
            for file_name in os.listdir(current_dir):
                if file_name.endswith(".jpg") or file_name.endswith("png"):
                    name, extension=os.path.splitext(file_name)
                    path=os.path.join(current_dir,file_name)
                    path=path.replace("\\","/")
                    name=name.replace("_"," ")
                    print("insert into item_trade values (" + str(id) + "," + str(35) + "," + str(10) + ");")
                    id=id+1

def create_equipments_trade():
    cards_dir="Equipment"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir = os.path.basename(root)
        current_name=""
        current_name = os.path.basename(os.path.dirname(root))
        for dir_name in dirs:
            current_dir = os.path.join(root, dir_name)
            for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith(".png"):
                        name, extension = os.path.splitext(file_name)
                        set1_folder_name = os.path.basename(os.path.dirname(current_dir))
                        name=name.replace("_"," ")
                        if "SR" in dir_name:
                            print("insert into equipment_trade values (" + str(id) + "," + str(47) + "," + str(200) + ");")
                            id += 1
                        elif "SSR" in dir_name:
                            print("insert into equipment_trade values (" + str(id) + "," + str(47) + "," + str(500) + ");")
                            id += 1
                        elif "UR" in dir_name:
                            print("insert into equipment_trade values (" + str(id) + "," + str(47) + "," + str(1000) + ");")
                            id += 1
                        elif "LG" in dir_name:
                            health=500000000
                            physical_attack=10000000
                            physical_defense=5000000
                            magical_attack=10000000
                            magical_defense=5000000
                            chemical_attack=10000000
                            chemical_defense=5000000
                            atomic_attack=10000000
                            atomic_defense=5000000
                            mental_attack=10000000
                            mental_defense=5000000
                            if "Souls_Equipment" in current_name or "Gem_Equipment" in current_name:
                                if "lv1" in name:
                                    health=50000000
                                    physical_attack=1000000
                                    physical_defense=500000
                                    magical_attack=1000000
                                    magical_defense=500000
                                    chemical_attack=1000000
                                    chemical_defense=500000
                                    atomic_attack=1000000
                                    atomic_defense=500000
                                    mental_attack=1000000
                                    mental_defense=500000
                                elif "lv2" in name:
                                    health=80000000
                                    physical_attack=3000000
                                    physical_defense=1500000
                                    magical_attack=3000000
                                    magical_defense=1500000
                                    chemical_attack=3000000
                                    chemical_defense=1500000
                                    atomic_attack=3000000
                                    atomic_defense=1500000
                                    mental_attack=3000000
                                    mental_defense=1500000
                                elif "lv3" in name:
                                    health=150000000
                                    physical_attack=5000000
                                    physical_defense=2500000
                                    magical_attack=5000000
                                    magical_defense=2500000
                                    chemical_attack=5000000
                                    chemical_defense=2500000
                                    atomic_attack=5000000
                                    atomic_defense=2500000
                                    mental_attack=5000000
                                    mental_defense=2500000
                                elif "lv4" in name:
                                    health=350000000
                                    physical_attack=8000000
                                    physical_defense=5000000
                                    magical_attack=8000000
                                    magical_defense=5000000
                                    chemical_attack=8000000
                                    chemical_defense=5000000
                                    atomic_attack=8000000
                                    atomic_defense=5000000
                                    mental_attack=8000000
                                    mental_defense=5000000
                                elif "lv5" in name:
                                    health=600000000
                                    physical_attack=10000000
                                    physical_defense=5000000
                                    magical_attack=10000000
                                    magical_defense=5000000
                                    chemical_attack=10000000
                                    chemical_defense=5000000
                                    atomic_attack=10000000
                                    atomic_defense=5000000
                                    mental_attack=10000000
                                    mental_defense=5000000
                                elif "lv6" in name:
                                    health=1000000000
                                    physical_attack=40000000
                                    physical_defense=25000000
                                    magical_attack=40000000
                                    magical_defense=25000000
                                    chemical_attack=40000000
                                    chemical_defense=25000000
                                    atomic_attack=40000000
                                    atomic_defense=25000000
                                    mental_attack=40000000
                                    mental_defense=25000000
                                elif "lv7" in name:
                                    health=5000000000
                                    physical_attack=90000000
                                    physical_defense=50000000
                                    magical_attack=90000000
                                    magical_defense=50000000
                                    chemical_attack=90000000
                                    chemical_defense=50000000
                                    atomic_attack=90000000
                                    atomic_defense=50000000
                                    mental_attack=90000000
                                    mental_defense=50000000
                            print("insert into equipment_trade values (" + str(id) + "," + str(47) + "," + str(2000) + ");")
                            id += 1
                        elif "MR" in dir_name:
                            print("insert into equipment_trade values (" + str(id) + "," + str(47) + "," + str(5000) + ");")
                            id += 1

def create_collaboration_trade():
    cards_dir="Collaboration"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                print("insert into collaboration_trade values (" + str(id) + "," + str(46) + "," + str(5000) + ");")
                id=id+1     

def create_monster_trade():
    cards_dir="Monster"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
                
                print("insert into monster_trade values (" + str(id) + "," + str(50) + "," + str(2000) + ");")

                id=id+1

def create_chest_equipment():
    cards_dir="Equipment"
    card_list = []
    id=1
    for root, dirs, files in os.walk(cards_dir):
        current_dir = os.path.basename(root)
        current_name=""
        current_name = os.path.basename(os.path.dirname(root))
        for dir_name in dirs:
            current_dir = os.path.join(root, dir_name)
            for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith(".png"):
                        name, extension = os.path.splitext(file_name)
                        set1_folder_name = os.path.basename(os.path.dirname(current_dir))
                        name=name.replace("_"," ")
                        if "Amnitus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(1) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(2) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(3) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(334) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(374) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Angelis_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(4) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(5) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(6) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(335) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(375) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Bellion_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(7) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(8) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(9) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(336) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(376) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Benzamin_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(10) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(11) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(12) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(337) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(377) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Celestial_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(13) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(14) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(15) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(338) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(378) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Ceverus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(16) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(17) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(18) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(339) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(379) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Delius_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(19) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(20) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(21) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(340) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(380) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Domitius_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(22) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(23) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(24) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(341) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(381) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Etherium_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(25) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(26) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(27) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(342) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(382) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Everlyn_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(28) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(29) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(30) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(343) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(383) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "EvilFruit_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(31) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(32) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(33) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(344) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(384) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Extra_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(34) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(35) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(36) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(345) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(385) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Faltus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(37) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(38) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(39) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(346) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(386) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Fealan_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(40) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(41) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(42) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(347) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(387) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Gamma_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(43) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(44) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(45) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(348) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(388) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Gem_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(46) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(47) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(48) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(349) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(389) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Hagoro_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(49) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(50) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(51) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(350) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(390) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Hakalite_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(52) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(53) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(54) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(351) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(391) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Heatherus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(55) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(56) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(57) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(352) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(392) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Ignis_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(58) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(59) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(60) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(353) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(393) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Ivitus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(61) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(62) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(63) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(354) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(394) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Karis_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(64) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(65) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(66) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(355) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(395) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Karmus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(67) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(68) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(69) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(356) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(396) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Lotus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(70) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(71) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(72) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(357) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(397) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Luminius_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(73) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(74) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(75) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(358) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(398) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Macus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(76) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(77) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(78) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(359) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(399) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Morganis_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(79) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(80) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(81) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(360) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(400) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Nimigazin_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(82) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(83) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(84) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(361) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(401) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Omonitus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(85) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(86) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(87) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(362) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(402) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Pet_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(88) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(89) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(90) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(363) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(403) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Qiyantus_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(91) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(92) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(93) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(364) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(404) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Rainbow_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(94) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(95) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(96) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(365) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(405) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Redvenger_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(97) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(98) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(99) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(366) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(406) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Retanic_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(100) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(101) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(102) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(367) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(407) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Souls_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(103) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(104) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(105) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(368) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(408) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Support_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(106) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(107) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(108) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(369) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(409) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Syncroharon_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(109) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(110) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(111) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(370) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(410) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Uni_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(112) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(113) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(114) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(371) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(411) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Zodiac_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(115) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(116) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(117) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(372) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(412) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        elif "Zpower_Equipment" in current_name:
                            print("insert into chest_equipment values (" + str(118) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(119) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(120) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(373) + "," + str(id) + "," + str(1) + ");")
                            print("insert into chest_equipment values (" + str(413) + "," + str(id) + "," + str(1) + ");")
                            id += 1
                        
def create_chest_card():
    cards_dir="Cards"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            if "SR" in dir_name:
                if "Adamas" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(283) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(284) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Avian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(285) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(286) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Barbarian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(287) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(288) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Cyttorak" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(289) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(290) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Dreizen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(291) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(292) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Etrigon" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(293) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(294) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Firimir" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(295) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(296) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Gennesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(297) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(298) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Hecarus" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(299) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(300) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Illonima" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(301) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(302) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Jaguar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(303) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(304) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Kryptonian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(305) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(306) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Lamania" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(307) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(308) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Marverick" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(309) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(310) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Nemesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(311) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(312) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Onyx" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(313) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(314) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Palladian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(315) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(316) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Quasar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(317) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(318) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Riverven" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(319) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(320) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Starroian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(321) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(322) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Terac" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(323) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(324) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Urius" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(325) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(326) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Vril" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(327) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(328) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Wyvern" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(329) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(330) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Xenomorph" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(331) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Yutogen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(332) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Zerath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(333) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                        
            if "SSR" in dir_name:
                if "Adamas" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(283) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(284) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Avian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(285) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(286) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Barbarian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(287) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(288) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Cyttorak" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(289) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(290) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Dreizen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(291) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(292) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Etrigon" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(293) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(294) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Firimir" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(295) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(296) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Gennesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(297) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(298) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Hecarus" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(299) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(300) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Illonima" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(301) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(302) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Jaguar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(303) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(304) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Kryptonian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(305) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(306) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Lamania" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(307) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(308) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Marverick" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(309) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(310) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Nemesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(311) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(312) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Onyx" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(313) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(314) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Palladian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(315) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(316) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Quasar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(317) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(318) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Riverven" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(319) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(320) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Starroian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(321) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(322) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Terac" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(323) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(324) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Urius" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(325) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(326) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Vril" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(327) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(328) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Wyvern" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(329) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(330) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Xenomorph" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(331) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Yutogen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(332) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Zerath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(333) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                        
            if "UR" in dir_name:
                if "Adamas" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(283) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(284) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Avian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(285) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(286) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Barbarian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(287) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(288) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Cyttorak" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(289) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(290) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Dreizen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(291) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(292) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Etrigon" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(293) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(294) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Firimir" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(295) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(296) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Gennesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(297) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(298) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Hecarus" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(299) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(300) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Illonima" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(301) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(302) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Jaguar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(303) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(304) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Kryptonian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(305) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(306) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Lamania" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(307) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(308) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Marverick" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(309) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(310) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Nemesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(311) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(312) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Onyx" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(313) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(314) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Palladian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(315) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(316) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Quasar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(317) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(318) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Riverven" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(319) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(320) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Starroian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(321) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(322) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Terac" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(323) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(324) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Urius" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(325) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(326) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Vril" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(327) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(328) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Wyvern" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(329) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(330) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Xenomorph" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(331) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Yutogen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(332) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Zerath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(333) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                        
            if "LG" in dir_name:
                if "Adamas" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(283) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(284) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Avian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(285) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(286) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Barbarian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(287) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(288) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Cyttorak" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(289) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(290) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Dreizen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(291) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(292) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Etrigon" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(293) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(294) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Firimir" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(295) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(296) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Gennesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(297) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(298) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Hecarus" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(299) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(300) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Illonima" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(301) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(302) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Jaguar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(303) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(304) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Kryptonian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(305) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(306) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Lamania" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(307) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(308) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Marverick" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(309) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(310) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Nemesis" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(311) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(312) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Onyx" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(313) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(314) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Palladian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(315) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(316) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Quasar" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(317) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(318) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Riverven" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(319) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(320) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Starroian" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(321) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(322) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Terac" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(323) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(324) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Urius" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(325) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(326) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Vril" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(327) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(328) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Wyvern" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(329) + "," + str(id) + "," + str(1) + ");")
                        print("insert into chest_card values (" + str(330) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Xenomorph" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(331) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Yutogen" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(332) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                elif "Zerath" in current_name:
                    current_dir =os.path.join(root,dir_name)
                    for file_name in os.listdir(current_dir):
                        print("insert into chest_card values (" + str(333) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
                                  
def create_chest_book():
    cards_dir="Book"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "ArtKnight_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(121) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(122) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(123) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "ETC_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(124) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(125) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(126) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Gemini_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(127) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(128) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(129) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Genshin_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(130) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(131) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(132) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Iterious_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(133) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(134) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(135) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Manhatan_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(136) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(137) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(138) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Monster_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(139) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(140) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(141) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "NA_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(142) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(143) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(144) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "OP_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(145) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(146) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(147) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Othellonia_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(148) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(149) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(150) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "SAO_book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(151) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(152) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(153) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Tanhagan_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(154) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(155) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(156) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Tensei_shitara_Slime_Datta_Ken_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(157) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(158) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(159) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Touhou_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(160) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(161) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(162) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Xenoraphine_Book" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_book values (" + str(163) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(164) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_book values (" + str(165) + "," + str(id) + "," + str(1) + ");")
                    id=id+1

def create_chest_army():
    cards_dir="Army"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Dark_Army" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_army values (" + str(166) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_army values (" + str(167) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_army values (" + str(168) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Light_Army" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_army values (" + str(169) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_army values (" + str(170) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_army values (" + str(171) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Void_Monster_Army" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_army values (" + str(172) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_army values (" + str(173) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_army values (" + str(174) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Void_Spell_Army" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_army values (" + str(175) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_army values (" + str(176) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_army values (" + str(177) + "," + str(id) + "," + str(1) + ");")
                    id=id+1

def create_chest_border():
    cards_dir="Border"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                print("insert into chest_border values (" + str(178) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_border values (" + str(179) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_border values (" + str(180) + "," + str(id) + "," + str(1) + ");")
                id=id+1

def create_chest_collaboration():
    cards_dir="Collaboration"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                print("insert into chest_collaboration values (" + str(181) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_collaboration values (" + str(182) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_collaboration values (" + str(183) + "," + str(id) + "," + str(1) + ");")
                id=id+1

def create_chest_currency():
    cards_dir="Currency"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                print("insert into chest_currency values (" + str(184) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_currency values (" + str(185) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_currency values (" + str(186) + "," + str(id) + "," + str(1) + ");")
                id=id+1

def create_chest_medal():
    cards_dir="Medal"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                print("insert into chest_medal values (" + str(187) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_medal values (" + str(188) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_medal values (" + str(189) + "," + str(id) + "," + str(1) + ");")
                id=id+1

def create_chest_monster():
    cards_dir="Monster"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                print("insert into chest_monster values (" + str(190) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_monster values (" + str(191) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_monster values (" + str(192) + "," + str(id) + "," + str(1) + ");")
                id=id+1

def create_chest_pet():
    cards_dir="Pet"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        
        # print(current_name)
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Legendary_Dragon" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_pet values (" + str(193) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(194) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(195) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Mysthic_Monster" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_pet values (" + str(196) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(197) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(198) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Naruto_Bijuu" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_pet values (" + str(199) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(200) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(201) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Naruto_Susanoo" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_pet values (" + str(202) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(203) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(204) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "One_Piece_Ship" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_pet values (" + str(205) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(206) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(207) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Prime_Monster" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_pet values (" + str(208) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(209) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(210) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Ultimate_Monster" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_pet values (" + str(211) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(212) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(213) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Xeras_Monster" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_pet values (" + str(214) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(215) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_pet values (" + str(216) + "," + str(id) + "," + str(1) + ");")
                    id=id+1

def create_chest_symbol():
    cards_dir="Symbol"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Symbol_1" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_symbol values (" + str(217) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(218) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(219) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Symbol_2" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_symbol values (" + str(220) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(221) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(222) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Symbol_3" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_symbol values (" + str(223) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(224) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(225) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Symbol_4" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_symbol values (" + str(226) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(227) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(228) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Symbol_5" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_symbol values (" + str(229) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(230) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_symbol values (" + str(231) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            
def create_chest_title():
    cards_dir="Title"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".jpg") or file_name.endswith("png"):
                name, extension=os.path.splitext(file_name)
                path=os.path.join(current_dir,file_name)
                path=path.replace("\\","/")
                name=name.replace("_"," ")
            
                print("insert into chest_title values (" + str(232) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_title values (" + str(233) + "," + str(id) + "," + str(1) + ");")
                print("insert into chest_title values (" + str(234) + "," + str(id) + "," + str(1) + ");")
                id=id+1

def create_chest_collaboration_equipment():
    cards_dir="CollborationEquipment"
    card_list = []
    id=1
    card_name=""
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=current_dir
        for dir_name in dirs:
            # print(current_name)  
            current_name = os.path.join(root, dir_name)          
            if "Berus_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(235) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(236) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(237) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Chibi_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(238) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(239) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(240) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "DragonBall_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(241) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(242) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(243) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Drasma_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(244) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(245) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(246) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "ETC_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(247) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(248) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(249) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Hirai_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(250) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(251) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(252) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Ikarus_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(253) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(254) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(255) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Kaisen_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(256) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(257) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(258) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Light_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(259) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(260) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(261) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Naruto_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(262) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(263) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(264) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Neko_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(265) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(266) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(267) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "OnePiece_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(268) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(269) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(270) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Rainbow_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(271) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(272) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(273) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Spirit_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(274) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(275) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(276) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Void_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(277) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(278) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(279) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
            elif "Xeras_Character" in current_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    print("insert into chest_collaboration_equipment values (" + str(280) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(281) + "," + str(id) + "," + str(1) + ");")
                    print("insert into chest_collaboration_equipment values (" + str(282) + "," + str(id) + "," + str(1) + ");")
                    id=id+1
# create_cards_database()
# create_books_database()
# create_skills_database()
# create_army_database()
# create_collaboration_equipments_database()
# create_equipments_database()
# create_monster_database()
# create_items_database()
# create_achievements_database()
# create_titles_database()
# create_currencies_database()
# create_pets_database()
# create_symbols_database()
# create_medals_database()
# create_borders_database()
# create_collaboration_database()

# create_cards_trade()
# create_book_trade()
# create_army_trade()
# create_skills_trade()
# create_collaboration_equipments_trade()
# create_pets_trade()
# create_symbols_trade()
# create_medals_trade()
# create_achievements_trade()
# create_titles_trade()
# create_borders_trade()
# create_items_trade()
# create_equipments_trade()
# create_collaboration_trade()
# create_monster_trade()

create_chest_equipment()
# create_chest_card()
# create_chest_book()
# create_chest_army()
# create_chest_border()
# create_chest_collaboration()
# create_chest_currency()
# create_chest_medal()
# create_chest_monster()
# create_chest_pet()
# create_chest_symbol()
# create_chest_title()
# create_chest_collaboration_equipment()