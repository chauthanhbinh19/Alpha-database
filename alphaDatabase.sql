drop database alpha;
create database alpha;
use alpha;

create table cards(
	id int primary key,
    cardName varchar(255),
    cardImage varchar(255),
    rare varchar(100),
    type varchar(100),
    star int,
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    description varchar(255)
);

create table books(
	id int primary key,
    bookName varchar(255),
    bookImage varchar(255),
    rare varchar(100),
    type varchar(100),
    star int,
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    description varchar(255)
);

create table army(
	id int primary key,
    armyName varchar(255),
    armyImage varchar(255),
    rare varchar(100),
    type varchar(100),
    star int,
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    description varchar(255)
);

create table collaboration_equipments(
	id int primary key,
    collaborationEquipmentName varchar(255),
    collaborationEquipmentImage varchar(255),
    rare varchar(100),
    type varchar(100),
    star int,
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    description varchar(255)
);

create table monsters(
	id int primary key,
    monsterName varchar(255),
    monsterImage varchar(255),
    rare varchar(100),
    type varchar(100),
    star int,
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    description varchar(255)
);

create table currency(
	id int primary key,
    currencyName varchar(255),
    currencyImage varchar(255)
);

create table equipments(
	id int primary key,
    equipmentName varchar(255),
    equipmentImage varchar(255),
    rare varchar(100),
    type varchar(100),
    equipmentSet varchar(100),
    star int,
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,

    special_health double,
    special_physical_attack double,
    special_physical_defense double,
    special_magical_attack double,
    special_magical_defense double,
    special_chemical_attack double,
    special_chemical_defense double,
    special_atomic_attack double,
    special_atomic_defense double,
    special_mental_attack double,
    special_mental_defense double,
    special_speed double,

    description varchar(255)
);

create table items(
	id int primary key,
    itemName varchar(255),
    itemImage varchar(255),
    type varchar(100),
    price double,
    description varchar(255)
);

create table achievements(
	id int primary key,
    achievementName varchar(255),
    achievementImage varchar(255),
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    description varchar(255)
);

create table medals(
	id int primary key,
    medalName varchar(255),
    medalImage varchar(255),
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    description varchar(255)
);

create table pets(
	id int primary key,
    petName varchar(255),
    petImage varchar(255),
    rare varchar(100),
    type varchar(100),
    star int,
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    description varchar(255)
);

create table skills(
	id int primary key,
    skillName varchar(255),
    skillImage varchar(255),
    rare varchar(100),
    type varchar(100),
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    description varchar(255)
);

create table symbols(
	id int primary key,
    symbolName varchar(255),
    symbolImage varchar(255),
    type varchar(100),
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    description varchar(255)
);

create table titles(
	id int primary key,
    titleName varchar(255),
    titleImage varchar(255),
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    description varchar(255)
);

create table borders(
	id int primary key,
    borderName varchar(255),
    borderImage varchar(255),
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    description varchar(255)
);

create table collaborations (
	id int primary key,
    collaborationName varchar(255),
    collaborationImage varchar(255),
    power double,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    description varchar(255)
);

create table users(
	id int primary key,
    username varchar(100),
    password varchar(100),
    name varchar(100),
    level int,
    experiment int,
    vip int,
    power double
);

create table user_cards(
    user_id int,
    card_id int,
    level int,
    experiment int,
    star int,
    
    block boolean,
    quantity int,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    PRIMARY KEY(user_id,card_id),
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_cards_rank(
    user_id int,
    user_card_id int,
    rank_id int,
    rank_type varchar(255),
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,

	percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,user_card_id, rank_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (user_card_id) REFERENCES user_cards(card_id)
);

create table user_books(
    user_id int,
    book_id int,
    level int,
    experiment int,
    star int,
    
    block boolean,
    quantity int,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    PRIMARY KEY(user_id,book_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_books_rank(
    user_id int,
    user_book_id int,
    rank_id int,
    rank_type varchar(255),
    
	health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,

	percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,user_book_id,rank_id),
    FOREIGN KEY (user_book_id) REFERENCES user_books(book_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_monsters(
    user_id int,
    monster_id int,
    level int,
    experiment int,
    star int,
    
    block boolean,
    quantity int,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    PRIMARY KEY(user_id,monster_id),
    FOREIGN KEY (monster_id) REFERENCES monsters(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_monsters_rank(
    user_id int,
    user_monster_id int,
    rank_id int,
    rank_type varchar(255),
    
	health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,

	percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,user_monster_id,rank_id),
    FOREIGN KEY (user_monster_id) REFERENCES user_monsters(monster_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_army(
    user_id int,
    army_id int,
    level int,
    experiment int,
    star int,
    
    block boolean,
    quantity int,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    PRIMARY KEY(user_id,army_id),
    FOREIGN KEY (army_id) REFERENCES army(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_army_rank(
    user_id int,
    user_army_id int,
    rank_id int,
    rank_type varchar(255),
    
	health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,

	percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,user_army_id,rank_id),
    FOREIGN KEY (user_army_id) REFERENCES user_army(army_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_collaboration_equipments(
    user_id int,
    collaboration_equipment_id int,
    level int,
    experiment int,
    star int,
    
    block boolean,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    PRIMARY KEY(user_id,collaboration_equipment_id),
    FOREIGN KEY (collaboration_equipment_id) REFERENCES collaboration_equipments(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_collaboration_equipments_rank(
    user_id int,
    user_collaboration_equipment_id int,
    rank_id int,
    rank_type varchar(255),
    
	health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,

	percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,user_collaboration_equipment_id, rank_id),
    FOREIGN KEY (user_collaboration_equipment_id) REFERENCES user_collaboration_equipments(collaboration_equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_equipments(
    user_id int,
    equipment_id int,
    level int,
    experiment int,
    star int,
    
    block boolean,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
        
    PRIMARY KEY(user_id,equipment_id),
    FOREIGN KEY (equipment_id) REFERENCES equipments(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_equipments_rank(
    user_id int,
    user_equipment_id int,
    rank_id int,
    rank_type varchar(255),
    
	health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,

	percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,user_equipment_id, rank_id),
    FOREIGN KEY (user_equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_pets(
    user_id int,
    pet_id int,
    level int,
    experiment int,
    star int,
    
    block boolean,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    PRIMARY KEY(user_id,pet_id),
    FOREIGN KEY (pet_id) REFERENCES pets(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_pets_rank(
    user_id int,
    user_pet_id int,
    rank_id int,
    rank_type varchar(255),
    
	health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,

	percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,user_pet_id, rank_id),
    FOREIGN KEY (user_pet_id) REFERENCES user_pets(pet_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_skill(
    user_id int,
    skill_id int,
    level int,
    star int,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    PRIMARY KEY(user_id,skill_id),
    FOREIGN KEY (skill_id) REFERENCES skills(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_items(
    user_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(user_id,item_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table user_achievements(
    user_id int,
    achievement_id int,
    
    PRIMARY KEY(user_id,achievement_id),
    FOREIGN KEY (achievement_id) REFERENCES achievements(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_medals(
    user_id int,
    medal_id int,
    
    PRIMARY KEY(user_id,medal_id),
    FOREIGN KEY (medal_id) REFERENCES medals(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_symbols(
    user_id int,
    symbol_id int,
    
    PRIMARY KEY(user_id,symbol_id),
    FOREIGN KEY (symbol_id) REFERENCES symbols(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_titles(
    user_id int,
    title_id int,
    
    PRIMARY KEY(user_id,title_id),
    FOREIGN KEY (title_id) REFERENCES titles(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_borders(
    user_id int,
    border_id int,
    
    PRIMARY KEY(user_id,border_id),
    FOREIGN KEY (border_id) REFERENCES borders(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_collaborations(
    user_id int,
    collaboration_id int,
    
    PRIMARY KEY(user_id,collaboration_id),
    FOREIGN KEY (collaboration_id) REFERENCES collaborations(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table cards_gallery(
    user_id int,
    card_id int,
    
    available boolean,
    star int,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,card_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (card_id) REFERENCES cards(id)
);

create table books_gallery(
    user_id int,
    book_id int,
    
    available boolean,
    star int,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
     PRIMARY KEY(user_id,book_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

create table monsters_gallery(
    user_id int,
    monster_id int,
    
    available boolean,
    star int,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,monster_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (monster_id) REFERENCES monsters(id)
);
create table army_gallery(
    user_id int,
    army_id int,
    
    available boolean,
    star int,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,army_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (army_id) REFERENCES army(id)
);

create table collaboration_equipments_gallery(
    user_id int,
    collaboration_equipment_id int,
    
    available boolean,
    star int,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,collaboration_equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (collaboration_equipment_id) REFERENCES collaboration_equipments(id)
);

create table equipments_gallery(
    user_id int,
    equipment_id int,
    
	available boolean,
    star int,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (equipment_id) REFERENCES equipments(id)
);

create table pets_gallery(
    user_id int,
    pet_id int,
    
    available boolean,
    star int,
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    percent_all_health double,
    percent_all_physical_attack double,
    percent_all_physical_defense double,
    percent_all_magical_attack double,
    percent_all_magical_defense double,
    percent_all_chemical_attack double,
    percent_all_chemical_defense double,
    percent_all_atomic_attack double,
    percent_all_atomic_defense double,
    percent_all_mental_attack double,
    percent_all_mental_defense double,
    
    PRIMARY KEY(user_id,pet_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

create table user_currency(
    user_id int,
    currency_id int,
    quantity double,
    
    PRIMARY KEY(user_id,currency_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table mail(
	id int primary key,
    user_id int,
    item_id int,
    mail_date DATETIME,
    type varchar(100),
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);


create table fact_army(
    user_id int,
    user_army_id int,
    
    power double,
    
    all_health double,
    all_physical_attack double,
    all_physical_defense double,
    all_magical_attack double,
    all_magical_defense double,
    all_chemical_attack double,
    all_chemical_defense double,
    all_atomic_attack double,
    all_atomic_defense double,
    all_mental_attack double,
    all_mental_defense double,
    all_speed double,
    all_critical_damage double,
    all_critical_rate double,
    all_armor_penetration double,
    all_avoid double,
    all_absorbs_damage double,
    all_regenerate_vitality double,
    all_mana float,
    
    PRIMARY KEY(user_id,user_army_id),
    FOREIGN KEY (user_army_id) REFERENCES user_army(army_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table fact_books(
    user_id int,
    user_book_id int,
    
    power double,
    
    all_health double,
    all_physical_attack double,
    all_physical_defense double,
    all_magical_attack double,
    all_magical_defense double,
    all_chemical_attack double,
    all_chemical_defense double,
    all_atomic_attack double,
    all_atomic_defense double,
    all_mental_attack double,
    all_mental_defense double,
    all_speed double,
    all_critical_damage double,
    all_critical_rate double,
    all_armor_penetration double,
    all_avoid double,
    all_absorbs_damage double,
    all_regenerate_vitality double,
    all_mana float,
    
    PRIMARY KEY(user_id,user_book_id),
    FOREIGN KEY (user_book_id) REFERENCES user_books(book_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table fact_monsters(
    user_id int,
    user_monster_id int,
    
    power double,
    
    all_health double,
    all_physical_attack double,
    all_physical_defense double,
    all_magical_attack double,
    all_magical_defense double,
    all_chemical_attack double,
    all_chemical_defense double,
    all_atomic_attack double,
    all_atomic_defense double,
    all_mental_attack double,
    all_mental_defense double,
    all_speed double,
    all_critical_damage double,
    all_critical_rate double,
    all_armor_penetration double,
    all_avoid double,
    all_absorbs_damage double,
    all_regenerate_vitality double,
    all_mana float,
    
    PRIMARY KEY(user_id,user_monster_id),
    FOREIGN KEY (user_monster_id) REFERENCES user_monsters(monster_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table fact_pets(
    user_id int,
    user_pet_id int,
    
    power double,
    
    all_health double,
    all_physical_attack double,
    all_physical_defense double,
    all_magical_attack double,
    all_magical_defense double,
    all_chemical_attack double,
    all_chemical_defense double,
    all_atomic_attack double,
    all_atomic_defense double,
    all_mental_attack double,
    all_mental_defense double,
    all_speed double,
    all_critical_damage double,
    all_critical_rate double,
    all_armor_penetration double,
    all_avoid double,
    all_absorbs_damage double,
    all_regenerate_vitality double,
    all_mana float,
    
    PRIMARY KEY(user_id,user_pet_id),
    FOREIGN KEY (user_pet_id) REFERENCES user_pets(pet_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table fact_cards(
    user_id int,
    user_card_id int,
    
    power double,
    
    all_health double,
    all_physical_attack double,
    all_physical_defense double,
    all_magical_attack double,
    all_magical_defense double,
    all_chemical_attack double,
    all_chemical_defense double,
    all_atomic_attack double,
    all_atomic_defense double,
    all_mental_attack double,
    all_mental_defense double,
    all_speed double,
    all_critical_damage double,
    all_critical_rate double,
    all_armor_penetration double,
    all_avoid double,
    all_absorbs_damage double,
    all_regenerate_vitality double,
    all_mana float,
    
    PRIMARY KEY(user_id,user_card_id),
    FOREIGN KEY (user_card_id) REFERENCES user_cards(card_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table card_equipment(
    user_id int,
    fact_card_id int,
    equipment_id int,

    PRIMARY KEY(user_id,fact_card_id,equipment_id),
    FOREIGN KEY (equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (fact_card_id) REFERENCES fact_cards(user_card_id)
);

create table army_equipment(
    user_id int,
    fact_army_id int,
    equipment_id int,

    PRIMARY KEY(user_id,fact_army_id, equipment_id),
    FOREIGN KEY (equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (fact_army_id) REFERENCES fact_army(user_army_id)
);

create table book_equipment(
    user_id int,
    fact_book_id int,
    equipment_id int,

    PRIMARY KEY(user_id,fact_book_id,equipment_id),
    FOREIGN KEY (equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (fact_book_id) REFERENCES fact_books(user_book_id)
);

create table pet_equipment(
    user_id int,
    fact_pet_id int,
    equipment_id int,

    PRIMARY KEY(user_id,fact_pet_id,equipment_id),
    FOREIGN KEY (equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (fact_pet_id) REFERENCES fact_pets(user_pet_id)
);

create table monster_equipment(
    user_id int,
    fact_monster_id int,
    equipment_id int,

    PRIMARY KEY(user_id,fact_monster_id,equipment_id),
    FOREIGN KEY (equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (fact_monster_id) REFERENCES fact_monsters(user_monster_id)
);

create table card_equipment_details(
    user_id int,
    fact_card_id int,
    equipment_id int,
    extra_equipment_id int,
    
    PRIMARY KEY(user_id,fact_card_id,equipment_id,extra_equipment_id),
    FOREIGN KEY (extra_equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (equipment_id) REFERENCES card_equipment(equipment_id),
    FOREIGN KEY (fact_card_id) REFERENCES fact_cards(user_card_id)
);

create table army_equipment_details(
    user_id int,
    fact_army_id int,
    equipment_id int,
    extra_equipment_id int,
    
    PRIMARY KEY(user_id,fact_army_id,equipment_id,extra_equipment_id),
    FOREIGN KEY (extra_equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (equipment_id) REFERENCES army_equipment(equipment_id),
    FOREIGN KEY (fact_army_id) REFERENCES fact_army(user_army_id)
);

create table book_equipment_details(
    user_id int,
    fact_book_id int,
    equipment_id int,
    extra_equipment_id int,
    
    PRIMARY KEY(user_id,fact_book_id,equipment_id,extra_equipment_id),
    FOREIGN KEY (extra_equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (equipment_id) REFERENCES book_equipment(equipment_id),
    FOREIGN KEY (fact_book_id) REFERENCES fact_books(user_book_id)
);

create table pet_equipment_details(
    user_id int,
    fact_pet_id int,
    equipment_id int,
    extra_equipment_id int,
    
    PRIMARY KEY(user_id,fact_pet_id,equipment_id,extra_equipment_id),
    FOREIGN KEY (extra_equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (equipment_id) REFERENCES pet_equipment(equipment_id),
    FOREIGN KEY (fact_pet_id) REFERENCES fact_pets(user_pet_id)
);

create table monster_equipment_details(
    user_id int,
    fact_monster_id int,
    equipment_id int,
    extra_equipment_id int,
    
    PRIMARY KEY(user_id,fact_monster_id,equipment_id,extra_equipment_id),
    FOREIGN KEY (extra_equipment_id) REFERENCES user_equipments(equipment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (equipment_id) REFERENCES monster_equipment(equipment_id),
    FOREIGN KEY (fact_monster_id) REFERENCES fact_monsters(user_monster_id)
);

create table cards_skills(
    user_id int,
    fact_card_id int,
    skill_id int,
    level int,
    
    health double,
    physical_attack double,
    physical_defense double,
    magical_attack double,
    magical_defense double,
    chemical_attack double,
    chemical_defense double,
    atomic_attack double,
    atomic_defense double,
    mental_attack double,
    mental_defense double,
    speed double,
    critical_damage double,
    critical_rate double,
    armor_penetration double,
    avoid double,
    absorbs_damage double,
    regenerate_vitality double,
    mana float,
    
    PRIMARY KEY(user_id,fact_card_id,skill_id),
    FOREIGN KEY (fact_card_id) REFERENCES fact_cards(user_card_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);

create table teams(
    user_id int,
    fact_card_id int,
    position int,
    role varchar(255),

    FOREIGN KEY (fact_card_id) REFERENCES fact_cards(user_card_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table army_trade(
    army_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(army_id, currency_id),
    FOREIGN KEY (army_id) REFERENCES army(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table book_trade(
    book_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(book_id, currency_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table border_trade(
    border_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(border_id, currency_id),
    FOREIGN KEY (border_id) REFERENCES borders(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table card_trade(
    card_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(card_id, currency_id),
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table collaboration_trade(
    collaboration_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(collaboration_id, currency_id),
    FOREIGN KEY (collaboration_id) REFERENCES collaborations(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table collaboration_equipment_trade(
    collaboration_equipment_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(collaboration_equipment_id, currency_id),
    FOREIGN KEY (collaboration_equipment_id) REFERENCES collaboration_equipments(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table equipment_trade(
    equipment_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(equipment_id, currency_id),
    FOREIGN KEY (equipment_id) REFERENCES equipments(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table skill_trade(
    skill_id int,
    currency_id int,
	price double,
    
    PRIMARY KEY(skill_id, currency_id),
    FOREIGN KEY (skill_id) REFERENCES skills(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table item_trade(
    item_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(item_id, currency_id),
    FOREIGN KEY (item_id) REFERENCES items(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table medal_trade(
    medal_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(medal_id, currency_id),
    FOREIGN KEY (medal_id) REFERENCES medals(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table pet_trade(
    pet_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(pet_id, currency_id),
    FOREIGN KEY (pet_id) REFERENCES pets(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table symbol_trade(
    symbol_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(symbol_id, currency_id),
    FOREIGN KEY (symbol_id) REFERENCES symbols(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table title_trade(
    title_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(title_id, currency_id),
    FOREIGN KEY (title_id) REFERENCES titles(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table monster_trade(
    monster_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(monster_id, currency_id),
    FOREIGN KEY (monster_id) REFERENCES monsters(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table achievement_trade(
    achievement_id int,
    currency_id int,
    price double,
    
    PRIMARY KEY(achievement_id, currency_id),
    FOREIGN KEY (achievement_id) REFERENCES achievements(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table chest_equipment(
    equipment_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(equipment_id, item_id),
    FOREIGN KEY (equipment_id) REFERENCES equipments(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_card(
    card_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(card_id, item_id),
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_book(
    book_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(book_id, item_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_army(
    army_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(army_id, item_id),
    FOREIGN KEY (army_id) REFERENCES army(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_border(
    border_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(border_id, item_id),
    FOREIGN KEY (border_id) REFERENCES borders(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_collaboration(
    collaboration_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(collaboration_id, item_id),
    FOREIGN KEY (collaboration_id) REFERENCES collaborations(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_collaboration_equipment(
    collaboration_equipment_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(collaboration_equipment_id, item_id),
    FOREIGN KEY (collaboration_equipment_id) REFERENCES collaboration_equipments(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_currency(
    
    currency_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(currency_id, item_id),
    FOREIGN KEY (currency_id) REFERENCES currency(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_item(
    material_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(material_id, item_id),
    FOREIGN KEY (material_id) REFERENCES items(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_medal(
    medal_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(medal_id, item_id),
    FOREIGN KEY (medal_id) REFERENCES medals(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_monster(
    monster_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(monster_id, item_id),
    FOREIGN KEY (monster_id) REFERENCES monsters(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_pet(
    pet_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(pet_id, item_id),
    FOREIGN KEY (pet_id) REFERENCES pets(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_skill(
    skill_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(skill_id, item_id),
    FOREIGN KEY (skill_id) REFERENCES skills(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_symbol(
    symbol_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(symbol_id, item_id),
    FOREIGN KEY (symbol_id) REFERENCES symbols(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table chest_title(
    title_id int,
    item_id int,
    quantity int,
    
    PRIMARY KEY(title_id, item_id),
    FOREIGN KEY (title_id) REFERENCES titles(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);