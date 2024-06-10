drop database alpha;
create database alpha;
use alpha;

create table cards(
	id int primary key,
    cardName varchar(100),
    cardImage varchar(100),
    rare varchar(100),
    type varchar(100),
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float,
    description varchar(255)
);

create table books(
	id int primary key,
    bookName varchar(100),
    bookImage varchar(100),
    rare varchar(100),
    type varchar(100),
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table army(
	id int primary key,
    armyName varchar(100),
    armyImage varchar(100),
    rare varchar(100),
    type varchar(100),
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table collaboration_equipments(
	id int primary key,
    collaborationEquipmentName varchar(100),
    collaborationEquipmentImage varchar(100),
    rare varchar(100),
    type varchar(100),
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table currency(
	id int primary key,
    currencyName varchar(100),
    currencyImage varchar(100)
);

create table equipments(
	id int primary key,
    equipmentName varchar(100),
    equipmentImage varchar(100),
    rare varchar(100),
    type varchar(100),
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table items(
	id int primary key,
    itemName varchar(100),
    itemImage varchar(100),
    type varchar(100),
    price double,
    description varchar(255)
);

create table achievements(
	id int primary key,
    achievementName varchar(100),
    achievementImage varchar(100),
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table medals(
	id int primary key,
    medalName varchar(100),
    medalImage varchar(100),
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table pets(
	id int primary key,
    petName varchar(100),
    petImage varchar(100),
    rare varchar(100),
    type varchar(100),
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table skills(
	id int primary key,
    skillName varchar(100),
    skillImage varchar(100),
    rare varchar(100),
    type varchar(100),
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table symbols(
	id int primary key,
    symbolName varchar(100),
    symbolImage varchar(100),
    rare varchar(100),
    type varchar(100),
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    description varchar(255)
);

create table titles(
	id int primary key,
    titleName varchar(100),
    titleImage varchar(100),
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double
);

create table user(
	id int primary key,
    username varchar(100),
    password varchar(100),
    name varchar(100),
    level int,
    experiment int,
    vip int,
    power double
);

create table limit_break(
	id int primary key,
    limitBreakName varchar(100),
    level int,
    step int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table awaken(
	id int primary key,
    awakenName varchar(100),
    level int,
    step int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table reincarnation(
	id int primary key,
    reincarnationName varchar(100),
    level int,
    step int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table potential(
	id int primary key,
    potentialName varchar(100),
    level int,
    step int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table user_cards(
	id int primary key,
    userId int,
    cardId int,
    level int,
    experiment int,
    star int,
    limitBreakId int,
    awakenId int,
    reincarnationId int,
    potentialId int,
    
    block boolean,
    
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table user_books(
	id int primary key,
    userId int,
    bookId int,
    level int,
    experiment int,
    star int,
    limitBreakId int,
    awakenId int,
    reincarnationId int,
    potentialId int,
    
    block boolean,
    
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table user_army(
	id int primary key,
    userId int,
    armyId int,
    level int,
    experiment int,
    star int,
    limitBreakId int,
    awakenId int,
    reincarnationId int,
    potentialId int,
    
    block boolean,
    
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table user_collaboration_equipments(
	id int primary key,
    userId int,
    collaborationEquipmentId int,
    level int,
    experiment int,
    star int,
    limitBreakId int,
    awakenId int,
    reincarnationId int,
    potentialId int,
    
    block boolean,
    
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table user_equipments(
	id int primary key,
    userId int,
    equipmentId int,
    level int,
    experiment int,
    star int,
    limitBreakId int,
    awakenId int,
    reincarnationId int,
    potentialId int,
    
    block boolean,
    
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table user_pets(
	id int primary key,
    userId int,
    petId int,
    level int,
    experiment int,
    star int,
    limitBreakId int,
    awakenId int,
    reincarnationId int,
    potentialId int,
    
    block boolean,
    
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table user_skill(
	id int primary key,
    userId int,
    skillId int,
    level int,
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float
);

create table user_items(
	id int primary key,
    itemId int,
    quantity int
);

create table user_achievements(
	id int primary key,
    achievementId int,
    userId int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double
);

create table user_medals(
	id int primary key,
    medalId int,
    userId int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double
);

create table user_symbols(
	id int primary key,
    symbolId int,
    userId int,
    rare varchar(100),
    type varchar(100),
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double
);

create table user_titles(
	id int primary key,
    titleId int,
    userId int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double
);

create table user_cards_gallery(
	id int primary key,
    userId int,
    cardId int,
    available boolean,
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float,
    allCardsId int
);

create table user_books_gallery(
	id int primary key,
    userId int,
    bookId int,
    available boolean,
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float,
    allBooksId int
);

create table user_army_gallery(
	id int primary key,
    userId int,
    armyId int,
    available boolean,
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float,
    allArmyId int
);

create table user_collaboration_equipments_gallery(
	id int primary key,
    userId int,
    collaborationEquipmentId int,
    available boolean,
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float,
    allCollaborationEquipmentsId int
);

create table user_equipments_gallery(
	id int primary key,
    userId int,
    equipmentId int,
	available boolean,
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float,
    allEquipmentId int
);

create table user_pets_gallery(
	id int primary key,
    userId int,
    petId int,
    available boolean,
    star int,
    health double,
    physicalAttack double,
    physicalDefense double,
    magicalAttack double,
    magicalDefense double,
    chemicalAttack double,
    chemicalDefense double,
    atomicAttack double,
    atomicDefense double,
    mentalAttack double,
    mentalDefense double,
    speed double,
    criticalDamage double,
    criticalRate double,
    armorPenetration double,
    avoid double,
    absorbsDamage double,
    regenerateVitality double,
    mana float,
    allPetsId int
);

create table equipment_gem(
	id int primary key,
    userId int,
    equipmentId1 int,
    gemId1 int,
    gemId2 int,
    gemId3 int,
    gemId4 int,
    gemId5 int,
    gemId6 int,
    gemId7 int,
    gemId8 int
);

create table equipment_amnitus(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int,
    equipmentGemId7 int,
    equipmentGemId8 int
);

create table equipment_angelis_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_angelis(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentAngelisAllId int
);

create table equipment_bellion(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_benzamin_set1(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_benzamin_set2(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_benzamin_set3(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_ceverus_set1(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_ceverus_set2(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_ceverus_set3(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_ceverus_set4(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_crystal_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_crystal(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentCrystalAll int
);

create table equipment_domitius(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int
);

create table equipment_ellis(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int,
    equipmentId5 int,
    equipmentId6 int,
    equipmentId7 int,
    equipmentId8 int
);

create table equipment_extra_set1(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_extra_set2(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_extra_set3(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_extra_set4(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_extra_set5(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_faltus_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_faltus(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentFaltusAll int
);

create table equipment_everlyn_set1(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_everlyn_set2(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_hagoro_set1(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int,
    equipmentId5 int,
    equipmentId6 int,
    equipmentId7 int,
    equipmentId8 int,
    equipmentId9 int,
    equipmentId10 int,
    equipmentId11 int,
    equipmentId12 int,
    equipmentId13 int,
    equipmentId14 int,
    equipmentId15 int,
    equipmentId16 int,
    equipmentId17 int,
    equipmentId18 int,
    equipmentId19 int,
    equipmentId20 int
);

create table equipment_hagoro_set2(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int,
    equipmentId5 int,
    equipmentId6 int,
    equipmentId7 int,
    equipmentId8 int
);

create table equipment_karis_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_karis(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentKarisAllId int
);

create table equipment_marcus(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_hakalite(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int
);

create table equipment_heatherus_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_heatherus(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentHeatherusAllId int
);

create table equipment_ignis_set1(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_ignis_set2(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_ignis_set3(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_ignis_set4(
	id int primary key,
    userId int,
	equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_ivitus(
	id int primary key,
    userId int,
     equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int
);

create table equipment_karmus(
	id int primary key,
    userId int,
	equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int
);

create table equipment_luminius_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_luminius(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentLuminiusAll int
);

create table equipment_morganis_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);
create table equipment_morganis(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentMorganisAllId int
);

create table equipment_nimigazin_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_nimigazin(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentNimigazinAll int
);

create table equipment_omonitus_set1(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_omonitus_set2(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int
);

create table equipment_omonitus_set3(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_omonitus_set4(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int,
    equipmentGemId7 int,
    equipmentGemId8 int
);

create table equipment_omonitus_set5(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int
);

create table equipment_omonitus_set6_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_omonitus_set6(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentOmonitusSet6All int
);

create table equipment_omonitus_set7(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int
);

create table equipment_pet(
	id int primary key,
    petId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int
);

create table equipment_qiyantus_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);
create table equipment_qiyantus(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentQiyantusAllId int
);

create table equipment_rainbow(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_retanic(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int
);

create table equipment_synrocharon_set1(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int,
    equipmentGemId7 int,
    equipmentGemId8 int
);

create table equipment_synrocharon_set2(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int,
    equipmentGemId7 int,
    equipmentGemId8 int
);

create table equipment_synrocharon_set3(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentGemId2 int,
    equipmentGemId3 int,
    equipmentGemId4 int,
    equipmentGemId5 int,
    equipmentGemId6 int,
    equipmentGemId7 int,
    equipmentGemId8 int
);

create table equipment_uni_all(
	id int primary key,
    userId int,
    
	allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);
create table equipment_uni(
	id int primary key,
    userId int,
    equipmentGemId1 int,
    equipmentUni int
);

create table equipment_zpower(
	id int primary key,
    userId int,
    equipmentId1 int,
    equipmentId2 int,
    equipmentId3 int,
    equipmentId4 int,
    equipmentId5 int,
    equipmentId6 int,
    equipmentId7 int,
    equipmentId8 int
);

create table all_army(
	id int primary key,
    userId int,
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table all_books(
	id int primary key,
    userId int,
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table all_cards(
	id int primary key,
    userId int,
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table all_collaboration_equipments(
	id int primary key,
    userId int,
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table all_equipments(
	id int primary key,
    userId int,
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table all_pets(
	id int primary key,
    userId int,
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table equipment_wearing(
	id int primary key,
    userId int,
    userCardId int,
	equipmentAmnitusId int,
    equipmentBellion int,
    equipmentBenzaminSet1Id int,
    equipmentBenzaminSet2Id int,
    equipmentBenzaminSet3Id int,
    equipmentCeverusSet1Id int,
    equipmentCeverusSet2Id int,
    equipmentCeverusSet3Id int,
    equipmentCeverusSet4Id int,
    equipmentDomitiusId int,
    equipmentEllisId int,
    equipmentExtraSet1Id int,
    equipmentExtraSet2Id int,
    equipmentExtraSet3Id int,
    equipmentExtraSet4Id int,
    equipmentExtraSet5Id int,
    equipmentEverlynSet1Id int,
    equipmentEverlynSet2Id int,
    equipmentMarcusId int,
    equipmentHakalite int,
    equipmentHagoroSet1Id int,
    equipmentHagoroSet2Id int,
    equipmentIgnisSet1Id int,
    equipmentIgnisSet2Id int,
    equipmentIgnisSet3Id int,
    equipmentIgnisSet4Id int,
    equipmentIvitusId int,
    equipmentKarmusId int,
    equipmentOmonitusSet1Id int,
    equipmentOmonitusSet2Id int,
    equipmentOmonitusSet3Id int,
    equipmentOmonitusSet4Id int,
    equipmentOmonitusSet5Id int,
    equipmentOmonitusSet6Id int,
    equipmentOmonitusSet7Id int,
    equipmentRainbowId int,
    equipmentRetanicId int,
    equipmentSynrocharonSet1Id int,
    equipmentSynrocharonSet2Id int,
    equipmentSynrocharonSet3Id int,
    equipmentZpowerId int,
    
    equipmentAngelisAllId int,
    equipmentCrystalAllId int,
    equipmentFaltusAllId int,
    equipmentKarisAllId int,
    equipmentHeatherusAllId int,
    equipmentLuminiusAllId int,
    equipmentMorganisAllId int,
    equipmentNimigazinAllId int,
    equipmentOmonitusSet6AllId int,
    equipmentQiyantusAllId int,
    equipmentUniAllId int,
    
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table fact_army(
	id int primary key,
    userId int,
    userArmyId int,
    
	equipmentWearingId int,
    power double,
    
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table fact_books(
	id int primary key,
    userId int,
    userBookId int,
    
	equipmentWearingId int,
    power double,
    
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table fact_pets(
	id int primary key,
    userId int,
    userCardId int,
    
    equipmentWearingId int,
	equipmentPetId int,
    power double,
    
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);

create table fact_cards(
	id int primary key,
    userId int,
    userCardId int,
    
    allArmyId int,
    allBooksId int,
    allCardsId int,
    allCollaborationEquipmentsId int,
    allEquipmentsId int,
    allPets int,
	equipmentWearingId int,
    power double,
    
    allHealth double,
    allPhysicalAttack double,
    allPhysicalDefense double,
    allMagicalAttack double,
    allMagicalDefense double,
    allChemicalAttack double,
    allChemicalDefense double,
    allAtomicAttack double,
    allAtomicDefense double,
    allMentalAttack double,
    allMentalDefense double,
    allSpeed double,
    allCriticalDamage double,
    allCriticalRate double,
    allArmorPenetration double,
    allAvoid double,
    allAbsorbsDamage double,
    allRegenerateVitality double,
    allMana float
);