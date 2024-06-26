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
	id int primary key,
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
    
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_cards_rank(
	id int primary key,
    user_id int,
    user_card_id int,
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
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (user_card_id) REFERENCES user_cards(id)
);

create table user_books(
	id int primary key,
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
    
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_books_rank(
	id int primary key,
    user_id int,
    user_book_id int,
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
    
    FOREIGN KEY (user_book_id) REFERENCES user_books(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_army(
	id int primary key,
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
    
    FOREIGN KEY (army_id) REFERENCES army(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_army_rank(
	id int primary key,
    user_id int,
    user_army_id int,
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
    
    FOREIGN KEY (user_army_id) REFERENCES user_army(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_collaboration_equipments(
	id int primary key,
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
    
    FOREIGN KEY (collaboration_equipment_id) REFERENCES collaboration_equipments(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_collaboration_equipments_rank(
	id int primary key,
    user_id int,
    user_collaboration_equipment_id int,
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
    
    FOREIGN KEY (user_collaboration_equipment_id) REFERENCES user_collaboration_equipments(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_equipments(
	id int primary key,
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
    
    full_equipment_id int,
    
    FOREIGN KEY (equipment_id) REFERENCES equipments(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_equipments_rank(
	id int primary key,
    user_id int,
    user_equipment_id int,
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
    
    FOREIGN KEY (user_equipment_id) REFERENCES user_equipments(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_pets(
	id int primary key,
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
    
    FOREIGN KEY (pet_id) REFERENCES pets(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_pets_rank(
	id int primary key,
    user_id int,
    user_pet_id int,
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
    
    FOREIGN KEY (user_pet_id) REFERENCES user_pets(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_skill(
	id int primary key,
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
    
    FOREIGN KEY (skill_id) REFERENCES skills(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_items(
	id int primary key,
    user_id int,
    item_id int,
    quantity int,
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table user_achievements(
	id int primary key,
    achievement_id int,
    user_id int,
    
    FOREIGN KEY (achievement_id) REFERENCES achievements(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_medals(
	id int primary key,
    medal_id int,
    user_id int,
    
    FOREIGN KEY (medal_id) REFERENCES medals(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_symbols(
	id int primary key,
    symbol_id int,
    user_id int,
    
    FOREIGN KEY (symbol_id) REFERENCES symbols(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_titles(
	id int primary key,
    title_id int,
    user_id int,
    
    FOREIGN KEY (title_id) REFERENCES titles(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_borders(
	id int primary key,
    border_id int,
    user_id int,
    
    FOREIGN KEY (border_id) REFERENCES borders(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_collaborations(
	id int primary key,
    collaboration_id int,
    user_id int,
    
    FOREIGN KEY (collaboration_id) REFERENCES collaborations(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table user_cards_gallery(
	id int primary key,
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
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (card_id) REFERENCES cards(id)
);

create table user_books_gallery(
	id int primary key,
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
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

create table user_army_gallery(
	id int primary key,
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
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (army_id) REFERENCES army(id)
);

create table user_collaboration_equipments_gallery(
	id int primary key,
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
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (collaboration_equipment_id) REFERENCES collaboration_equipments(id)
);

create table user_equipments_gallery(
	id int primary key,
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
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (equipment_id) REFERENCES equipments(id)
);

create table user_pets_gallery(
	id int primary key,
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
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

create table user_currency(
	id int primary key,
    user_id int,
    currency_id int,
    quantity double,
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);

create table mail(
	id int primary key,
    user_id int,
    item_id int,
    type varchar(100),
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

create table full_equipment(
	id int primary key,
    userId int,
    equipmentId int,
    extra_equipment_id int,
    
    fact_army_id int,
    fact_book_id int,
    fact_pet_id int,
    fact_card_id int,
    
    FOREIGN KEY (equipmentId) REFERENCES user_equipments(id),
    FOREIGN KEY (extra_equipment_id) REFERENCES user_equipments(id)
);

create table fact_army(
	id int primary key,
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
    
    FOREIGN KEY (user_army_id) REFERENCES user_army(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table fact_books(
	id int primary key,
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
    
     FOREIGN KEY (user_book_id) REFERENCES user_books(id),
     FOREIGN KEY (user_id) REFERENCES users(id)
);

create table fact_pets(
	id int primary key,
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
    
    FOREIGN KEY (user_pet_id) REFERENCES user_pets(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table fact_cards(
	id int primary key,
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
    
    FOREIGN KEY (user_card_id) REFERENCES user_cards(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

ALTER TABLE full_equipment
ADD CONSTRAINT fk_fact_army FOREIGN KEY (fact_army_id) REFERENCES fact_army(id),
ADD CONSTRAINT fk_fact_book FOREIGN KEY (fact_book_id) REFERENCES fact_books(id),
ADD CONSTRAINT fk_fact_pet FOREIGN KEY (fact_pet_id) REFERENCES fact_pets(id),
ADD CONSTRAINT fk_fact_card FOREIGN KEY (fact_card_id) REFERENCES fact_cards(id);

create table cards_skills(
	id int primary key,
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
    
    FOREIGN KEY (fact_card_id) REFERENCES fact_cards(id),
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);

create table teams(
	id int primary key,
    user_id int,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table positions(
	id int primary key,
    team_id int,
    type varchar(255),
    
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

create table slots(
	id int primary key,
    fact_card_id int,
    position_id int,
    
    FOREIGN KEY (fact_card_id) REFERENCES fact_cards(id),
    FOREIGN KEY (position_id) REFERENCES positions(id)
);

create table user_transaction(
	id int primary key,
    object_type varchar(255),
    army_id int,
    book_id int,
    card_id int,
    collaboration_equipment_id int,
    equipment_id int,
    skill_id int,
    item_id int,
    medal_id int,
    pet_id int,
    symbol_id int,
    title_id int,
    currency_id int,
    
    FOREIGN KEY (army_id) REFERENCES army(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (collaboration_equipment_id) REFERENCES collaboration_equipments(id),
    FOREIGN KEY (equipment_id) REFERENCES equipments(id),
    FOREIGN KEY (item_id) REFERENCES items(id),
    FOREIGN KEY (medal_id) REFERENCES medals(id),
    FOREIGN KEY (pet_id) REFERENCES pets(id),
    FOREIGN KEY (symbol_id) REFERENCES symbols(id),
    FOREIGN KEY (title_id) REFERENCES titles(id),
    FOREIGN KEY (currency_id) REFERENCES currency(id)
);