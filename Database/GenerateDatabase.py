import json
import os
import random
import math

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
def get_story(character):
    stories = {
        "Adamas": [
            "In the realm of Adamas, strange phenomena began to plague the land. Reality itself appeared to unravel, causing chaos and confusion among the inhabitants. Lyra, a skilled mage, discovered ancient texts that spoke of the Fractured Shard, an artifact believed to mend the very fabric of reality. As Lyra gathered a band of brave allies, they journeyed through treacherous terrains filled with warped creatures and distorted landscapes. Each challenge tested their resolve, but the greatest threat emerged when they inadvertently awakened a malevolent entity. This ancient evil sought to consume the world, forcing the group to unite their powers in an epic confrontation. In the end, their combined strength and newfound friendships were the key to restoring balance to the realm.",
            "At the heart of Adamas, the excitement of the Ascendant Duel filled the air. Aelar and Caelum, two champions with extraordinary powers, faced off in a battle that would determine the fate of their faction. As the duel unfolded, their respective card abilities created dazzling displays of magic. However, the duel took an unexpected turn when both champions discovered a dark sorcerer manipulating events from the shadows, aiming to exploit their rivalry. Realizing the true threat lay beyond their personal ambitions, Aelar and Caelum joined forces. Their collaboration led to a thrilling chase and a climactic showdown against the sorcerer, teaching them that unity and trust were far more powerful than rivalry.",
            "During an expedition to ancient ruins, Selene, a young mage, stumbled upon a set of enchanted stones. Each stone held the power to whisper forgotten tales, revealing secrets of the past. Intrigued by the mysteries they contained, Selene dedicated herself to unraveling their significance. As she delved deeper, she uncovered a prophecy foretelling the return of a dark force, one that had been banished long ago. As ominous signs began to appear in her village, Selene rallied a group of allies. Together, they set out to decipher the prophecy and confront the looming threat. Their journey tested their courage and trust, culminating in a showdown against the dark force that would determine the fate of their world.",
            "When the Guardian Spirits of Adamas, revered protectors of the realm, began to vanish mysteriously, panic gripped the faction. The leaders convened an emergency council and reluctantly forged an alliance with a rival faction known for their brutal tactics. This unprecedented collaboration took them into the Forbidden Forest, where they discovered a dark ritual orchestrated by a vengeful sorceress. Determined to reclaim their Guardians, the allied factions faced fierce battles against nightmarish creatures. Along the way, deep-seated mistrust threatened to unravel their alliance, but they learned that cooperation and understanding were essential. In a final battle, they confronted the sorceress and her minions, leading to a climactic victory that solidified their bond.",
            "As tensions rose in the faction of Adamas, whispers of betrayal echoed through the citadel. A trusted leader revealed himself as a traitor, conspiring with enemy factions to undermine their strength. Kaelin, a fierce warrior, took it upon herself to expose the traitor's plans. Gathering a small group of loyal allies, she delved into the depths of intrigue that surrounded the faction. As they pieced together the evidence, they uncovered a larger conspiracy involving multiple factions. Time was of the essence, and Kaelin led her team through perilous encounters to thwart the traitor\'s schemes. In a gripping climax, loyalty and bravery shone through, ensuring the safety of their people and restoring faith in their leadership.",
            "An ancient card named Echo emerged from a forgotten archive, believed to hold the spirit of a legendary hero. As the Adamas faction began to use Echo in their battles, visions of the hero\'s life flooded their minds, revealing forgotten truths and hidden wisdom. However, these revelations awakened a dark force tied to the hero\'s legacy, threatening the peace of their world. The faction realized they must uncover the truth behind Echo\'s past to prevent disaster. This journey took them into the depths of their own history, where they faced their fears and insecurities. In a powerful climax, they confronted the dark force, ultimately embracing the lessons of the past to secure a brighter future.",
            "An impending alliance with neighboring factions faced a severe crisis as misunderstandings spiraled into conflict. As tensions escalated, a group of diplomats, led by the cunning strategist Elowen, took it upon themselves to mend the rift. Their quest for peace led them through dangerous territories filled with hostile forces. Along the way, Elowen uncovered a common enemy that sought to exploit the divisions among the factions. Through negotiation, strategy, and daring exploits, they managed to expose the truth behind the animosities. In a gripping conclusion, Elowen brokered peace and forged a new alliance, proving that understanding and dialogue were far more potent than weapons.",
            "Deep within the mountains, a long-forgotten citadel of pure crystal lay waiting to be discovered. Legends spoke of its incredible power to amplify the abilities of card wielders. When the Adamas faction ventured inside, they were met with a series of trials designed to test their virtues and resolve. Each chamber challenged their strengths, forcing them to confront their innermost fears. As they approached the heart of the citadel, ancient guardians emerged to protect its secrets. A fierce battle ensued, where the faction had to choose between the temptation of power and their responsibility to protect their realm. In the end, their decisions forged their legacy, and the citadel revealed its true purpose.",
            "A catastrophic storm descended upon the land, believed to be the wrath of a long-forgotten deity seeking revenge for past betrayals. The leaders of Adamas understood the urgent need to quell the tempest before it consumed everything. A brave team, led by the fearless explorer Thorne, ventured into the storm\'s eye. Within the chaos, they uncovered remnants of an ancient civilization that once worshiped the deity. As they pieced together the truth, they realized that the deity\'s anger stemmed from profound loss and betrayal. Through a combination of bravery, ancient rituals, and fierce battles against storm minions, they managed to calm the deity\'s spirit, restoring harmony to the realm.",
            "In the depths of an ancient library, scholars of Adamas discovered texts revealing their true purpose as guardians of a primordial force that shaped magic itself. This revelation ignited a sense of duty among the faction\'s members. However, they soon learned that a rival faction sought to harness this power for their own ambitions. A group of dedicated card wielders, led by the wise elder Ilyana, set out to protect this knowledge. Their journey took them through treacherous landscapes, facing powerful adversaries and ethical dilemmas. In a climactic battle that intertwined fate and magic, they defended their legacy, securing their place as true stewards of magic for future generations."
        ],
        "Avian":[
            "In the majestic skies of Avian, where floating islands drifted like clouds, a young aerial navigator named Mira dreamed of discovering the legendary Isle of Whispers. According to ancient tales, the isle held secrets of forgotten powers that could control the winds themselves. Joined by her loyal companion, a mischievous sparrow named Flick, Mira set off on her airship. Their journey led them through treacherous storms, encounters with sky pirates, and mystical creatures of the wind. As they neared the isle, Mira faced a choice between her ambition and protecting the fragile harmony of the skies. In a dramatic finale, she used her newfound powers to restore balance, earning the respect of the skyborne clans.",
            "In the heart of Avian, an ancient prophecy foretold the rise of a hero with feathers of gold who would unite the warring bird factions. As tensions escalated between the Sunwing and Moonshadow clans, a humble villager named Kaelan discovered that he bore the mark of the prophecy. With the guidance of a wise elder, Kaelan embarked on a quest to find the sacred Golden Feather. Along the way, he faced trials that tested his courage, wisdom, and ability to unite disparate factions. Through clever diplomacy and unexpected alliances, Kaelan ultimately brought peace to Avian, proving that true leadership lies in understanding and compassion.",
            "When a powerful storm swept across the lands of Avian, it threatened to tear apart the delicate balance between the elemental factions. Zephyra, a fierce wind elemental, sought to uncover the source of the chaos. As she delved deeper into the storm\'s mysteries, she discovered that a rogue storm spirit had gone awry, driven by anger and despair. With the help of a reluctant ally from the earth faction, Zephyra embarked on a perilous journey to confront the spirit. Their battles against fierce gales and violent lightning culminated in a confrontation where understanding and empathy triumphed. Zephyra learned that even the most chaotic beings needed compassion, ultimately restoring harmony to the skies.",
            "Deep within the Emerald Forest, a dark curse befell the once-vibrant Avian community. A cursed talon, said to belong to an ancient beast, spread despair and illness among the birdfolk. A courageous healer named Lira took it upon herself to break the curse. Guided by the whispers of the forest spirits, Lira ventured into the depths of the woods, seeking the truth behind the talon\'s origin. Along her journey, she encountered enigmatic creatures and faced trials that tested her resolve. In a heart-stopping climax, Lira confronted the beast and discovered that the curse was born from pain and betrayal. By healing the beast\'s heart, she not only lifted the curse but also restored peace to the forest.",
            "In a world where light and shadow coexisted, the balance was disrupted when a shadowy figure began stealing the light from Avian. A daring avian warrior named Tarek, known for his unmatched skill in combat, vowed to confront this mysterious thief. His journey took him through dark caverns and into the heart of the shadow realm, where he uncovered a hidden society of shadow beings. As Tarek battled against the darkness, he realized that not all shadows were evil; some sought liberation from their chains. In an epic showdown, Tarek had to decide between defeating the shadow thief or forging an alliance to restore balance. His choice would redefine the relationship between light and shadow forever.",
            "In the melodious realm of Avian, music held the power to unite and heal. However, the Great Song, the source of this power, had been lost for centuries. Elara, a talented songbird with a voice that could charm the skies, set out on a quest to find the pieces of the Great Song. With the help of a mysterious bard and an eccentric inventor, she traveled across floating islands, solving riddles and overcoming obstacles. Each piece of the song revealed a fragment of the history of Avian, and as they came together, Elara felt the call of her ancestors. In a breathtaking finale, she performed the completed Great Song, awakening the spirits of Avian and restoring harmony to the realm.",
            "When the winds grew restless and the skies darkened, rumors spread of an ancient heir to the throne of the Wind Clan. A young girl named Anya, raised in a humble village, discovered that she possessed the bloodline of the Wind Clan. With the guidance of a retired warrior, she embarked on a journey to claim her rightful place and restore peace among the factions. Along the way, Anya faced formidable challenges, including betrayal from those seeking power. Her journey became one of self-discovery, as she learned to embrace her heritage and the responsibilities it entailed. In a gripping climax, Anya united the clans against a common enemy, proving that true leadership is born from courage and integrity.",
            "Every few years, the avian tribes of Avian participated in a Great Migration to ensure the survival of their species. However, this year, a malevolent force sought to disrupt the migration, threatening the delicate ecosystem. A daring young hawk named Kiran was chosen to lead the flock through dangerous territories. As they soared through fierce storms and navigated treacherous landscapes, Kiran discovered that the threat came from a rival faction that had turned rogue. In a battle for survival, Kiran had to rally the tribes, forging alliances and overcoming mistrust. The migration became a testament to unity, resilience, and the power of community as they triumphed over adversity.",
            "In a secluded part of Avian, ancient ruins held secrets of a bygone era. When explorers discovered strange symbols that foretold a great danger, a group of scholars and adventurers, including a clever raven named Jax, set out to uncover the truth. As they delved deeper into the ruins, they faced ancient traps, riddles, and guardians that tested their wits and bravery. The deeper they went, the more they uncovered the story of an ancient civilization that had fallen due to hubris. In a climactic moment, Jax deciphered the final riddle, revealing a way to prevent history from repeating itself. The team emerged with newfound knowledge and a responsibility to protect the future of Avian.",
            "The fragile peace among the avian tribes was shattered when a series of misunderstandings led to accusations and hostilities. A brave diplomat named Rowan sought to mend the rift and restore unity. Traveling from clan to clan, he listened to grievances and sought common ground. However, a hidden enemy sought to exploit the divisions for their own gain, orchestrating further chaos. As Rowan uncovered the truth behind the manipulations, he rallied the clans to confront the true threat. In an epic confrontation, Rowan\'s efforts to unite the tribes led to a powerful alliance that not only defeated the enemy but also forged a new era of cooperation. His legacy became a testament to the strength found in unity."
        ],
        "Barbarian":[
            "In the rugged mountains of Barbaria, a young warrior named Grom made a blood oath to avenge his fallen clan, slain by a rival tribe. With his trusty axe, he embarked on a journey through treacherous terrains, facing beasts and hostile warriors alike. Along the way, he encountered a mysterious shaman who revealed that revenge alone would not heal his wounds. Grom had to confront his own rage and learn the value of community and honor. In a fierce battle against the rival tribe\'s leader, Grom\'s newfound wisdom transformed his vengeance into a quest for justice, ultimately uniting both clans against a greater evil lurking in the shadows.",
            "Legends spoke of the Shattered Shield, an ancient artifact that once protected the land from invaders. When it was stolen by a dark sorceress, chaos erupted across Barbaria. A fierce warrior named Thalia rallied her fellow fighters, determined to reclaim the shield. As they journeyed through enchanted forests and cursed caves, the team faced formidable foes, including mythical creatures and treacherous traps. Each battle revealed more about the sorceress\'s tragic past and her reasons for seeking power. In a climactic showdown, Thalia and her allies not only retrieved the shield but also broke the sorceress\'s curse, restoring peace to the land and learning the true meaning of strength.",
            "In a remote village, a mysterious illness plagued the inhabitants, transforming them into monstrous beasts under the full moon. A young warrior named Kael, who had lost his family to the curse, sought to uncover the truth behind this dark magic. Guided by an ancient scroll, he traveled to the heart of the Forbidden Woods, where he encountered a reclusive druid named Eldara. She revealed that the curse was a result of a broken pact with nature. Together, they embarked on a quest to restore the balance, facing spectral guardians and unraveling hidden secrets. In a heart-stopping climax, Kael confronted his own inner beast, ultimately embracing it as part of his identity, and saved his village.",
            "Barbaria was once united, but now the elemental tribes—Earth, Fire, Water, and Air—were embroiled in a devastating conflict. A young barbarian named Lira, born of mixed elemental heritage, sought to bridge the divide. As she journeyed from tribe to tribe, Lira discovered the truth behind the war: a manipulative entity was pitting the tribes against each other for its own gain. With the help of an unlikely ally from each tribe, she uncovered ancient prophecies and powerful relics. In a dramatic battle that showcased the strengths of all elements, Lira united the tribes against the entity, proving that diversity could forge an unbreakable bond.",
            "In a kingdom ruled by a tyrant, the barbarian clans had long been oppressed. A fiery leader named Ragnar ignited the flames of rebellion, calling upon warriors to rise against the oppressive regime. As Ragnar and his band of rebels embarked on daring raids to liberate villages, they encountered betrayal from within their ranks. Trust was shattered, and alliances were tested. Amidst the chaos, Ragnar learned that the fight for freedom required not just strength but also strategic cunning. In a gripping climax, he confronted the tyrant in an epic battle that symbolized the hope of a united Barbaria. The rebellion sparked a revolution, reshaping the future of the land.",
            "In the heart of Barbaria, a legendary huntress named Elara roamed the wilderness, revered for her unmatched skills. When a series of mysterious disappearances plagued the forest, she took it upon herself to investigate. Guided by whispers from the spirits of the wild, Elara discovered a sinister plot orchestrated by a malevolent beast seeking to dominate the forest. With her bow and unwavering courage, she rallied a group of unlikely allies—a clever trickster and a gentle giant. Together, they ventured deep into the beast\'s lair, facing fierce battles and unraveling dark secrets. In a breathtaking showdown, Elara\'s ingenuity and compassion transformed the beast, restoring peace to the land.",
            "Every century, the barbarian clans held the Trials of the Ancients, a series of challenges to honor their forebears. This year, young warriors competed not just for glory but to determine the next chieftain. Among them was Kira, a determined young woman who aimed to prove her worth in a male-dominated world. As the trials progressed, Kira faced fierce competitors and personal doubts. Through physical and mental challenges, she uncovered ancient wisdom about leadership and sacrifice. In the final trial, she confronted a rival who sought to sabotage her, using both her strength and newfound knowledge to triumph. Kira\'s victory not only changed her fate but also redefined the legacy of her clan.",
            "In a time of turmoil, the worship of the ancient gods faded, leaving a once-vibrant faith in ruins. A young shaman named Orin sought to awaken the Forgotten God, believed to hold the power to restore balance to the world. As he embarked on a quest across Barbaria, he faced skepticism, ridicule, and the encroaching darkness threatening to consume the land. Orin\'s journey led him to ancient shrines where he sought guidance from spirits. Along the way, he gathered allies who believed in his cause, and together they faced monstrous challenges. In a heart-stirring climax, Orin performed a ritual that rekindled the faith of his people, awakening the Forgotten God and ushering in a new era of hope.",
            "In a remote village, an ancient relic known as the Stone of Valor held the memories of past warriors. When the stone was stolen by a band of marauders, the village faced despair. A determined warrior named Brynn vowed to retrieve it, knowing the relic was the key to uniting the tribes against the encroaching threat. Brynn\'s journey led her through perilous landscapes, where she encountered legendary beasts and forgotten spirits. Each encounter revealed the strength and sacrifice of those who came before her. In a climactic battle against the marauders, Brynn unlocked the power of the stone, channeling the spirits of the fallen warriors to reclaim her village\'s legacy and inspire a new generation.",
            "When a colossal serpent awoke from its slumber, it brought destruction to the lands of Barbaria. A fierce warrior named Kael was determined to end the serpent\'s reign of terror. With a band of skilled fighters, he set off on a quest to uncover the origins of the curse that bound the serpent to its rage. Their journey took them to ancient ruins and hidden caves filled with traps and challenges. As they unraveled the history of the serpent, they discovered that it was once a guardian of balance, corrupted by greed and betrayal. In a gripping showdown, Kael faced the serpent, not with brute force, but with a heart full of compassion and understanding, ultimately breaking the curse and restoring the serpent to its rightful role as protector of the land."
        ],
        "Cyttorak":[
            "In the heart of a desolate wasteland, a powerful artifact known as the Crimson Gem lay hidden. This gem was said to hold the essence of Cyttorak, granting immense strength to its wielder. A young warrior named Jarek, driven by the desire to protect his village, embarked on a perilous quest to find the gem. Along the way, he encountered ancient guardians, treacherous traps, and rival treasure hunters. As Jarek delved deeper into the secrets of the gem, he discovered that it was not just a source of power but also a key to awakening an ancient evil. In a gripping climax, Jarek had to choose between using the gem for his own gain or destroying it to prevent catastrophe, ultimately realizing that true strength comes from sacrifice.",
            "In a world where sorcery and brute force clashed, a young sorceress named Elira discovered she was chosen by Cyttorak to become the next Guardian of Balance. As darkness began to spread across the realm, threatening to consume everything in its path, Elira set out on a journey to gather allies from different factions. Each ally brought unique skills, but tensions ran high as old rivalries resurfaced. Through trials of trust and friendship, Elira led her group to confront the source of the darkness. In an epic battle against a corrupted warlock who sought to harness Cyttorak\'s power, Elira\'s unwavering belief in unity turned the tide, restoring balance to the realm.",
            "A clandestine cult devoted to Cyttorak sought to revive their ancient deity by performing a forbidden ritual. A skilled rogue named Rylan infiltrated their ranks, determined to stop them from unleashing chaos. As he navigated the treacherous world of cultists, he discovered that the cult planned to sacrifice an innocent child to summon Cyttorak\'s essence. Rylan formed an uneasy alliance with a former cult member, who revealed the truth about the cult\'s dark past. Together, they devised a plan to thwart the ritual, leading to a breathtaking showdown where Rylan had to confront his own fears and doubts. In the end, he not only saved the child but also shattered the cult\'s power, exposing their lies to the world.",
            "When a powerful serpent emerged from the depths of the Underworld, its malevolence threatened to plunge the realm into darkness. A brave knight named Lira took it upon herself to uncover the origins of the serpent\'s curse. With her loyal companion, a mystical beast named Koru, Lira journeyed through haunted forests and desolate ruins, gathering clues and facing nightmarish creatures. As she delved deeper into the serpent\'s past, Lira discovered that it was once a guardian betrayed by those it trusted. In a heart-wrenching climax, Lira confronted the serpent, not as an enemy, but as a healer, breaking the curse and restoring the guardian\'s true nature.",
            "In the hidden sanctum of Cyttorak, a series of arcane trials awaited those who sought to prove their worth. A group of aspiring mages, each with their own motivations, entered the trials, unaware of the challenges that lay ahead. As they faced magical puzzles and powerful foes, alliances formed and shattered under the pressure. Among them was a young mage named Kaelin, who struggled with self-doubt but possessed a unique affinity for elemental magic. Through perseverance and courage, Kaelin unlocked her true potential and learned the importance of collaboration. In the final trial, she stood against an ancient elemental guardian, ultimately proving that strength lies in unity and understanding.",
            "In the city of Cyttorak, political intrigue festered beneath the surface. A noblewoman named Seraphine discovered a plot to overthrow the ruling council by a group of power-hungry nobles. As she delved deeper into the conspiracy, she faced betrayal from those she once trusted. Seraphine sought the aid of a brooding mercenary known for his ruthless tactics, hoping to gain insights into the shadowy underworld. Together, they uncovered dark secrets that threatened not just the council but the very fabric of the city. In a nail-biting climax, Seraphine orchestrated a counterplot that exposed the traitors, leading to a fierce confrontation that would decide the fate of Cyttorak.",
            "In a world where magic was fading, the last Guardian of Cyttorak, an ancient being named Thalos, faced the impending doom of his realm. As darkness began to envelop the lands, Thalos sought a mortal champion to help him restore balance. He chose a reluctant farmer named Elan, who possessed an untapped potential for magic. As Elan trained under Thalos\'s guidance, he encountered trials that tested his character and resolve. With time running out, Elan and Thalos faced the encroaching darkness in an epic showdown that revealed the true power of belief and sacrifice. In a heart-stopping conclusion, Elan embraced his destiny, becoming a beacon of hope for a new generation.",
            "An ancient mirror rumored to reflect one\'s true self was hidden within the depths of Cyttorak. A determined thief named Mira sought the mirror to change her fate, believing it held the key to her dreams. As she navigated through traps and enchanted guardians, Mira uncovered dark truths about herself and her past. The mirror, however, revealed more than she anticipated, forcing her to confront her deepest fears and insecurities. In a climactic moment, Mira realized that true change comes from within, not through magical artifacts. By accepting herself and her choices, she emerged stronger, breaking free from the chains of her past.",
            "In Cyttorak, time flowed differently, and a rift threatened to collapse the fabric of reality. A scholar named Rion discovered that ancient prophecies spoke of a timekeeper who could mend the rift. Alongside a group of brave adventurers, Rion embarked on a quest to locate the elusive timekeeper, traversing through alternate realities and facing temporal anomalies. As they ventured deeper into the heart of the rift, they confronted their own pasts and the choices that led them there. In a breathtaking climax, Rion and his allies united their strengths, channeling the essence of time itself to restore balance, proving that the future is shaped by the choices of the present.",
            "In the realm of Cyttorak, music held the power to influence magic and reality. A gifted bard named Liora sought to uncover the lost Song of the Ancients, said to hold the key to ultimate power. Her journey took her to ancient ruins, where she deciphered cryptic melodies and faced ethereal guardians. As she gathered fragments of the song, Liora encountered others who sought the power for themselves, leading to fierce rivalries. In a heart-pounding finale, Liora performed the completed song, awakening the spirits of the ancients and harnessing their magic. With newfound understanding, she chose to use her power to unite rather than conquer, transforming the realm through the harmony of music."
        ],
        "Dreizen":[
            "In the world of Dreizen, the land was once a harmonious blend of nature and magic, but a catastrophic event known as the Shattering split the realm into fragments. A young sorceress named Aria set out on a quest to restore balance. Guided by ancient texts, she traveled across floating islands and treacherous chasms, gathering shards of a powerful artifact known as the Heart of Dreizen. Along the way, she encountered other seekers—some allies, some foes. In a climactic battle against a dark sorcerer who sought to control the Heart for himself, Aria learned that true power comes from unity. With her newfound friends, she combined their strengths to restore the Heart and heal the realm.",
            "Deep within Dreizen lay the Whispering Woods, rumored to be enchanted by the spirits of the ancients. A curious bard named Finn ventured into the woods seeking inspiration for his songs but soon discovered that the woods held dark secrets. As he wandered, he heard whispers that warned him of an impending danger—a malevolent force awakening from a slumber. With the help of a mysterious forest guardian named Elowen, Finn navigated through illusions and traps to uncover the truth. Together, they faced the awakened spirit in an epic showdown, using the power of music and harmony to banish the darkness, teaching Finn that his songs could wield great power.",
            "Every decade, the kingdoms of Dreizen hosted the Tournament of Champions, where the bravest warriors competed for glory. A humble blacksmith named Kael entered the tournament, fueled by the desire to prove himself and protect his village from invading forces. As he faced formidable opponents, he forged unexpected alliances with fellow competitors. Amidst fierce battles, Kael uncovered a conspiracy to sabotage the tournament, orchestrated by a rival kingdom seeking to claim dominance. In a thrilling climax, Kael rallied his allies to expose the plot, turning the tournament into a battle for justice. His bravery not only won him the title of champion but also united the kingdoms against a common enemy.",
            "In the northern reaches of Dreizen, the Crystal Caves held mysteries that had captivated explorers for generations. When a famed archaeologist disappeared within the caves, a determined apprentice named Mira set out to find him. Guided by a cryptic map and her intuition, she journeyed through the shimmering caverns, encountering magical creatures and formidable guardians. As she delved deeper, Mira uncovered an ancient prophecy about a crystal that could reshape reality. In a heart-pounding climax, she confronted a shadowy figure seeking to harness the crystal\'s power for destruction. Mira\'s quick thinking and bravery ultimately saved the archaeologist and secured the crystal, proving that knowledge and courage could conquer darkness.",
            "Legends spoke of a lost city hidden beneath the sands of Dreizen, guarded by ancient beings. When rumors surfaced of a treasure buried within the city, a band of treasure hunters, led by the cunning rogue Tarek, sought to claim it for themselves. However, they soon discovered that the city was protected by powerful guardians who tested the worthiness of all who entered. Tarek\'s crew faced traps, riddles, and trials that revealed their true motivations. In a dramatic twist, Tarek realized that the treasure was not gold but knowledge that could change the fate of their world. With newfound purpose, he chose to leave the treasure behind and unite the hunters in preserving the city\'s legacy.",
            "In the village of Eldergrove, a moonstone jewel held great power but was cursed to bring misfortune. When the jewel was stolen by a mysterious thief, the village descended into chaos. A brave herbalist named Lyra set out to retrieve the moonstone and break the curse. Along the way, she faced dark forces and discovered that the thief was a cursed soul seeking redemption. As Lyra confronted the thief, she learned the importance of understanding and compassion. In a climactic moment, she chose to help the thief lift their curse instead of seeking revenge, ultimately restoring peace to Eldergrove and freeing both the village and the thief from their burdens.",
            "The four elemental clans of Dreizen—Earth, Fire, Water, and Air—were once united, but a catastrophic war erupted between them. A young diplomat named Elysia, born of mixed heritage, sought to bring peace. As she traveled to each clan, she faced deep-rooted prejudices and fierce rivalries. Elysia discovered that a dark entity was manipulating the clans to fuel their conflict. With the help of elemental champions from each clan, she uncovered the truth and forged a plan to confront the entity. In an epic battle, Elysia united the elemental powers, demonstrating that cooperation could overcome even the most profound divisions. Her bravery restored harmony to the clans and healed the land.",
            "A notorious thief known as the Shadow Thief plagued the cities of Dreizen, stealing powerful artifacts and leaving chaos in his wake. A young detective named Rowan was determined to bring him to justice. As he tracked the thief through shadowy alleys and hidden passages, Rowan uncovered a web of deceit that reached the highest echelons of society. Along the way, he formed an alliance with a reformed thief named Selene, who possessed knowledge of the criminal underworld. Together, they unraveled the truth behind the Shadow Thief\'s motives, leading to a breathtaking confrontation that tested their resolve. In the end, Rowan learned that sometimes justice meant understanding the complexities of morality.",
            "In the night sky of Dreizen, two stars shone brighter than the rest, believed to be connected to an ancient prophecy. A young astronomer named Arlen became obsessed with deciphering its meaning. His quest led him to an ancient temple where he discovered that the stars were guardians of fate, linked to the balance of light and dark. As dark forces sought to extinguish the stars\' light, Arlen gathered a group of allies, including a fierce warrior and a wise elder. Together, they faced challenges that tested their resolve and loyalty. In a stunning finale, Arlen unlocked the secret of the stars, channeling their power to restore balance, proving that destiny is shaped by choices.",
            "In a world where fire was both a gift and a curse, a young fire mage named Kira faced the extinction of her kind. The last ember, said to hold the essence of fire magic, was believed to be hidden in the volcanic mountains. Kira embarked on a treacherous journey, facing rival mages and ancient fire spirits. As she delved deeper into the mountain, she confronted her fears and insecurities, learning the true meaning of courage. In a climactic battle against a powerful entity seeking to extinguish the last ember, Kira embraced her identity and unleashed the full potential of her magic. Her victory not only saved her people but also reignited hope for a future where fire could be a source of life and creation."
        ],
        "Etrigon":[
            "In the once-mighty Etrigon Empire, a dark prophecy foretold the rise of a tyrant who would shatter the realm. A young scholar named Elian discovered ancient texts that hinted at a hidden power capable of preventing this fate. Determined to save his homeland, Elian embarked on a perilous journey to gather the lost artifacts of the Etrigon Kings. Along the way, he faced treacherous landscapes, betrayal from former allies, and encounters with mythical creatures. As the empire descended into chaos, Elian rallied a band of unlikely heroes—including a disgraced knight and a skilled rogue. In an epic climax, they confronted the tyrant in a battle that would decide the fate of Etrigon, revealing that the strength of unity could triumph over darkness.",
            "Deep within the enchanted woods of Etrigon lay the Heart of the Forest, a mystical gem that maintained the balance of nature. When it was stolen by a dark sorceress, the forest began to wither, and chaos spread through the realm. A brave ranger named Kaelin set out to retrieve the Heart, guided by ancient prophecies and the whispers of the trees. Along her journey, she faced dangerous beasts, deceptive illusions, and trials that tested her resolve. With the help of a reluctant apprentice who harbored a deep connection to the forest, Kaelin unraveled the sorceress\'s motives, discovering a tragic past that fueled her rage. In a heart-stopping climax, Kaelin confronted the sorceress, learning that compassion could heal even the deepest wounds, and restored the Heart to its rightful place.",
            "In the city of Zorath, a mysterious cult known as the Shadow Dancers wielded dark magic, manipulating the fabric of reality. When the city fell into fear and chaos, a young street performer named Mira found herself drawn into their web of intrigue. Unbeknownst to her, Mira possessed a rare ability to manipulate light, making her a target for the cult. With the help of a seasoned warrior and a wise mage, she sought to uncover the cult\'s secrets and put an end to their reign of terror. As she delved deeper into the shadows, Mira discovered the true nature of her power and the responsibility that came with it. In a climactic showdown, she faced the cult\'s leader, embracing her light to dispel the darkness and free the city from its grasp.",
            "In Etrigon, the four elemental factions—Earth, Water, Fire, and Air—had coexisted for centuries. However, tensions boiled over when a powerful artifact known as the Elemental Core was stolen. A gifted elemental mage named Lira, born of all four elements, was chosen to unite the factions and recover the Core. As she journeyed to each faction\'s territory, she faced prejudice and distrust. Lira learned that the artifact had been taken by a rogue elementalist who sought to unleash chaos. In a breathtaking finale, Lira forged alliances among the factions, combining their strengths in a climactic battle that proved that diversity was their greatest asset.",
            "In a small village, an ancient heirloom—a necklace said to grant protection—was cursed, bringing misfortune to its wearer. A young girl named Aria, determined to lift the curse, uncovered the heirloom\'s dark history tied to a vengeful spirit. With the guidance of a local elder, she embarked on a quest to confront the spirit and uncover the truth behind the curse. Along the way, Aria faced her own fears and learned the importance of bravery and forgiveness. In a heart-wrenching climax, she confronted the spirit, offering empathy and understanding, ultimately breaking the curse and restoring peace to her village.",
            "Every century, a powerful trial was held to select the next Guardian of Etrigon, a protector of balance and peace. A young warrior named Bran sought to prove himself worthy, but the trials were fraught with danger. As he faced physical and mental challenges, he discovered that the true test lay not in strength but in wisdom and compassion. With the guidance of a mysterious mentor, Bran learned to harness the strengths of his companions. In a final trial, he faced an ancient guardian, revealing that sacrifice and selflessness were the keys to becoming a true Guardian. Bran\'s victory not only secured his place as a protector but also united the realms in harmony.",
            "When a celestial event known as the Starfall occurred, strange phenomena swept across Etrigon, awakening dormant powers within its inhabitants. A curious astronomer named Elenor sought to understand the mysteries behind the Starfall, gathering a group of adventurers to explore the unexplained occurrences. As they journeyed through the realm, they encountered others affected by the event, each with unique abilities and struggles. Together, they unraveled a conspiracy that aimed to exploit the Starfall\'s power for domination. In a gripping climax, Elenor and her allies confronted the mastermind behind the plot, using their newfound abilities to restore balance and reveal the true nature of the Starfall.",
            "In the desert lands of Etrigon, a prophecy spoke of a Phoenix that would rise to save the realm from destruction. A humble farmer named Joren discovered he had a deep connection to the Phoenix and set out to find it. His journey led him through perilous sands and treacherous landscapes, where he encountered nomadic tribes and ancient ruins. As he learned about the Phoenix\'s significance, Joren discovered that he must confront his own fears to fulfill the prophecy. In an explosive finale, he faced a malevolent force threatening to engulf the realm, ultimately awakening the Phoenix within himself and harnessing its power to restore hope.",
            "In the ruins of a once-great city, the ghosts of fallen heroes haunted the remnants, seeking justice for their forgotten sacrifices. A brave historian named Selene uncovered the truth behind the city\'s downfall, discovering that a corrupt ruler had betrayed its guardians. With the help of a group of intrepid adventurers, Selene sought to honor the fallen by uncovering their stories and revealing the truth to the world. As they faced trials of courage and resilience, Selene learned the importance of remembering the past. In a moving climax, she confronted the remnants of the corrupt ruler\'s regime, channeling the strength of the fallen heroes to reclaim the city\'s legacy and restore its honor.",
            "In the heart of Etrigon, a renowned alchemist named Thaddeus disappeared, leaving behind a trail of enigmatic clues. A determined apprentice named Cassia set out to uncover the truth behind his disappearance, believing it tied to a legendary formula that could change the course of alchemy. As she followed the clues, Cassia encountered rival alchemists, mythical creatures, and dangerous traps. Along her journey, she discovered the true nature of Thaddeus\'s work and the responsibility that came with great power. In a thrilling climax, Cassia faced a rival seeking to exploit the formula for destruction. Embracing her mentor\'s teachings, she used her knowledge and creativity to thwart the rival\'s plans and ensure that the secrets of alchemy were used for good."
        ],
        "Firimir":[
            "In the realm of Firimir, a celestial event known as the Twilight Convergence was prophesied to awaken ancient powers. A young mage named Elowen discovered she was destined to harness these powers to prevent impending doom. As she gathered a diverse group of adventurers, including a rogue with a mysterious past and a noble knight seeking redemption, they journeyed to the sacred Mountain of Echoes. Along the way, they faced trials that tested their loyalties and strengths. In a climactic battle against a dark sorceress aiming to exploit the convergence, Elowen learned that true power lies in unity. Together, they channeled the convergence to restore balance to Firimir.",
            "In the kingdom of Eldoria, a crown that once united the land was shattered, leading to chaos among its factions. A brave warrior named Kael found one of the crown\'s shards and was thrust into a quest to restore the crown and unite the kingdoms. His journey led him to treacherous mountains and enchanted forests, where he encountered mythical beasts and rival claimants. As Kael pieced together the shards, he learned about the history of the crown and the sacrifices of its past bearers. In a thrilling climax, he confronted a power-hungry lord who sought to claim the crown for himself. With newfound allies by his side, Kael united the kingdoms, proving that unity could overcome ambition.",
            "In the coastal city of Myridian, the Whispering Tides—a mysterious phenomenon that granted visions of the future—began to falter. A young oracle named Lyra was chosen to uncover the truth behind the tides. Guided by her visions, she sailed into uncharted waters, accompanied by a spirited crew and a skeptical first mate. As they ventured deeper, they faced monstrous sea creatures and treacherous storms. Lyra discovered that the tides were linked to the emotions of the people. In a heart-pounding finale, she calmed the raging seas by uniting the city in hope and purpose, restoring the Whispering Tides and ensuring a brighter future.",
            "Once a thriving metropolis, Elysium had fallen into ruin after its magical core was stolen. A resourceful thief named Ash was drawn to the ruins, believing that recovering the core could restore his lost homeland. Alongside a brilliant inventor and a fierce protector, he navigated the city\'s labyrinthine streets, facing enchanted traps and malevolent spirits. As they uncovered the truth, they discovered that a dark entity sought to drain the city\'s magic for its own gain. In a gripping climax, Ash and his companions confronted the entity, reclaiming the core and awakening the city\'s magic, proving that even in despair, hope could be found.",
            "In the heart of Firimir, a mythical shard was said to grant its bearer the power to shape destiny itself. A humble farmer named Jorin stumbled upon the shard while tending his fields, unknowingly setting off a chain of events that attracted powerful factions seeking to claim it. As chaos engulfed his village, Jorin joined forces with a wise elder and a fierce warrior to protect the shard from falling into the wrong hands. Their journey took them through enchanted forests and hidden caves, where they encountered ancient guardians. In a breathtaking showdown, Jorin embraced his destiny, proving that ordinary people could rise to greatness.",
            "In a world where fire magic was slowly fading, a young pyromancer named Rhea sought to rekindle the Last Ember, a legendary flame that could restore fire magic to its former glory. Her quest led her to the treacherous Volcano of Ashara, where she faced trials that tested her skills and determination. Along the way, she discovered that the ember was guarded by a powerful fire spirit, bound by a curse. Rhea learned that true fire magic came from within and needed to be balanced with compassion. In a heart-stopping finale, she freed the spirit from its curse, reigniting the Last Ember and awakening the fire magic throughout Firimir.",
            "In the ancient ruins of Nythara, a long-forgotten prophecy spoke of a hero who would rise to save Firimir from an encroaching darkness. A curious historian named Elira uncovered the prophecy and found herself at the center of a brewing conflict. As dark forces sought to silence her, Elira joined forces with a group of misfits: a cynical bard, a brash warrior, and a reclusive sorceress. Together, they unraveled the prophecy\'s meaning and discovered the source of the darkness. In a thrilling climax, Elira embraced her role as the chosen hero, uniting her companions and the realm against the impending threat, proving that even the most unlikely heroes could change the world.",
            "In the mystical realm of Firimir, Dreamweavers possessed the unique ability to shape dreams into reality. A young Dreamweaver named Sylas was tasked with protecting the Dream Nexus, a powerful source of dream magic. When a shadowy figure sought to corrupt the Nexus, Sylas embarked on a quest to stop them. Alongside a tenacious guardian and a cunning illusionist, he ventured into the Dream Realm, confronting twisted nightmares and his own fears. In a climactic showdown, Sylas harnessed the power of dreams and hope, defeating the shadowy figure and preserving the Dream Nexus, ensuring that dreams would continue to inspire the people of Firimir.",
            "In the skies above Firimir, celestial beings known as the Guardians maintained the balance between light and darkness. When a rogue Guardian sought to upset this balance, a courageous pilot named Aria found herself caught in the middle of an ancient conflict. With the help of a spirited engineer and a wise mentor, Aria embarked on a journey to confront the rogue Guardian and restore harmony. As they soared through the skies, they uncovered secrets of the Guardians\' past and the true nature of their powers. In a breathtaking aerial battle, Aria and her companions fought against the rogue Guardian, ultimately reclaiming the balance and safeguarding the skies of Firimir.",
            "In Firimir, music held the power to influence magic and evoke emotions. A gifted bard named Liora discovered an ancient song that could awaken forgotten powers. However, a dark force sought to silence the song and plunge the realm into despair. Liora embarked on a quest to gather the lost verses, aided by a ragtag group of musicians and warriors. As they traveled through enchanted forests and haunted ruins, they faced challenges that tested their creativity and resolve. In a heart-pounding finale, Liora performed the completed song, awakening the spirits of the ancients and channeling their magic to defeat the dark force, ensuring that music would continue to thrive in Firimir."
        ],
        "Gennesis":[
            "In Gennesis, ancient crystals held the power to shape reality itself. A young artisan named Kaelan discovered a forgotten crystal in his village, awakening a latent power within him. As he began to harness this energy, dark forces sought to claim the crystal for themselves. Kaelan embarked on a quest to uncover the truth about the crystals, joined by a fierce warrior named Thalia and a wise scholar named Eldrin. Together, they traversed treacherous landscapes and faced mythical beasts. In a climactic battle against a power-hungry sorceress, Kaelan learned that true strength came not just from power, but from the bonds forged with friends, ultimately restoring balance to Gennesis.",
            "In the mystical realm of Gennesis, a prophecy foretold the rise of the Starborn—individuals destined to wield immense power. A young girl named Mira discovered that she was one of the Starborn, marked by a celestial birthmark. As darkness began to spread across the land, she set out to find others like her. Along her journey, she encountered a brooding knight and a spirited rogue, each with their own hidden talents. Together, they faced trials that tested their resolve and friendship. In a breathtaking climax, Mira embraced her destiny, combining her powers with her allies to confront a looming darkness, proving that unity could conquer even the greatest evil.",
            "The Shattered Isles were once a vibrant archipelago, but a catastrophic event had torn them apart, scattering their inhabitants. A determined sailor named Rion sought to reunite the islands and restore their former glory. Guided by an ancient map, he journeyed through stormy seas and treacherous waters. Along the way, he gathered a crew of misfits: a skilled navigator, a fierce warrior, and a cunning thief. As they faced rival factions and mythical sea creatures, Rion discovered the islands held powerful secrets. In a climactic battle against a rival pirate lord, Rion learned that true leadership meant valuing his crew\'s strengths, ultimately restoring harmony to the Shattered Isles.",
            "Deep beneath the surface of Gennesis lay the ruins of an ancient civilization, rumored to be guarded by powerful spirits. When a group of explorers stumbled upon the ruins, they unwittingly awakened the spirits, who sought to reclaim their lost power. A brave archaeologist named Selene, determined to understand the past, joined forces with a rugged mercenary and a gifted mage. As they navigated the ruins, they uncovered secrets about the ancients\' downfall and the forces that had awakened them. In a gripping finale, Selene and her allies confronted the spirits, learning that understanding and respect could bridge the gap between past and present, restoring peace to the land.",
            "In the tranquil kingdom of Eldoria, a sinister shadow loomed, casting fear over its inhabitants. A young knight named Aric was tasked with investigating the source of the darkness. As he delved deeper, he discovered a conspiracy that reached the highest echelons of power. With the help of a rebellious thief and a wise old seer, Aric unraveled the mystery behind the shadow, which was tied to an ancient artifact hidden within the kingdom. In a thrilling climax, Aric confronted the corrupt nobles who sought to use the artifact for their gain, proving that courage and honor could restore hope to Eldoria.",
            "The Moonstone, a legendary gem said to possess the power to grant wishes, was thought to be a mere myth until it was discovered in a hidden cave. A determined young woman named Liora stumbled upon the Moonstone while searching for her lost brother. As she held the gem, she realized its power came with a price. Joined by a skeptical warrior and a cunning sorceress, Liora embarked on a quest to find her brother while navigating the dangers of the Moonstone\'s magic. In a heart-wrenching climax, she had to choose between using the gem to save her brother or protecting it from those who sought to exploit its power, ultimately learning the value of selflessness.",
            "Rumors of a fabled artifact, the Eye of Gennesis, began to spread throughout the land, promising untold power to its bearer. A young thief named Jax sought to claim the artifact for himself, believing it would grant him the respect he craved. However, he quickly found himself entangled in a web of deceit as other factions pursued the artifact. Teaming up with a fierce warrior and a clever diplomat, Jax navigated treacherous landscapes and encountered ancient guardians. In a dramatic showdown, he learned that true power lies not in possession but in the choices one makes, ultimately deciding to protect the artifact rather than seize it.",
            "In Gennesis, the Timekeeper maintained the flow of time, ensuring balance across the realm. When the Timekeeper was betrayed and trapped in a temporal rift, chaos ensued. A brave young woman named Aria was chosen to restore balance, guided by fragments of time left behind by the Timekeeper. As she traveled through various eras, she met historical figures and learned valuable lessons. With the help of a rogue time traveler and a wise sage, Aria confronted the traitor responsible for the Timekeeper\'s downfall. In a mind-bending finale, she used her newfound knowledge to repair the rift, restoring the Timekeeper and the stability of time itself.",
            "In the desert sands of Gennesis, an ancient tomb held secrets that could alter the fate of the realm. When a band of treasure hunters entered the tomb, they unwittingly unleashed a curse that threatened to consume the land. A courageous healer named Zara, whose village was affected by the curse, set out to stop the hunters and restore balance. Joined by a skilled archer and a mysterious wanderer, she navigated the treacherous tomb, facing traps and ancient guardians. In a gripping climax, Zara confronted the leader of the treasure hunters, using her healing magic to break the curse and teach the value of respecting history and the past.",
            "In the enchanted Forest of Eldralore, a heart-shaped gemstone known as the Heart of the Forest maintained the balance of nature. When it was stolen by a malevolent sorceress, the forest began to wither, and its magic faded. A determined ranger named Thorne was chosen to retrieve the Heart. Along his journey, he formed an unlikely alliance with a reclusive elf and a spirited druid. As they ventured deeper into the forest, they faced corrupted creatures and trials that tested their resolve. In a climactic battle against the sorceress, Thorne learned the true meaning of sacrifice and unity, ultimately reclaiming the Heart and restoring the forest\'s magic."
        ],
        "Hecarus":[
            "In the skies of Hecarus, the city of Zephyria floated among the clouds, hidden from the eyes of mortals. A curious young scholar named Elara stumbled upon ancient texts that spoke of its existence and the powerful Wind Crystals that kept it aloft. Determined to find the city, Elara embarked on a journey through treacherous mountain passes, guided by a weathered map and an eccentric sky pirate named Jarek. Together, they faced fierce storms and aerial creatures guarding the skies. Upon reaching Zephyria, they discovered that the Wind Crystals were fading, threatening the city\'s existence. In a dramatic climax, Elara harnessed her knowledge of ancient magic to restore the crystals, proving that intellect and courage could reshape destiny.",
            "In the heart of Eldran Forest, whispers of a dark force began to spread, corrupting the land and its inhabitants. A brave ranger named Thorne, known for his connection with nature, ventured into the woods to uncover the truth. Joined by a fiery sorceress named Lyra and a reformed thief named Finn, they journeyed deeper into the shadows. As they encountered twisted creatures and ancient spirits, Thorne learned that the darkness stemmed from a forgotten betrayal. In a heart-wrenching climax, the trio confronted the source of the corruption: a vengeful spirit of an ancient guardian. Thorne\'s compassion broke the cycle of hatred, healing the forest and restoring its beauty.",
            "In Hecarus, the legend of the Phoenix spoke of a fiery being that would rise to save the realm in its darkest hour. A young blacksmith named Kael dreamed of forging a weapon powerful enough to wield the Phoenix\'s flame. When a tyrant threatened to plunge Hecarus into eternal darkness, Kael set out to find the fabled Ember of the Phoenix. Accompanied by a wise elder and a fearless warrior, he traversed volcanic landscapes and faced tests of character. In a thrilling climax, Kael discovered that the true power of the Phoenix was not in destruction but in renewal. With the Ember, he forged a blade that ignited hope, rallying the people to rise against the tyrant.",
            "In Hecarus, the Veil Between Worlds separated the realm of mortals from the mystical domain of the Fae. A curious young woman named Mira accidentally tore the Veil while exploring an ancient shrine, allowing Fae creatures to invade her village. Realizing the chaos her actions caused, Mira sought to mend the Veil with the help of a brooding Fae prince named Aelion and a mischievous sprite. Together, they navigated the complexities of both worlds, facing dangers and misunderstandings. In a climactic showdown against an ancient force that sought to keep the Veil torn, Mira learned that understanding and empathy could bridge worlds, ultimately restoring harmony.",
            "Deep within the caverns of Hecarus lay ancient runes that held the key to untold power. A young archaeologist named Selene sought to uncover their secrets, believing they could bring peace to her war-torn homeland. Joined by a skeptical warrior and a cunning thief, Selene ventured into the darkness. As they deciphered the runes, they awakened an ancient guardian tasked with protecting the secrets. In a tense standoff, Selene realized that the true power of the runes lay in unity and cooperation. Together, they forged a pact, using the runes to heal the land and promote understanding among the warring factions.",
            "In the desert realms of Hecarus, a powerful serpent deity demanded tribute from the people to maintain the balance of nature. A brave young woman named Zara, tired of the sacrifices, sought to confront the deity. Accompanied by a clever merchant and a skilled warrior, she journeyed into the heart of the desert to find the Serpent\'s lair. Along the way, they encountered trials that tested their resolve and friendship. In a climactic confrontation, Zara challenged the deity, offering a pact of coexistence rather than submission. Her bravery and compassion impressed the Serpent, leading to a new era of balance where the people thrived alongside nature.",
            "In the grand city of Illumara, a mysterious mirror appeared in the central square, said to reveal one\'s true self. Curious citizens flocked to it, but the mirror\'s magic began to twist their reflections, leading to chaos. A young illusionist named Lyra, known for her skills in crafting illusions, took it upon herself to investigate. Joined by a loyal friend and a skeptical guard, they uncovered that the mirror was cursed by a powerful sorceress seeking revenge. In a heart-stopping climax, Lyra faced the sorceress, using her knowledge of illusions to turn the curse against her. By restoring the mirror\'s true magic, she helped the city rediscover its identity and strength.",
            "In the floating archipelago of Aetheris, the sky islands were governed by a council of aerial mages. When the council\'s power began to wane due to a rising faction of ground dwellers seeking independence, a young mage named Orion sought to mediate peace. He journeyed between the islands and the ground, forming unlikely alliances with both sides. As tensions escalated, Orion uncovered a plot to manipulate the council\'s decisions. In a dramatic confrontation, he revealed the truth, using his magic to unite the factions against a common foe. In a stunning finale, the council reformed, leading to a new era of cooperation between the sky and ground dwellers.",
            "In the enchanted Woodlands of Lumira, a luminous owl was said to be the guardian of wisdom. When the owl went missing, chaos ensued as nature began to falter. A determined herbalist named Elowyn embarked on a quest to find the owl, accompanied by her loyal wolf companion and a reclusive alchemist. They followed clues that led them through mystical realms and encountered ancient guardians. In a heart-wrenching climax, they discovered that the owl had been captured by a dark force seeking to steal its wisdom. Elowyn\'s compassion and courage ultimately freed the owl, restoring balance and reminding the realm of the importance of wisdom and understanding.",
            "In Hecarus, the Cycle of the Seasons was a sacred balance maintained by four elemental guardians: Winter, Spring, Summer, and Autumn. When the guardian of Winter vanished, the realm fell into chaos as the seasons began to blend. A spirited young woman named Thalia, a child of Spring, sought to restore balance. Joined by a stoic warrior of Winter and a wise elder of Autumn, they ventured to find the lost guardian. Along their journey, they faced elemental trials and learned the importance of each season\'s role in maintaining balance. In a climactic showdown, they confronted the dark force that sought to disrupt the cycle, ultimately restoring harmony and ensuring the Seasons continued to flow in unity."
        ],
        "Illonima":[
            "In the floating city of Aetheria, home to the Sky Mages, a young apprentice named Kaelin discovered an ancient tome containing the lost spells of the Aether. As he practiced the powerful magic, strange echoes began to manifest throughout the city, drawing the attention of a sinister cult seeking to harness the tome\'s power. With the help of a fierce warrior named Elara and a clever scholar named Tamsin, Kaelin delved into the mysteries of the tome. Their journey took them to hidden archives and forgotten ruins. In a thrilling climax, they faced the cult in a skyward battle, where Kaelin learned that true power comes from understanding and respect, ultimately sealing the tome\'s magic for the protection of Aetheria.",
            "In the realm of Illonima, an ancient artifact known as the Crystal of Harmony maintained balance between the kingdoms. When the crystal shattered, chaos ensued as rival factions fought for the shards. A determined diplomat named Seraphine was tasked with uniting the kingdoms to restore peace. Accompanied by a rogue with a mysterious past and a loyal knight, she embarked on a quest to retrieve the shards. As they navigated political intrigues and treacherous landscapes, Seraphine discovered the true history of the crystal and the bonds that once united the kingdoms. In a heart-pounding climax, she brokered a fragile alliance among the factions, leading to a final confrontation that restored the Crystal of Harmony and the unity of Illonima.",
            "In the mystical Emerald Woods, a guardian spirit known as the Green Warden had protected nature for centuries. When an industrialist sought to exploit the forest for its resources, the balance of life was threatened. A brave herbalist named Aria, who had a deep connection with the forest, vowed to protect her home. Joined by a band of unlikely allies—a reformed hunter and a cunning trickster—Aria ventured to awaken the Green Warden. They faced tests of loyalty and courage in the depths of the forest. In a climactic showdown against the industrialist's forces, Aria harnessed the power of nature itself, proving that the bond between humans and the earth could triumph over greed.",
            "In the coastal city of Tempest Bay, time itself was said to flow like the ocean waves. A mysterious tidal anomaly began to distort time, causing chaos in the lives of the inhabitants. A young time-weaver named Lira discovered that the anomaly was tied to a powerful relic hidden beneath the waves. Determined to restore the natural flow of time, she teamed up with a daring sea captain and a clever inventor. As they dove into the depths, they faced mythical sea creatures and unravelled the relic\'s secrets. In a breathtaking climax, Lira confronted the entity manipulating time, learning to embrace her own past in the process, ultimately restoring balance to Tempest Bay.",
            "Every century, the Celestial Convergence brought together the forces of light and darkness in Illonima. This year, a young warrior named Alaric was chosen to represent the Light, but he struggled with doubts about his worthiness. Guided by an enigmatic oracle, he set out to gather allies from across the realm: a fierce fire mage, a wise healer, and a mischievous shadow thief. As they journeyed together, they faced trials that tested their resolve and unity. In a climactic battle during the Convergence, Alaric learned to harness the strength of his friends, transforming doubt into power and defeating the dark forces seeking to disrupt the balance.",
            "In the tranquil waters of Siren\'s Cove, the melodies of the sirens were said to enchant all who heard them. However, when their songs began to fade, a young fisherman named Rowan discovered that an ancient curse was silencing them. Determined to save the sirens, he teamed up with a brave warrior and a talented bard. Together, they embarked on a quest to find the source of the curse. Their journey took them through perilous waters and hidden caverns, where they faced enchanting illusions and dangerous foes. In a heart-stopping climax, Rowan used his own voice to break the curse, allowing the sirens to reclaim their songs and restore harmony to the cove.",
            "In the grand city of Luminas, an ancient prophecy spoke of a hero who would rise to confront a great darkness. A young scholar named Mira stumbled upon fragments of the prophecy while researching in the Royal Library. As darkness began to creep into the city, she realized she might be the hero foretold. With the help of a reluctant knight and a charming rogue, she set out to piece together the remaining fragments of the prophecy. Their journey took them through treacherous landscapes and ancient ruins, leading to the heart of the darkness itself. In a gripping climax, Mira embraced her destiny, proving that courage and wisdom could light the way even in the darkest of times.",
            "In the vibrant city of Mirage, a mystical mask was said to grant its wearer the ability to manipulate reality. When the mask was stolen, chaos erupted as illusions blurred the line between truth and deception. A skilled illusionist named Thalia was drawn into the fray, determined to recover the mask and restore order. Joined by a skeptical detective and a street-smart pickpocket, Thalia navigated the tangled web of lies and treachery. In a thrilling climax, they confronted the thief in a battle of wits and illusions, ultimately revealing the truth behind the mask\'s power and restoring balance to Mirage.",
            "In the volcanic region of Pyrathos, the Flamekeeper protected the sacred fire that sustained life. When the fire was extinguished by a rival clan, the Flamekeeper\'s daughter, a brave young woman named Elowen, set out to reignite it. Joined by a rebellious fire mage and a loyal friend, she journeyed through treacherous terrain filled with lava and ash. Along the way, they discovered hidden truths about their ancestors and the importance of unity. In a climactic battle against the rival clan, Elowen\'s determination and sacrifice reignited the sacred fire, proving that courage could blaze a trail even through the darkest of times.",
            "In the depths of the Whispering Caves, a powerful serpent spirit offered forbidden knowledge to those brave enough to seek it. A young sorceress named Lysandra, desperate to save her ailing village, ventured into the caves to make a bargain with the serpent. Accompanied by a wise old sage and a spirited warrior, she navigated the challenges of the caves, confronting her deepest fears. In a climactic encounter, Lysandra realized that true knowledge came from within, rejecting the serpent\'s dark offer. Instead, she learned to harness her own magic, ultimately saving her village and proving that wisdom and courage could illuminate the darkest paths."
        ],
        "Jaguar":[
            "In the dense jungles of Jaguar, the Heart of the Jaguar, a legendary gemstone said to grant unparalleled power to its bearer, was hidden deep within sacred ruins. A young tracker named Xolotl, gifted with the ability to communicate with animals, set out on a quest to find the gem after a dark sorcerer threatened to unleash chaos upon the land. Joined by a fierce warrior named Itzel and a wise shaman, they navigated through treacherous terrain, facing mythical creatures and traps set to protect the gem. In a climactic battle against the sorcerer, Xolotl discovered that true strength came from unity and respect for nature, ultimately using the Heart\'s power to restore balance to the jungle.",
            "In a village shadowed by the towering peaks of the Jaguar Mountains, whispers of a curse plagued the inhabitants, leading to mistrust and fear. A brave young woman named Amara, whose family had been affected by the curse, sought the truth. With the help of an enigmatic stranger possessing knowledge of ancient magic and a skeptical hunter, she uncovered a hidden plot by a rival clan aiming to sow discord. As they delved deeper into the shadows, they faced illusions and confrontations that tested their loyalty. In a gripping climax, Amara confronted the true source of the curse, revealing that understanding and forgiveness could shatter even the darkest illusions.",
            "In the heart of Jaguar, a sacred flame burned brightly, symbolizing the spirit of the land. When the flame began to flicker, a young firekeeper named Tula was chosen to embark on a journey to reignite it. Accompanied by a rebellious spirit and an ancient guardian of the forest, Tula ventured through enchanted groves and treacherous paths. Along the way, they discovered forgotten rituals and the importance of harmony between fire and nature. In a climactic showdown against a malevolent force seeking to extinguish the flame forever, Tula learned that true power came not just from fire but from the love and respect for her surroundings, restoring the sacred flame and the spirit of the land.",
            "In the annual Festival of Jaguars, the spirit of the jaguar was said to bless the victor with unmatched strength and wisdom. A young athlete named Nahuel, determined to win for his village, trained tirelessly. However, as the festival approached, a dark rival from a neighboring village resorted to underhanded tactics to win. With the guidance of his wise grandmother and the support of his friends, Nahuel uncovered the rival\'s scheme and realized that the true essence of the festival was not just about winning but about community and respect. In a heart-stopping finale, Nahuel faced his rival, showcasing not only physical prowess but also integrity, earning the blessing of the jaguar spirit for all.",
            "In the realm of Jaguar, a mystical feather belonged to the legendary bird known as the Quetzal. It was said to grant the ability to see the truth hidden beneath illusions. When a corrupt chieftain seized the feather, the balance of the land began to unravel. A brave young woman named Cielo, determined to retrieve the feather, teamed up with a clever trickster and a steadfast warrior. Together, they navigated through enchanted forests and faced trials designed to test their resolve. In a thrilling climax, Cielo confronted the chieftain, using the feather\'s power to reveal the truth and rally the people against corruption, ultimately restoring harmony to the land.",
            "In the coastal village of Selva, a moonstone was said to bring prosperity and protection. However, when it was stolen by a malevolent sea witch, the village was plunged into despair. A determined fisherman named Eli, whose family depended on the sea, vowed to retrieve the moonstone. Joined by a fierce mermaid and a wise elder, he set out on a perilous journey beneath the waves. They faced treacherous currents and mythical sea creatures, unraveling the witch\'s dark magic. In a dramatic climax, Eli confronted the witch, learning that true bravery was not the absence of fear but the willingness to face it. He ultimately reclaimed the moonstone, restoring peace and prosperity to Selva.",
            "Deep within the Jaguar jungles, ancient spirits guided those who sought wisdom. A curious young man named Mateo yearned for guidance to lead his people. He embarked on a vision quest, seeking the wisdom of the Ancients. With the help of a skilled herbalist and a strong warrior, he traversed sacred grounds and faced trials of spirit and strength. As Mateo confronted his fears and doubts, he received visions that revealed the interconnectedness of all living beings. In a powerful climax, he returned to his village, ready to share the wisdom he had gained and inspire his people to live in harmony with nature.",
            "In the ancient city of Tzeltal, stone guardians protected the sacred temple of the jaguar. When a power-hungry warlord sought to claim the temple\'s secrets, a young priestess named Ximena was determined to stop him. Joined by a courageous warrior and a resourceful thief, they ventured into the depths of the temple to awaken the guardians. Facing trials and riddles, Ximena discovered the importance of sacrifice and selflessness. In a climactic battle against the warlord and his forces, she united her companions\' strengths to awaken the guardians, who rose to defend the temple. Together, they restored peace to Tzeltal, ensuring that the guardians would protect the land for generations to come.",
            "Every hundred years, the Blood Moon cast a red hue over Jaguar, signaling a time of great change. A young oracle named Luna received visions of impending disaster during this celestial event. With the help of a brave knight and a cunning rogue, she sought to decipher the prophecy and prevent the darkness from engulfing the land. As they traveled across jagged mountains and lush valleys, they faced trials that tested their loyalty and resolve. In a breathtaking climax, Luna faced the forces of darkness, using her visions to guide her friends in a battle that would determine the fate of Jaguar. Together, they turned the tide, transforming the Blood Moon\'s omen from despair to hope.",
            "In the hidden library of Jaguar, a keeper of ancient secrets held knowledge that could alter the course of history. When a powerful sorceress sought to steal this knowledge, a clever librarian named Isandro discovered her plans. With the help of a rebellious thief and a wise elder, he embarked on a quest to protect the library. As they faced magical traps and deceptive illusions, Isandro learned the importance of trust and courage. In a climactic showdown, he confronted the sorceress, using his wits to outsmart her and safeguard the library\'s secrets. Ultimately, Isandro realized that knowledge is most powerful when shared, inspiring a new generation to protect the wisdom of the past."
        ],
        "Kryptonian":[
            "In the distant reaches of the galaxy, the planet Krypton was home to a civilization known for its advanced technology and unparalleled powers. However, when the core of Krypton began to destabilize, panic spread among its inhabitants. A brilliant scientist named Zor-El discovered a way to save the planet using a powerful energy source from the heart of the sun. Joined by his courageous sister, Alura, and a team of elite warriors, Zor-El embarked on a perilous mission to harness the energy before it was too late. As they battled against corrupt leaders and their forces, they uncovered a conspiracy that threatened not just Krypton but the entire universe. In a heart-stopping climax, Zor-El and Alura united the people to harness their collective strength, ultimately saving Krypton from destruction.",
            "In the city of Kandor, a mysterious phantom began haunting the streets, spreading fear and chaos. A young Kryptonian named Kira, who possessed the ability to manipulate shadows, felt a strange connection to the phantom. Determined to uncover the truth, she enlisted the help of her childhood friend, a fearless soldier named Jax. Together, they delved into the city\'s hidden secrets and discovered that the phantom was actually a manifestation of unresolved grief from the city\'s past. In a thrilling confrontation, Kira faced her fears and embraced the shadows, ultimately bringing peace to the phantom and healing the city\'s wounds.",
            "In the upper echelons of Kryptonian society, the Celestial Council governed the planet\'s most powerful beings. When a powerful artifact known as the Crystal of Eternity was stolen, the council was thrown into disarray. A young envoy named Thorne was chosen to investigate the theft, joined by a fierce warrior and a cunning diplomat. As they traveled through treacherous lands, they encountered hidden factions and discovered a plot to overthrow the council. In a breathtaking climax, Thorne used his intelligence and diplomatic skills to unite the warring factions, revealing the true thief and restoring order to the council, proving that cooperation was stronger than division.",
            "In a time of peace, an ancient rivalry between the House of El and the House of Zod threatened to erupt once more. When a mysterious force began manipulating events to reignite the conflict, a brave warrior named Kal-El found himself caught in the middle. With the help of a wise mentor and a fierce ally from the House of Zod, he sought to uncover the truth behind the disturbances. As they faced ambushes and traps set by the manipulator, Kal-El learned the importance of unity and understanding. In an epic showdown, they confronted the true villain, a fallen Kryptonian who sought revenge. Kal-El\'s ability to forgive and unite the houses led to a new era of peace on Krypton.",
            "On Krypton, the worship of Rao, the sun god, was central to its culture. When a powerful cult arose, claiming to be the true emissaries of Rao, a devoted priestess named Lyra was determined to uncover their deception. Joined by a skeptical warrior and a young oracle, Lyra ventured into the cult\'s stronghold to expose their lies. As they infiltrated the cult, they faced dark rituals and tests of faith that pushed them to their limits. In a climactic battle, Lyra confronted the cult leader, revealing the true teachings of Rao and inspiring the followers to embrace the light rather than fear. Her courage transformed the cult into a force for good, uniting the people in faith and harmony.",
            "In a hidden temple, an ancient artifact known as the Timekeeper\'s Orb controlled the flow of time on Krypton. When a rogue faction sought to seize the orb, a young timekeeper named Orin discovered their plot. With the help of a resourceful engineer and a brave warrior, Orin embarked on a quest to protect the orb. As they navigated through time rifts and faced time-altering challenges, Orin learned about the consequences of tampering with fate. In a gripping climax, they confronted the rogue leader, who sought to rewrite history. Orin\'s understanding of time\'s delicate balance allowed them to restore the orb and protect Krypton\'s timeline.",
            "When an ancient Kryptonian starship, believed to be a myth, was discovered, a team of explorers led by the courageous pilot Zara set out to uncover its secrets. Joined by a skilled engineer and a knowledgeable historian, they embarked on a journey across the galaxy. As they traversed uncharted territories, they faced hostile alien species and navigated treacherous space phenomena. In a thrilling climax, they awakened the ship\'s long-dormant AI, which revealed hidden knowledge about Krypton\'s past. Zara\'s leadership and bravery united the crew, transforming them into legends as they returned to Krypton with newfound wisdom.",
            "In the Fortress of Solitude, an ancient guardian spirit protected the secrets of Kryptonian knowledge. When a dark sorcerer sought to claim the fortress for himself, a young scholar named Elara was determined to stop him. Joined by a skilled fighter and a wise sage, she journeyed into the fortress\'s depths to awaken its guardian. Facing trials that tested their minds and hearts, Elara discovered the importance of sacrifice and bravery. In a climactic battle against the sorcerer, Elara and her allies united their strengths, awakening the guardian to protect the fortress and preserve the knowledge of their ancestors.",
            "As Krypton faced a new threat from an alien empire, a coalition of warriors from different houses was formed to protect their homeland. A fierce general named Vex was chosen to lead the coalition, but internal strife threatened their unity. Determined to prove that they could overcome their differences, Vex sought the help of a young diplomat and a powerful warrior. Together, they navigated through tensions and rivalries, fostering alliances among the houses. In an epic climax, Vex and the coalition faced the alien empire in a battle that would determine the fate of New Krypton. Their unity and resolve triumphed over the invaders, ensuring a brighter future for their people.",
            "In the catacombs of Krypton, echoes of the past whispered secrets of the ancient civilization. A young archaeologist named Talia uncovered a hidden chamber filled with forgotten knowledge. Joined by a brave soldier and a curious child, she ventured deeper into the catacombs to learn about their ancestors. As they faced guardians and puzzles that protected the ancient wisdom, Talia realized the importance of her heritage. In a gripping finale, they uncovered a prophecy that foretold a great conflict. Talia\'s understanding of the past empowered her to guide her people, ensuring they would learn from their history rather than repeat it."
        ],
        "Lamania":[
            "In the heart of Lamania lies the Whispering Grove, a sacred forest where ancient spirits communicate through the rustling leaves. A young herbalist named Elowen discovers that the grove is fading, causing the spirits to become restless. Determined to save her home, she embarks on a quest to uncover the source of the grove\'s decline. Joined by a fierce protector named Kael and a clever trickster named Soren, they navigate through enchanted paths and face dark creatures threatening the grove. In a climactic confrontation with a shadowy entity seeking to drain the grove\'s magic, Elowen learns the importance of harmony between nature and humanity, ultimately restoring balance and peace to the Whispering Grove.",
            "The Crystal of Eternity, a powerful artifact hidden within the Temple of Ages, was said to grant the bearer the ability to manipulate time. When a ruthless warlord seeks to seize the crystal for his own gain, a young warrior named Thalia is chosen to protect it. Accompanied by a wise sage and a courageous knight, she embarks on a perilous journey to the temple. As they encounter treacherous landscapes and magical guardians, Thalia uncovers her own hidden potential. In a thrilling climax, she confronts the warlord, using her newfound abilities to protect the crystal and preserve the delicate flow of time in Lamania.",
            "In the majestic city of Eldoria, a dark sorceress threatens to plunge the realm into chaos. As the city prepares for a siege, a brave captain named Aric rallies his troops to defend their home. Among them is a talented mage named Lyra, whose unique powers hold the key to defeating the sorceress. Together, they devise a plan to infiltrate the enemy\'s ranks and gather intelligence. As the siege unfolds, Aric and Lyra must confront their deepest fears and insecurities. In a climactic battle, they unite the city\'s forces, inspiring hope and courage, ultimately driving back the sorceress and restoring peace to Eldoria.",
            "Rumors of ancient artifacts hidden throughout Lamania spark the interest of treasure hunters and adventurers alike. A skilled rogue named Jaxon teams up with a brave warrior named Selene to search for the fabled Sword of Light, said to possess the power to vanquish evil. Their journey takes them through treacherous ruins, enchanted caves, and forgotten temples, where they encounter magical creatures and traps designed to protect the artifacts. As they piece together clues from ancient texts, Jaxon and Selene develop a deep bond. In a thrilling finale, they confront a rival treasure hunter determined to claim the sword for himself, ultimately proving that the strength of their friendship is their greatest treasure.",
            "In the secluded village of Varyn, an oracle named Seraphine receives a vision of impending doom threatening Lamania. As dark clouds gather on the horizon, she seeks the help of a skeptical warrior named Rael and a curious scholar named Mira. Together, they interpret the oracle\'s cryptic message and set out on a quest to prevent the disaster. Their journey takes them across diverse landscapes and through ancient ruins, where they uncover forgotten lore about Lamania\'s past. In a heart-pounding climax, they confront the source of the darkness and realize that the power to change fate lies within them, allowing them to avert disaster and bring hope to their land.",
            "Every year, Lamania hosts a grand masquerade ball, where magic and intrigue intertwine. This year, a mysterious figure known only as the Phantom has stolen a powerful artifact during the festivities. A talented dancer named Elara, who possesses the ability to see glimpses of the future, teams up with a charming thief named Dorian to uncover the Phantom\'s identity and recover the artifact. As they navigate the glamorous yet dangerous world of the masquerade, they encounter secrets, betrayals, and unexpected alliances. In a thrilling climax, Elara\'s foresight leads them to confront the Phantom, revealing a shocking connection to their past that changes everything.",
            "In the coastal town of Eldermere, a powerful sea serpent cursed the waters, bringing storms and despair to the fishermen. A courageous sailor named Finn, determined to save his village, sets sail with a wise old mariner and a spirited healer. They journey across turbulent seas, facing mythical creatures and treacherous waters, in search of the serpent\'s lair. As they uncover the truth behind the curse, they realize that the serpent is guarding a sacred treasure. In a climactic encounter, Finn learns that compassion and understanding can break the curse, leading to a resolution that restores harmony between the town and the serpent.",
            "Deep within the archives of Lamania, an ancient prophecy speaks of a hero destined to unite the fractured kingdoms. A young scribe named Alaric discovers the prophecy while researching his family\'s history. As tensions rise between the kingdoms, Alaric teams up with a fierce warrior and a cunning diplomat to fulfill the prophecy and bring peace to the land. Their journey takes them through political intrigue and treacherous alliances, where they must navigate the challenges of leadership and sacrifice. In a gripping climax, Alaric uncovers the true meaning of the prophecy, realizing that unity and understanding are the keys to a brighter future for Lamania.",
            "In a world where dreams hold immense power, a Dreamweaver named Isolde is tasked with protecting the realm from nightmares that threaten to invade the waking world. When a rogue Dreamweaver seeks to unleash chaos through a powerful nightmare, Isolde must confront her fears. Joined by a brave knight and a clever trickster, they enter the realm of dreams to face the rogue in an epic duel. As they navigate surreal landscapes and face their own nightmares, Isolde discovers the strength of her own dreams. In a thrilling climax, she confronts the rogue, using her newfound abilities to protect both worlds and restore harmony.",
            "The Guardians, ancient protectors of Lamania, have grown weak over the centuries. A young guardian named Kaelin is determined to awaken the lost spirits of his ancestors. With the help of a talented healer and a brave warrior, he embarks on a quest to recover sacred relics that hold the key to restoring the Guardians\' power. Their journey leads them to forgotten temples and treacherous realms, where they face powerful foes and unlock hidden potential. In a climactic battle, Kaelin and his allies awaken the spirits of the Guardians, uniting their strength to protect Lamania from an impending darkness, ensuring that the legacy of the Guardians endures."
        ],
        "Marverick":[
            "In the bustling city of Eldron, a dark cult known as the Shadow Brotherhood has begun to rise, threatening to plunge Marverick into chaos. A brave knight named Sir Cedric, sworn to protect the realm, discovers their plot to awaken an ancient evil. Joined by a fierce rogue named Mira and a wise mage named Elowen, they embark on a quest to gather allies and uncover the cult\'s secrets. As they journey through treacherous landscapes and face powerful foes, Cedric learns that the strength of friendship and trust is essential in their battle against darkness. In a climactic showdown, they confront the cult\'s leader, ultimately thwarting their plans and restoring peace to Eldron.",
            "In the kingdom of Aeloria, a young woman named Lyra discovers she is the last surviving heir to the throne, hidden away since infancy. When her village is attacked by mercenaries seeking the royal lineage, she must flee. With the help of a skilled warrior named Aric and a cunning bard named Finn, Lyra sets out to reclaim her birthright. As they navigate political intrigue and face betrayal, they uncover a conspiracy that threatens the entire kingdom. In a thrilling climax, Lyra confronts the usurper who has taken her family\'s throne, using her newfound strength and the bonds she has forged to reclaim her destiny.",
            "In the Elemental Realm, where fire, water, earth, and air collide, the balance of power has been disrupted. A young elemental mage named Kaelin is chosen to undergo the Elemental Trials, a series of challenges designed to restore harmony. Accompanied by a fierce fire elemental named Ember and a stoic earth guardian named Flint, Kaelin faces trials that test their skills and resolve. As they navigate the challenges, they learn to harness their powers and work together. In a climactic battle against a rogue elemental threatening to engulf the realm in chaos, Kaelin realizes that unity among the elements is the key to overcoming darkness.",
            "In the steampunk city of Gearhaven, where machines and magic coexist, a brilliant inventor named Tinker discovers a plot to seize control of the city\'s technology. With the help of a savvy engineer named Lila and a rogue with a mysterious past, Tinker races against time to unravel the conspiracy. As they delve deeper into the underbelly of Gearhaven, they uncover secrets that could change the fate of the city. In a thrilling climax, Tinker and his friends confront the mastermind behind the plot, revealing the importance of innovation and collaboration in overcoming tyranny.",
            "In the mountainous regions of Marverick, a powerful dragon named Zephyra guards a sacred treasure known to bestow immense power. When a band of mercenaries attempts to steal it, a young dragon rider named Aiden must intervene. With the help of a wise mentor and a fierce dragoness named Ember, Aiden seeks to forge an alliance with Zephyra. As they navigate the treacherous landscape and face the mercenaries, Aiden learns the true meaning of loyalty and respect for nature. In a climactic battle, Aiden and his allies unite with Zephyra to protect the treasure, ensuring that its power is used for the greater good.",
            "Deep beneath the waves of Marverick lies an ancient civilization shrouded in mystery. A daring explorer named Selene is determined to uncover its secrets. Joined by a skilled navigator and a sea creature with the ability to communicate, Selene embarks on an underwater adventure. As they dive into the abyss, they encounter strange creatures and ancient traps guarding the civilization\'s treasures. In a thrilling climax, Selene uncovers the truth behind the civilization\'s fall and learns that knowledge must be protected and shared responsibly to prevent history from repeating itself.",
            "Every hundred years, a meteor shower known as the Starfall grants incredible powers to those chosen by fate. When the prophecy is revealed, a young mage named Orion discovers he is destined to harness its energy. Joined by a skeptical warrior named Kael and an enthusiastic herbalist named Lyra, they embark on a quest to retrieve the falling stars. As they encounter rival factions and face their own fears, they learn the true meaning of destiny. In a climactic moment, Orion must confront the consequences of wielding such power, ultimately choosing to use it to protect the realm rather than for personal gain.",
            "In the ancient library of Eldoria, a forbidden tome holds secrets of dark magic that could alter the fabric of reality. A curious scholar named Alina stumbles upon it and inadvertently unleashes a powerful curse. With the help of a brave knight and a reformed thief, Alina must gather the pieces of a counter-curse scattered across Marverick. As they face dark forces and navigate moral dilemmas, Alina learns the importance of responsibility and the consequences of knowledge. In a climactic showdown, they confront the dark entity released by the tome, ultimately sealing it away and safeguarding the realm.",
            "In the quiet village of Elden, legends speak of forgotten heroes who once protected Marverick. When dark forces begin to rise, a group of unlikely allies—an aging warrior, a mischievous bard, and a timid healer—decide to uncover the truth behind the legends. Their journey leads them to ancient ruins and long-lost artifacts, revealing the importance of courage and sacrifice. In a climactic battle, they find themselves facing the very darkness that threatened their ancestors, proving that heroism can be found in even the most unexpected places.",
            "The Celestial Guardians, ancient beings tasked with maintaining the balance of magic in Marverick, have been weakened by a mysterious force. A young guardian named Aria sets out on a quest to restore their power. Joined by a loyal companion and a skilled archer, she travels through enchanted realms and faces powerful adversaries. As Aria uncovers the truth about her lineage and the origins of the Guardians, she learns the importance of embracing her identity. In a thrilling climax, she rallies the Guardians to confront the dark force threatening to engulf Marverick, ultimately restoring balance and hope."
        ],
        "Nemesis":[
            "In the heart of Nemesis, a cataclysmic rift opens between the realms of light and shadow. A brave warrior named Kaelan discovers that he possesses the unique ability to traverse this rift. When a dark force begins to spill into his homeland, threatening to consume everything in darkness, Kaelan teams up with a skilled shadowmancer named Elara. Together, they venture into the shadow realm to find the source of the darkness. As they navigate through treacherous landscapes and encounter dark creatures, they learn that the true enemy lies not just in the shadows but within their own hearts. In a climactic showdown, Kaelan must confront his fears and insecurities to seal the rift and restore balance.",
            "In the once-thriving city of Aeloria, a traitor has emerged among the ranks of the guardians sworn to protect it. A young guardian named Lira is determined to uncover the identity of the betrayer before it\'s too late. As she delves deeper into the city\'s politics, she finds herself tangled in a web of deceit and betrayal. With the help of a resourceful rogue named Darius and a loyal mentor, she uncovers clues that lead her to unexpected allies and hidden enemies. In a thrilling climax, Lira confronts the betrayer in a tense standoff, realizing that trust is both a weapon and a vulnerability in a world rife with deception.",
            "A powerful phoenix known as Ashara has been captured by a nefarious warlord seeking to harness her flames for destruction. A daring warrior named Orion sets out to rescue her, believing that the phoenix holds the key to restoring peace to the land. Joined by a fierce fire mage and a wise old sage, Orion embarks on a quest filled with perilous battles and ancient prophecies. As they face the warlord\'s forces, they uncover a deeper connection between Ashara and the fate of Nemesis itself. In a breathtaking finale, Orion and his companions unite their strengths to free Ashara, igniting a flame of hope that spreads across the land.",
            "Deep within the mystical forests of Nemesis lies the Mirror of Truth, a legendary artifact that reveals the true nature of those who gaze upon it. When a corrupt nobleman seeks to claim its power for his own gain, a young seer named Mira must protect it. With the help of a brave knight and a cunning thief, they embark on a journey to safeguard the mirror. Along the way, they confront their own insecurities and fears as they learn to embrace their true selves. In a climactic battle, they face the nobleman and his dark forces, ultimately using the power of the mirror to expose his true nature and restore justice.",
            "The factions of light and shadow have been at war for centuries, and the conflict reaches a boiling point when an ancient artifact known as the Eclipse Stone resurfaces. A soldier named Thorne, torn between loyalty to his light faction and the truth he uncovers about the shadows, seeks to end the war once and for all. With the help of a renegade shadow mage named Selene, Thorne embarks on a journey to uncover the origins of the Eclipse Stone. As they delve deeper into the history of their world, they realize that the key to peace lies in understanding and accepting their differences. In a gripping climax, they confront the leaders of both factions, revealing the truth and forging a new alliance.",
            "In a hidden sanctuary known as the Celestial Forge, ancient weapons are crafted using the essence of stars. When a dark sorcerer seeks to corrupt the forge for his own nefarious purposes, a young blacksmith named Kael must protect it. Teaming up with a celestial warrior and an astute scholar, Kael embarks on a quest to find the lost shards of the Star Blade, the only weapon capable of defeating the sorcerer. As they traverse the realms, they encounter legendary creatures and face trials that test their strength and resolve. In a climactic battle, Kael and his allies confront the sorcerer, proving that true power comes not just from weapons, but from the heart.",
            "In the enchanted city of Illusara, a powerful illusionist known as Zarin has cast a veil over the city, trapping its inhabitants in a world of deception. A young mage named Elowen, gifted with the ability to see through illusions, is determined to break the spell. Joined by a skeptical knight and a mischievous trickster, Elowen embarks on a quest to uncover Zarin\'s true intentions. As they navigate the labyrinth of illusions, they face their own fears and insecurities. In a thrilling climax, Elowen confronts Zarin, using her gift to reveal the truth and liberate the city from the illusionist\'s grasp.",
            "In the ancient ruins of Nemesis, colossal stone titans lie dormant, waiting to be awakened. When a power-hungry warlock seeks to harness their strength, a courageous archaeologist named Lyra discovers the plot and must act quickly. With the help of a valiant guardian and a wise historian, she embarks on a quest to awaken the titans before they fall into the wrong hands. As they uncover the titans\' secrets and history, they learn that the titans were once protectors of balance in the realm. In a climactic confrontation, Lyra and her allies awaken the titans, who rise to reclaim their role as guardians of Nemesis.",
            "Legend speaks of a lost city, Veilara, said to hold treasures and knowledge beyond imagination. A daring explorer named Jaxon discovers a map leading to its location and assembles a team of adventurers to uncover its secrets. Among them are a fierce warrior, a clever rogue, and a knowledgeable sage. As they navigate treacherous terrain and face ancient guardians, they uncover the city\'s dark past and the reason for its disappearance. In a gripping climax, Jaxon and his companions confront the forces that protect the city, ultimately learning that some treasures are meant to be guarded, not possessed.",
            "In the tempestuous skies of Nemesis, storms rage and threaten to tear the world apart. A gifted stormcaller named Aria is tasked with calming the storms but soon discovers that a malevolent force is manipulating the weather. Joined by a brave sky pirate and a wise old hermit, Aria embarks on a journey to uncover the truth. As they traverse stormy skies and face fierce winds, they learn to harness their own powers and confront their fears. In a climactic battle against the dark force controlling the storms, Aria discovers the strength within herself and her allies, ultimately restoring peace to the skies of Nemesis."
        ],
        "Onyx":[
            "In the heart of Onyx lies a powerful sigil that maintains the balance of magic across the realm. When a dark sorceress named Morwen shatters the sigil to unleash chaos, a young mage named Kaelin is thrust into a quest to restore it. Accompanied by a stoic warrior named Thorne and a clever rogue named Lira, Kaelin embarks on a perilous journey to gather the pieces of the shattered sigil. As they face treacherous landscapes and dark creatures, Kaelin learns to harness his own latent powers. In a climactic battle against Morwen, they unite their strengths to restore the sigil, bringing balance back to Onyx.",
            "In the ancient city of Eldrath, a series of mysterious disappearances plague the citizens. A curious historian named Elara discovers clues leading to the fabled Temple of the Ancients, rumored to hold secrets of immense power. With the help of a skeptical knight named Garrick and a resourceful thief named Jaxon, Elara sets out to uncover the truth. As they navigate traps and riddles within the temple, they unravel the mysteries of the Ancients and their connection to the present. In a thrilling climax, they confront the dark force behind the disappearances, learning that knowledge must be wielded with wisdom.",
            "Deep within the Moonlit Forest, legends tell of a phantom who guards a hidden treasure. When a ruthless band of treasure hunters enters the forest, a brave ranger named Lyra must protect the phantom and the treasure. Teaming up with a skilled archer and a wise old druid, Lyra embarks on a mission to confront the hunters. As they delve deeper into the forest, they encounter magical creatures and unravel the secrets of the phantom\'s past. In a climactic encounter, they defend the forest against the hunters, revealing the true nature of the treasure: the harmony between nature and magic.",
            "In the Kingdom of Obsidian, a crystal known for revealing glimpses of the future has gone missing. A young seer named Orion sets out to retrieve it, believing it holds the key to preventing a looming disaster. Joined by a fierce warrior named Kaela and a cunning diplomat named Darius, Orion navigates a web of political intrigue and dark conspiracies. As they uncover clues leading to the crystal\'s whereabouts, they realize that the future is not set in stone. In a gripping climax, they confront those who seek to manipulate the crystal for their own gain, learning that true power lies in choices made in the present.",
            "In a time of unrest, the spirit of a legendary warrior awakens to protect Onyx from an impending invasion. A young blacksmith named Elysia discovers the warrior\'s ancient armor, which grants her the power to wield his strength. With the help of a brave knight and a wise sage, she embarks on a quest to awaken the warrior\'s spirit fully. As they face dark forces and rally allies, Elysia learns that true heroism comes from within. In a climactic battle against the invaders, she channels the warrior\'s strength and proves that courage and compassion can turn the tide of war.",
            "In the depths of the Shadow Realm, a labyrinth holds the key to untold power. A young adventurer named Finn stumbles upon the entrance and is drawn inside, where he must navigate ever-shifting paths and illusions. Guided by a mysterious voice and aided by a brave companion, Finn must confront his own fears and insecurities. As he unravels the labyrinth\'s secrets, he discovers the truth about his lineage and the role he must play in the world of Onyx. In a thrilling climax, Finn faces the shadowy guardian of the labyrinth, ultimately emerging stronger and more self-aware.",
            "In the western lands of Onyx, a powerful witch named Selene has been rumored to curse anyone who dares to enter her domain. A determined herbalist named Aiden sets out to confront her, seeking the truth behind the curses. With the help of a skilled healer and a brave knight, he navigates the treacherous terrain and uncovers the witch\'s tragic past. As they confront Selene, they learn that her curses stem from pain and loss. In a heartwarming climax, they offer her understanding and compassion, breaking the cycle of hatred and forging a new alliance.",
            "In Onyx, the veil between the human realm and the realm of spirits is thin, and a malevolent force seeks to exploit it. A gifted spiritwalker named Talia is called to action when spirits begin to vanish. With the help of a loyal friend and a reclusive shaman, Talia embarks on a journey to restore the balance between the realms. As they delve into the spirit world, they encounter challenges that test their resolve and friendships. In a climactic confrontation, Talia confronts the dark entity threatening the spirits, ultimately learning that love and connection transcend even the deepest divides.",
            "In the heart of the city of Onyx, an alchemist named Lucian uncovers a hidden formula that grants the power to transmute matter. When his discovery falls into the hands of a power-hungry noble, Lucian must team up with a determined thief named Rhea and a brilliant scholar to retrieve it. Their journey leads them through the underbelly of the city, where they face rival factions and dark forces. As they unravel the alchemist\'s secret, they discover that true wealth lies not in power, but in knowledge and community. In a thrilling climax, they confront the noble, reclaiming the formula and using it to benefit the people of Onyx.",
            "Deep within the ancient mountains of Onyx lies the Heart of Onyx, a legendary gem that grants immense power. When a dark sorceress named Valeria seeks to claim it for herself, a band of unlikely heroes—including a young thief, a noble knight, and a wise wizard—set out to protect the gem. Their journey takes them through treacherous terrain and magical obstacles, where they must confront their own inner demons. In a climactic showdown, they face Valeria and her minions, learning that the true power of the Heart lies not in domination, but in unity and sacrifice. Together, they ensure that the Heart of Onyx remains a source of hope for the realm."
        ],
        "Palladian":[
            "In Palladian, every century, the stars align to create the Celestial Convergence, a rare event that amplifies magical powers. As the date approaches, a young sorceress named Lira learns that an ancient artifact known as the Starheart is hidden in the depths of the Celestial Caverns. With her mentor, a wise old mage named Eldrin, and a daring rogue named Jax, Lira embarks on a perilous quest to retrieve it. Along the way, they face mythical creatures and traps set by those who seek the artifact for themselves. In a climactic showdown, Lira must tap into her true potential to harness the power of the Starheart, ensuring that it does not fall into the wrong hands.",
            "In the enchanted Whispering Woods, a dark force begins to corrupt the magical flora and fauna. A courageous druid named Thalia discovers that the source of the corruption is an ancient spirit trapped in a twisted form. Joined by a skilled ranger and a knowledgeable herbalist, Thalia ventures deep into the heart of the woods to restore balance. They encounter enchanted creatures and face challenges that test their resolve and friendship. As they confront the corrupted spirit, Thalia learns that compassion and understanding are the keys to healing both the land and the spirit, ultimately restoring harmony to the Whispering Woods.",
            "The kingdom of Eldoria has been cursed by a vengeful sorceress, plunging it into eternal darkness. A young prince named Aric, desperate to save his people, sets out to find the fabled Crystal of Dawn, said to possess the power to break the curse. Along his journey, he is joined by a fearless warrior named Kaela and a wise seer named Miri. Together, they traverse dangerous landscapes and face trials that challenge their loyalty and courage. In a thrilling climax, Aric must confront the sorceress and make a choice that will determine the fate of his kingdom, ultimately discovering that love and sacrifice can conquer even the darkest of curses.",
            "When a fallen star crashes into Palladian, it brings with it a powerful entity known as the Luminary. A curious astronomer named Finn discovers the Luminary\'s existence and learns that it possesses knowledge of the universe. However, dark forces seek to capture the Luminary for their own ambitions. Finn, along with his childhood friend and aspiring mage, Elara, embark on a quest to protect the Luminary. They face bounty hunters and navigate treacherous terrains as they uncover the truth behind the fallen star. In a heart-pounding climax, they confront the dark forces, and Finn learns that true knowledge is best shared, ultimately helping the Luminary return to the stars.",
            "In a realm divided between light and shadow, a prophecy foretells the rise of a Shadowbearer, one who can wield the powers of both realms. A young outcast named Aiden discovers his connection to the prophecy and sets out to master his abilities. Along the way, he meets a fiery warrior named Zara, who believes in his potential. Together, they embark on a journey to unite the two factions, facing prejudice and danger at every turn. As Aiden learns to harness his powers, he uncovers secrets that could change the fate of Palladian. In a climactic battle against the forces of darkness, Aiden must embrace his duality to fulfill the prophecy and bring balance to the realm.",
            "In the bustling city of Alchemoria, a talented alchemist named Seraphina discovers a formula for a potion that grants unimaginable power. However, her discovery attracts the attention of a ruthless criminal organization intent on seizing it. With the help of her enigmatic mentor and a street-smart thief, Seraphina must navigate the underbelly of the city to protect her formula. As they unravel the conspiracy behind the organization, Seraphina learns about the ethical implications of her discovery. In a thrilling climax, she faces the leader of the organization, ultimately deciding to use her skills for the greater good rather than personal gain.",
            "A mysterious artifact known as the Timekeeper has the ability to manipulate time itself. When it is stolen from the Grand Library, a gifted historian named Lucian is tasked with retrieving it. Joined by a resourceful time mage and a reluctant thief, Lucian embarks on a quest through different eras of Palladian\'s history. As they travel through time, they encounter legendary figures and face challenges that test their knowledge and wit. In a race against time, they must confront the thief and secure the Timekeeper before history is irrevocably altered. In the end, Lucian learns that understanding the past is vital for shaping the future.",
            "In the oppressive kingdom of Drakar, a group of rebels seeks to overthrow a tyrannical ruler who has banned magic. A brave fire mage named Nyra becomes the reluctant leader of the rebellion after witnessing the destruction of her village. With the help of a skilled warrior and a charismatic bard, Nyra rallies allies and orchestrates daring missions against the king\'s forces. As they face insurmountable odds, they uncover hidden truths about the ruler\'s past and the source of his power. In a climactic battle, Nyra must ignite the flames of hope within her people, proving that unity and courage can bring about change.",
            "In the coastal town of Merrow\'s Edge, sailors are mysteriously disappearing, lured by a haunting melody. A determined fisherman named Rowan sets out to uncover the truth behind the siren\'s song. Joined by a brave sailor and a wise marine biologist, they dive into the depths of the ocean to confront the siren, revealing her tragic past. As they navigate the dangers of the deep sea, they learn that the siren\'s song is a cry for help, not a lure for destruction. In a heartwarming climax, they help her find peace, restoring harmony between the sea and the townsfolk.",
            "In a hidden academy for magical studies, a gifted student named Elowen discovers a long-lost tome that holds the secrets of ancient magic. As she delves deeper into its pages, she learns that a dark force seeks to reclaim the tome for nefarious purposes. With the help of her closest friends—a talented illusionist and a fearless fighter—Elowen embarks on a quest to protect the legacy of the arcane. As they face trials and uncover hidden truths about their own magical abilities, they learn that knowledge must be safeguarded for the future. In a climactic battle, Elowen and her friends confront the dark force, proving that the bonds of friendship and knowledge are the true essence of magic."
        ],
        "Quasar":[
            "In the heart of Quasar, a celestial forge known as the Starfire Anvil holds the power to create legendary weapons infused with the essence of stars. When a tyrant known as Lord Xypher seeks to control the forge, a young blacksmith named Lyra discovers her unique ability to manipulate starlight. Joined by a daring space pirate and a wise scholar, she embarks on a quest to protect the forge from falling into Xypher\'s hands. As they journey through cosmic storms and ancient ruins, Lyra learns that true strength comes from within. In a climactic showdown, she channels the power of the forge to forge a weapon that can turn the tide of battle.",
            "A mysterious signal emanates from the Void, a dark and uncharted region of Quasar. A team of brave explorers, led by Captain Orion, ventures into the abyss to uncover the source of the echoes. Alongside his loyal crew, including an enigmatic navigator and a brilliant scientist, they face unimaginable dangers and cosmic anomalies. As they delve deeper, they discover an ancient civilization lost to time, revealing secrets that could alter the fabric of reality. In a thrilling climax, they confront an ancient entity that guards the truth, ultimately deciding the fate of their universe.",
            "In Quasar, a group of elite warriors known as the Cosmic Guardians protects the realm from interstellar threats. When a powerful artifact called the Celestial Prism is stolen, the Guardians must track it down before it can be used for destruction. A rookie Guardian named Kira, eager to prove herself, joins the mission alongside a seasoned veteran and a rogue with questionable loyalties. As they journey across planets and face off against mercenaries, Kira learns about sacrifice, trust, and the true meaning of heroism. In an epic finale, they confront the artifact\'s new owner, and Kira must tap into her potential to save Quasar from impending doom.",
            "In a vibrant nebula known for its breathtaking beauty, a rare flower blooms once a century, said to hold the essence of the universe. A botanist named Elion seeks the Nebula\'s Heart to harness its power for good. However, dark forces also covet the flower, led by a ruthless warlord who desires its energy for his own ambitions. Elion teams up with a fierce warrior and a clever strategist to protect the flower and ensure it remains untainted. As they traverse the nebula\'s wonders, they face numerous challenges that test their resolve. In a dramatic climax, they confront the warlord, learning that true power lies in preserving nature and balance.",
            "A catastrophic event shatters a constellation that has guided travelers for centuries, plunging Quasar into chaos. A determined astronomer named Zane discovers that the pieces of the constellation hold the key to restoring order. With the help of an adventurous pilot and a skilled mechanic, Zane embarks on a quest to recover the fragments scattered across the cosmos. Along the way, they encounter strange phenomena and cosmic beings, each with their own stories. In a heart-pounding finale, they gather the fragments and confront the forces trying to exploit the chaos, restoring the constellation and peace to Quasar.",
            "In Quasar, the Timekeeper maintains the flow of time across the cosmos. When he goes missing, time begins to unravel, causing events to loop and distort. A young time mage named Mira sets out to find the Timekeeper, joined by a loyal guardian and a cunning thief. As they traverse the timelines, they must solve riddles and confront past versions of themselves. Along their journey, Mira learns about the consequences of time manipulation and the importance of choices. In a thrilling climax, they confront a rogue time manipulator who seeks to control time for personal gain, ultimately restoring the balance of time in Quasar.",
            "As tensions rise between two powerful galaxies, a reluctant diplomat named Alaric is sent as an envoy to broker peace. Accompanied by a skilled pilot and a fierce warrior, he must navigate the complex politics and deep-rooted animosities between the factions. As he uncovers a conspiracy aimed at igniting war, Alaric realizes that he must unite the galaxies before it\'s too late. Facing betrayal and danger at every turn, he learns the true value of trust and cooperation. In a dramatic finale, Alaric orchestrates a plan to bring both sides together, proving that peace is worth fighting for.",
            "A notorious group of thieves plans an audacious heist to steal a powerful artifact from the Galactic Museum. A master thief named Cassian is reluctantly pulled back into the game when his estranged sister is kidnapped by the gang. With the help of a tech-savvy hacker and a former Guardian, Cassian must navigate the underworld of Quasar to rescue her. As they infiltrate the museum, they face high-tech security and unexpected challenges. In a thrilling climax, Cassian confronts the leader of the gang, realizing that family bonds are stronger than any treasure.",
            "A rift opens between Quasar and a dark parallel universe, unleashing chaos and dark creatures into the realm. A brave knight named Selene is chosen to close the rift, but she cannot do it alone. Teaming up with a rebellious sorcerer and a resourceful engineer, Selene embarks on a quest to gather the ancient artifacts needed to seal the rift. As they face trials and confront their own fears, they learn about courage, friendship, and the strength found in unity. In a climactic battle against dark forces, Selene and her team must harness their combined powers to restore balance to Quasar.",
            "A legendary tome containing the knowledge of the Ancients is discovered, sparking a race among factions to claim its power. A young scholar named Aisling, driven by her desire to protect the knowledge, sets out to find the tome first. Joined by a skeptical warrior and an adventurous historian, she embarks on a quest filled with peril and intrigue. As they uncover the secrets of the Ancients, they learn about the consequences of power and the responsibility that comes with it. In a gripping finale, they confront those who wish to misuse the tome, proving that true wisdom lies in understanding and sharing knowledge for the greater good."
        ],
        "Riverven":[
            "In the heart of Riverven, the Luminous Oracle grants visions of the future to those who seek its wisdom. When a dark sorcerer named Kael attempts to seize the Oracle\'s power for his own ambitions, a brave young seer named Elara steps forward to protect it. Accompanied by a loyal knight and a cunning rogue, she embarks on a quest to unlock the Oracle\'s secrets. As they navigate treacherous landscapes and face mystical creatures, Elara learns that the future is not set in stone. In a thrilling climax, she confronts Kael, using her newfound understanding of fate to protect the Oracle and preserve the balance of Riverven.",
            "Deep within Riverven lies the Enchanted Grove, a sacred place where ancient spirits dwell. When a blight threatens the grove, a passionate druid named Thorne seeks to uncover its source. With the help of a spirited healer and a skeptical hunter, Thorne embarks on a journey to restore the grove. Along the way, they encounter magical beings and unravel the secrets of the forest. As they confront the dark force corrupting the grove, Thorne discovers the true power of nature and the importance of harmony between all living beings. In a climactic battle, they unite their strengths to heal the grove and banish the darkness.",
            "The kingdom of Eldoria is in turmoil after the royal crown, a symbol of unity and peace, is stolen. A courageous young thief named Rylan finds himself caught in the midst of a conspiracy. To clear his name, he teams up with a headstrong princess and a disgraced knight. Together, they delve into the depths of Eldoria\'s underbelly, uncovering dark secrets and hidden agendas. As they race against time to retrieve the crown, Rylan learns that true bravery comes from standing up for what is right. In a gripping climax, they confront the mastermind behind the theft, restoring the crown and unity to the kingdom.",
            "An ancient prophecy speaks of a hero who will rise to save Riverven from impending doom. When the signs begin to manifest, a humble blacksmith named Aric discovers that he is the prophesied hero. Reluctant to accept his fate, he sets out on a quest to understand his role. Along the way, he is joined by a fierce warrior and a wise sage. Together, they uncover the truth behind the prophecy and confront the dark forces threatening Riverven. In a thrilling finale, Aric embraces his destiny, discovering that heroism lies in the choices one makes, not just in fate.",
            "A rare crystal known for its ability to amplify magic is hidden within the depths of the Whispering Caves. When a power-hungry warlock learns of its existence, a brave mage named Isolde must protect it. Joined by a rogue with a mysterious past and a loyal companion, Isolde embarks on a perilous journey. As they traverse the caves, they face illusions and magical traps. Along the way, Isolde discovers her own latent powers and learns the importance of friendship and trust. In a climactic confrontation, they confront the warlock, using the crystal\'s magic to defeat him and protect Riverven.",
            "In Riverven, a forbidden path known as the Shadowed Trail leads to untold riches and dangers. A group of treasure hunters, led by the ambitious captain Lira, ventures into the shadows, unaware of the consequences that await them. Among them is a reluctant healer who harbors a dark secret. As they navigate the treacherous terrain, they encounter ancient guardians and unravel a curse that haunts the path. In a thrilling climax, Lira must confront her greed and make a choice that could save or doom her team, ultimately learning that some treasures are not worth the price.",
            "In a forgotten village, a wraith emerges, seeking vengeance for a past betrayal. A brave young woman named Mira, whose family was affected by the wraith\'s curse, sets out to uncover the truth. Joined by a fearless warrior and a wise elder, she delves into the village\'s dark history. As they piece together the wraith\'s story, Mira learns about forgiveness and the power of redemption. In a gripping finale, they confront the wraith, offering it the chance to find peace, ultimately breaking the cycle of vengeance and restoring harmony to the village.",
            "In Riverven, the Timekeeper maintains the flow of time and history. When he goes missing, time begins to unravel, leading to chaos across the realm. A young scholar named Jaden discovers that he is the Timekeeper\'s heir and must step into the role. With the help of a resourceful friend and a rebellious mage, Jaden embarks on a quest to restore the timeline. As they navigate through different eras of Riverven, they confront those who wish to exploit the chaos for power. In a thrilling climax, Jaden learns that true wisdom lies in understanding the past to protect the future.",
            "In Riverven, the elemental clans of Fire and Ice have been at odds for generations. When a devastating drought threatens both clans, a young fire mage named Kira and an ice sorcerer named Thorne must put aside their differences to save their homes. As they embark on a quest to find the legendary Elemental Crystal, they face trials that test their abilities and challenge their beliefs. Along the way, Kira and Thorne learn about the importance of cooperation and understanding. In a climactic battle against a dark elemental spirit, they unite their powers to restore balance to Riverven.",
            "In the depths of the Abyssal Sea, ancient secrets lie waiting to be discovered. A fearless diver named Selene is drawn to the mysteries beneath the waves. Joined by a resourceful sailor and a wise oceanic guardian, she embarks on a quest to uncover the truth behind an ancient civilization lost to time. As they navigate the dangers of the deep, they encounter mythical sea creatures and unravel the legends of the Abyss. In a thrilling finale, Selene discovers that the secrets of the Abyss hold the key to preserving the balance between land and sea, ultimately uniting both worlds."
        ],
        "Starroian":[
            "In the heart of Starroian lies the Cosmic Nexus, a portal that connects all realms. When a malevolent force seeks to corrupt it, a young guardian named Kael is chosen to protect the Nexus. With the help of an ancient sorceress and a rogue starship captain, Kael embarks on a quest to gather the Celestial Crystals needed to stabilize the Nexus. Along the way, they encounter intergalactic beasts and treacherous space pirates. As they race against time, Kael learns that the true strength of a guardian comes from unity and sacrifice. In a climactic battle, they confront the dark force threatening the Nexus, ultimately preserving the balance of Starroian.",
            "An ancient prophecy speaks of the Shattered Stars, remnants of a once-great constellation that holds the key to immense power. A determined historian named Lyra discovers a fragment and realizes she must restore the constellation to prevent chaos from engulfing Starroian. Joined by a fearless warrior and a skilled thief, she sets out on a quest across distant planets to recover the remaining shards. As they confront enemies seeking the shards for themselves, Lyra uncovers secrets about her own lineage. In a thrilling climax, they must unite the shards against an ancient evil that seeks to dominate the stars.",
            "In a universe filled with uncharted territories, a celestial cartographer named Arin dreams of mapping the cosmos. When he stumbles upon a lost star map leading to the fabled Starfall Ruins, he realizes he is not the only one searching for it. A cunning bounty hunter and a mysterious alien join forces with him to navigate the dangers that lie ahead. As they decode the map and face mythical guardians, Arin learns about the importance of knowledge and its impact on destiny. In a thrilling climax, they confront rival treasure hunters, uncovering the true purpose of the ruins and their connection to the fate of Starroian.",
            "A sacred artifact known as the Luminary, capable of channeling light to protect Starroian, has been stolen by a dark sorcerer named Vorath. A courageous knight named Elenor takes it upon herself to retrieve it. With the help of a wise elder and a rebellious mage, Elenor embarks on a journey to confront Vorath\'s dark forces. As they traverse enchanted landscapes, they encounter trials that test their resolve and friendship. In a climactic battle, Elenor must harness the true power of the Luminary, discovering that light shines brightest in the darkest times.",
            "In Starroian, a powerful Timeweaver named Seraphine has maintained the flow of time for eons. When she goes missing, the timeline begins to unravel, causing chaos throughout the realms. A young apprentice named Orion discovers that he must take on the mantle of the Timeweaver. Joined by a brave warrior and a skilled historian, they embark on a quest to find Seraphine and restore the timeline. As they journey through different epochs of Starroian, they confront those who seek to exploit the chaos for their gain. In a thrilling climax, Orion learns that the choices of the past shape the future and must face a time-bending adversary.",
            "In the fabled Celestial Library, ancient knowledge and powerful spells are housed. When a dark faction attempts to seize it, a passionate scholar named Nia must protect its secrets. With the help of a dashing rogue and a loyal librarian, Nia embarks on a quest to secure the library\'s defenses. As they uncover hidden chambers and lost tomes, they encounter ancient spirits and traps set to guard the knowledge. In a gripping climax, they confront the dark faction leader, and Nia must prove that knowledge is the greatest weapon against tyranny.",
            "Every century, the Starborn—a group of gifted individuals—must undergo trials to prove their worth and protect Starroian. A young participant named Kaelin discovers a conspiracy to undermine the trials and unleash chaos. With the help of a mentor and a determined friend, Kaelin must navigate the challenges and uncover the truth. As they face tests of courage, wisdom, and strength, Kaelin learns about the true meaning of leadership. In a dramatic finale, they confront the conspirators during the final trial, demonstrating that unity is stronger than division.",
            "In a land where elemental forces clash, a cataclysm threatens to disrupt the balance of nature. A skilled elemental mage named Taryn discovers that the Conflux, a gathering of elemental spirits, is needed to restore harmony. Joined by an earthbound guardian and a mischievous water sprite, Taryn sets out on a journey to summon the spirits. As they navigate treacherous terrains and face elemental guardians, they uncover ancient rituals that hold the key to balance. In an epic battle, they confront the forces of chaos, proving that the elements are stronger together.",
            "A council of star leaders governs the harmony of Starroian, but when one of them betrays the alliance, chaos ensues. A loyal council member named Jax discovers the conspiracy and sets out to uncover the traitor. With the help of a brilliant strategist and a courageous soldier, Jax journeys through political intrigue and betrayal. As they gather evidence and rally allies, they learn about the power of loyalty and trust. In a thrilling climax, Jax must confront the traitor in a showdown that could determine the fate of Starroian.",
            "A mysterious phenomenon known as the Echoes begins to disrupt the natural order of Starroian, causing memories and time to overlap. A young empath named Mira discovers she has the ability to hear the echoes and must navigate the confusion to restore harmony. Joined by a skilled healer and a rogue with a troubled past, Mira embarks on a quest to uncover the source of the Echoes. As they journey through overlapping realities and face their own pasts, they learn about forgiveness and acceptance. In a heart-wrenching finale, Mira confronts the source of the Echoes, ultimately bringing peace to her world."
        ],
        "Terac":[
            "Deep beneath the surface of Terac lies the ancient city of Eldoria, home to a long-forgotten race of magical beings known as the Eldorians. When a powerful artifact called the Heartstone is disturbed by a mining expedition, it awakens the Eldorians from their slumber. A courageous young woman named Mira, who has a unique connection to the Eldorians, must rally her friends—a brave warrior and a clever mage—to protect the Heartstone from a dark sorcerer who seeks to use its power for his own gain. As they navigate treacherous landscapes and face ancient guardians, Mira discovers her own hidden potential and the true meaning of bravery.",
            "In the world of Terac, tales of a Lost Realm filled with untold treasures and powerful relics abound. A young treasure hunter named Kael, determined to uncover the truth, sets out on a quest with his loyal companion, an enigmatic rogue named Elara. They traverse enchanted forests and face mythical beasts, piecing together clues that lead them to the fabled realm. However, as they draw closer to their goal, they realize that others are also hunting for the Lost Realm, including a malevolent cult seeking to harness its power. In a gripping climax, Kael and Elara must outsmart their adversaries and unlock the secrets of the realm before it falls into the wrong hands.",
            "In the shadowy corners of Terac, a sinister force known as the Darkening threatens to engulf the land. A young girl named Lyra discovers she has the rare ability to manipulate shadows. Fearing her powers, she hides away until a wise mentor appears, urging her to embrace her gift. Together, they embark on a quest to uncover the origins of the Darkening and the ancient prophecy that foretells its defeat. Along the way, they gather allies—a fierce warrior and a cunning bard—who help Lyra learn to control her powers. In a climactic battle, she must confront the source of the Darkening, proving that even shadows can bring light.",
            "The four elemental clans of Terac—Earth, Fire, Water, and Air—have lived in harmony for centuries. However, a mysterious force begins to sow discord among them, inciting a war that threatens to tear the world apart. A young diplomat named Arin is chosen to negotiate peace. He teams up with representatives from each clan: a fiery warrior, a wise water mage, and a fierce air archer. As they travel between the clans, they uncover a conspiracy aimed at manipulating the elemental balance for power. In a thrilling climax, Arin and his companions must unite their strengths to thwart the conspiracy and restore harmony to Terac.",
            "The Forbidden Forest is a realm of magic and danger, said to hold the secrets of ancient magic. A curious young sorceress named Elowen ventures into the forest against her better judgment, determined to prove herself. Within its depths, she encounters talking animals, mischievous spirits, and powerful guardians. As she navigates the challenges of the forest, Elowen discovers a hidden prophecy that could change her fate and that of Terac. In a heart-pounding finale, she must confront the guardian of the forest, learning that sometimes the greatest magic comes from within.",
            "Every thousand years, a Celestial Star falls from the heavens, said to grant unimaginable power to its possessor. A young farmer named Finn witnesses the star\'s descent and rushes to claim it. However, he soon learns that he is not the only one searching for it. A group of ruthless mercenaries and a dark sorceress are also on the hunt. Finn teams up with a skilled archer and a wise herbalist to protect the star from falling into the wrong hands. As they journey through perilous terrains, they uncover secrets about the star\'s true nature. In a dramatic climax, Finn must make a choice that will determine the fate of Terac.",
            "Beneath Terac lie the Crystal Caverns, a labyrinth of shimmering crystals that holds the key to ancient magic. A young miner named Talia stumbles upon a hidden chamber filled with powerful crystals, awakening a guardian spirit. The spirit reveals that the crystals are linked to the balance of magic in Terac and warns of an impending disaster. Talia teams up with a resourceful engineer and a skilled fighter to protect the caverns from a greedy merchant who seeks to exploit their power. As they delve deeper into the caverns, they face challenges that test their courage and resolve. In a thrilling finale, they confront the merchant, proving that true power lies in preservation, not exploitation.",
            "In a forgotten corner of Terac, a lost kingdom awaits its rightful ruler. A noble knight named Sir Cedric discovers an ancient map that leads to the kingdom\'s hidden location. Joined by a loyal squire and a fierce warrior princess, Cedric embarks on a quest to restore the kingdom and its honor. As they face trials and adversaries, they learn about the history of the lost kingdom and the sacrifices made by its people. In a climactic battle against those who wish to claim the kingdom for themselves, Cedric must embrace his destiny and unite the kingdom\'s inhabitants for a brighter future.",
            "In the enchanting realm of Terac, the Fae hold a festival every hundred years, bringing magic and wonder to the land. However, when a dark force threatens to disrupt the celebration, a young Fae named Lira must step up to save her kin. With the help of a human bard and a mischievous sprite, Lira embarks on a quest to restore the festival\'s magic. Along the way, they encounter ancient creatures and face trials that test their resolve and friendship. In a dazzling finale, Lira must harness the true essence of the festival to defeat the darkness, proving that joy and unity can overcome any challenge.",
            "In the majestic Mountains of Terac lies the Heartstone, a powerful gem that sustains the land\'s magic. When the Heartstone is stolen by a rogue sorcerer, the balance of magic begins to falter. A brave mountain dweller named Eamon, along with a determined healer and a grizzled warrior, sets out on a quest to retrieve the gem. Their journey takes them through treacherous terrains and ancient ruins, where they uncover the sorcerer\'s dark plans. In a thrilling climax, they confront the sorcerer in an epic battle, learning that true strength comes from courage, friendship, and the heart of the mountain itself."
        ],
        "Urius":[
            "In Urius, the balance between the elemental forces is maintained by the Council of the Four. When a dark entity known as the Shadowbringer rises, it begins to disrupt this balance, causing chaos across the land. A young elemental mage named Lyra discovers that her family has guarded a powerful relic—the Prism of Unity. Teaming up with a fierce warrior and a wise druid, Lyra embarks on a quest to restore the balance. As they journey through enchanted forests and perilous mountains, they uncover secrets about the Shadowbringer\'s origins. In a climactic battle, Lyra must harness the power of the Prism, proving that unity can overcome darkness.",
            "Legends speak of a Lost City, hidden beneath the sands of Urius, filled with untold treasures and ancient knowledge. A determined archaeologist named Jaxon stumbles upon a fragment of an ancient map that may lead to the city. Joined by a cunning thief and a reluctant scholar, Jaxon sets out on a perilous expedition. As they decipher clues and overcome deadly traps, they encounter guardians of the city, bound to protect its secrets. In a gripping finale, they confront a rival expedition determined to seize the treasures for themselves, leading to a revelation about the true purpose of the Lost City.",
            "Once every century, the Blood Moon casts its crimson glow over Urius, awakening ancient curses. A small village is struck by a mysterious illness during this time, leading a brave healer named Elara to investigate. With the help of a skeptical knight and a mysterious wanderer, Elara uncovers an ancient prophecy linking the Blood Moon to an ancient vampire lord. As they gather allies and confront the vampire\'s minions, Elara learns about her own family\'s connection to the prophecy. In a thrilling climax, she must confront the vampire lord, using her healing powers to break the curse and save her village.",
            "In Urius, the Arcane Trials are held every ten years to determine the most skilled magic users. A talented but inexperienced mage named Kaelin dreams of proving himself. When a shadowy figure begins sabotaging the trials, Kaelin teams up with a fierce rival and a supportive mentor to uncover the truth. As they navigate magical challenges and face formidable opponents, they learn that trust and friendship are just as important as skill. In a heart-pounding finale, Kaelin must face the shadowy figure in the final trial, proving that true strength comes from within.",
            "In the coastal regions of Urius, enchanting sirens lure sailors to their doom with their mesmerizing songs. A young sailor named Finn survives an encounter with the sirens and discovers that they are under a curse that forces them to sing for power-hungry warlocks. Determined to save the sirens, Finn teams up with a brave pirate and a cunning sea witch. Together, they embark on a quest to break the curse and restore harmony to the seas. As they face treacherous waters and magical storms, Finn learns that true courage comes from compassion and sacrifice. In a dramatic showdown, they confront the warlocks, freeing the sirens and restoring their rightful place in the ocean.",
            "In the celestial realm of Urius, Starshapers mold the very fabric of reality with their celestial magic. When a malevolent force threatens to consume the stars, a gifted Starshaper named Mira discovers her unique ability to manipulate light. Alongside a grizzled veteran and an eager apprentice, Mira embarks on a quest to forge a powerful artifact that can restore the light. As they traverse astral realms and face cosmic creatures, they uncover a conspiracy that threatens the existence of the Starshapers. In a breathtaking finale, Mira must confront the darkness and harness her powers to save the stars.",
            "In a time when elemental magic is dying, a young girl named Elin discovers she is the last Elementalist, capable of wielding all four elements. When an oppressive regime seeks to eliminate magic, Elin must flee her village with a group of misfits, including a jaded warrior and a clever trickster. As they travel through dangerous territories, they gather allies and uncover ancient spells that strengthen Elin\'s powers. In a thrilling climax, Elin confronts the regime\'s leader, realizing that the true power of an Elementalist lies not just in magic, but in the bonds forged with her friends.",
            "In the haunted lands of Urius, whispers of the past echo through the air. A young historian named Aric becomes obsessed with uncovering the truth behind a series of ghostly apparitions plaguing his village. With the help of a fearless ghost hunter and a gifted medium, Aric delves into the history of the land, uncovering a dark secret tied to an ancient betrayal. As they confront vengeful spirits and navigate treacherous terrains, Aric learns about forgiveness and the power of letting go. In a heart-stopping finale, they must face the source of the whispers, ultimately freeing the spirits and bringing peace to the land.",
            "The Crystal Isles are a magical archipelago known for their breathtaking beauty and powerful crystals. When a greedy tyrant seeks to exploit the islands\' magic, a young islander named Talia bands together with a diverse group of rebels—including a charismatic pirate and a wise elder. Together, they devise a plan to protect the islands and restore their natural balance. As they face fierce battles and treacherous waters, Talia learns about leadership and the importance of fighting for one\'s home. In a climactic showdown, they confront the tyrant, proving that unity can overcome even the strongest adversaries.",
            "Legends tell of a dragon who guards a powerful heart crystal capable of granting immense power. When the dragon is captured by a dark warlord, a brave knight named Cedric embarks on a quest to rescue it. Joined by a skilled archer and a mysterious sorceress, Cedric must navigate the warlord\'s fortress and face deadly traps. As they delve deeper into the fortress, they uncover the true connection between the dragon and the fate of Urius. In a thrilling finale, Cedric confronts the warlord and learns that true strength lies in compassion, ultimately freeing the dragon and restoring balance to the realm."
        ],
        "Vril":[
            "In the heart of Vril lies a forgotten temple, home to the Vrilborn, beings who channel the mystical energy known as Vril. When an ancient prophecy awakens them, a young Vrilborn named Asha discovers her ability to harness this energy. However, a dark cult, intent on controlling Vril for their own nefarious purposes, rises to power. Asha, along with a skeptical warrior and a wise elder, embarks on a quest to unite the Vrilborn and protect their sacred heritage. As they journey through enchanted forests and desolate ruins, Asha learns the true meaning of sacrifice and unity. In a climactic battle, she faces the cult leader, proving that the strength of the Vrilborn lies in their connection to each other and their world.",
            "Legends speak of the Eternal Flame, a source of unending power hidden deep within the Caves of Lumina. A brave adventurer named Kael sets out to find it, believing it can save his village from a devastating drought. Along the way, he teams up with a clever rogue and a gifted healer. As they navigate treacherous caves filled with traps and ancient guardians, they uncover the truth about the Flame\'s origin. They soon realize that the Flame is not merely a source of power, but a reflection of one\'s heart. In a gripping finale, Kael must confront his own motivations and decide if he is worthy of wielding such power.",
            "In a hidden library beneath the ruins of an ancient city, a young historian named Elara discovers the Lost Chronicles, manuscripts that detail the history of Vril and its magical energies. However, when a shadowy figure attempts to steal the manuscripts, Elara teams up with a rugged protector and a witty bard to safeguard the knowledge. As they delve deeper into the chronicles, they uncover dark secrets that could alter the fate of Vril. In a thrilling climax, they must confront the thief, revealing that knowledge itself can be the most potent weapon against tyranny.",
            "In the dark corners of Vril, an ominous force known as the Shadow Wraiths begins to emerge, threatening to consume the realm in darkness. A young knight named Cedric, whose village is attacked, takes it upon himself to uncover the source of this evil. Joined by a brave sorceress and a mystical creature, he embarks on a quest to locate the ancient sigils that can bind the Wraiths. As they face perilous challenges and ancient guardians, Cedric learns about the power of courage and friendship. In a dramatic confrontation, he discovers that the key to defeating the Wraiths lies in understanding their tragic past.",
            "Deep within the Crystal Mountains of Vril, an ancient order known as the Crystal Guardians protects the realm\'s most precious gems, each imbued with unique magical properties. When a power-hungry warlord seeks to steal these crystals to enhance his own dark powers, a young Guardian named Lira rallies her comrades—a fierce warrior and a cunning rogue—to protect their home. As they embark on a quest to reclaim the stolen crystals, they encounter mythical beasts and treacherous landscapes. In an epic finale, Lira learns that true strength comes from unity and sacrifice, ultimately confronting the warlord in a battle that will determine the fate of Vril.",
            "In Vril, the Echoes are spirits of the ancients who guard the wisdom of the past. A troubled young woman named Selene hears their whispers, guiding her toward a hidden truth about her lineage. Driven by curiosity, she teams up with a seasoned explorer and a mysterious wanderer to uncover the truth behind the Echoes. Their journey leads them to ancient ruins where they unlock powerful spells and confront dark forces that seek to silence the Echoes forever. In a thrilling climax, Selene discovers her true heritage and must embrace her destiny to save the Echoes from extinction.",
            "In a realm where dimensions intersect, the Veil protects the fabric of reality from collapsing. A skilled guardian named Thorne is tasked with monitoring the Veil, but when it begins to weaken, he teams up with a rebellious inventor and a clever illusionist. Together, they discover a plot by a group of rogue sorcerers to breach the Veil for their own gain. As they journey through shifting landscapes and alternate realities, they must overcome trials that test their loyalty and resolve. In a breathtaking finale, Thorne learns that the strength of the Veil lies not just in magic, but in the bonds of friendship forged through adversity.",
            "The Heart of the Forest is a legendary source of life in Vril, revered by all who dwell within its borders. When a blight begins to spread, a young druid named Rowan sets out to find the source of the corruption. Accompanied by a fierce protector and a wise elder, they journey into the depths of the forest, where they uncover a dark conspiracy that threatens the very essence of nature. As they confront twisted creatures and dark magic, Rowan learns the importance of balance and respect for the natural world. In a climactic battle, they must restore the Heart and heal the forest before it\'s too late.",
            "Every decade, the Elemental Masters of Vril gather to test their abilities in a series of trials. A young apprentice named Alia aspires to join their ranks but struggles to harness her powers. When a rival seeks to undermine the trials, Alia forms an unlikely alliance with a skilled competitor and a mischievous spirit. As they navigate the trials, they uncover a plot to manipulate the outcomes for personal gain. In a heart-pounding finale, Alia must confront her insecurities and learn that true mastery comes from embracing one\'s own strengths.",
            "In the skies of Vril, celestial spirits dance among the stars, weaving the fabric of fate. A young astronomer named Orin witnesses a celestial event that foretells a catastrophic event. Determined to warn the realm, he teams up with a fearless knight and a talented artist who can capture the spirits\' essence. Together, they journey to ancient observatories and seek out powerful artifacts that can amplify their voices. As they face obstacles and challenges, they learn the importance of hope and collaboration. In a thrilling finale, they must convince the celestial spirits to aid them in preventing the impending disaster, proving that even the smallest voices can resonate through the cosmos."
        ],
        "Wyvern":[
            "In the skies of Wyvern, the legendary Wyvern Riders were once the protectors of the realm. When the last rider, a young woman named Elara, discovers a hidden egg of a rare wyvern species, she becomes its guardian. As dark forces rise, seeking to exploit the power of the wyverns, Elara must train her newfound companion, a spirited wyvern named Kael, to protect their home. Together, they face treacherous battles against mercenaries and sorcerers, uncovering the secrets of the wyvern bond. In a climactic showdown, Elara learns that true strength comes from her connection with Kael and her unwavering courage.",
            "In a hidden valley, a mystical gem known as the Wyvern\'s Heart maintains the balance of magic in the realm. When it is stolen by a power-hungry warlock, a group of unlikely heroes—including a rogue thief, a noble knight, and a wise mage—embark on a quest to retrieve it. As they journey through enchanted forests and perilous mountains, they encounter ancient guardians and unravel the truth behind the warlock\'s dark intentions. In an epic battle, they must reclaim the Wyvern\'s Heart, discovering that its true power lies in the unity of their diverse strengths.",
            "In Wyvern, the winds carry whispers of prophecy. A young boy named Finn, gifted with the ability to understand these whispers, discovers a dark omen that threatens his village. Joined by a rebellious girl with a knack for elemental magic and a grizzled warrior seeking redemption, Finn sets out to uncover the truth. Their journey leads them to ancient ruins where they confront the source of the prophecy. In a heart-pounding climax, Finn learns that the power of belief can change destiny, ultimately rallying his village to face the impending threat.",
            "Deep within the Crystal Caverns of Wyvern, a powerful guardian known as the Crystal Dragon protects ancient secrets. When a band of treasure hunters seeks to exploit the caverns, a courageous young girl named Mira stumbles upon the dragon. Instead of fleeing, she befriends it and learns about the delicate balance of magic that sustains the land. Together, they embark on a quest to stop the treasure hunters and restore harmony. In a thrilling finale, Mira must use her newfound connection with the dragon to confront the hunters, proving that true treasure lies in friendship and protection of the natural world.",
            "The Enchanted Isle is a mystical land said to hold the key to unlocking ancient powers. A curious explorer named Jaxon discovers a map leading to the isle, along with his loyal companion, a fierce warrior named Kael. Upon reaching the isle, they encounter magical creatures and face trials that test their resolve. As they delve deeper into the isle\'s mysteries, they uncover a plot to exploit its magic for personal gain. In a gripping climax, Jaxon and Kael must confront the true villain and protect the isle\'s secrets, learning that wisdom and courage go hand in hand.",
            "In Wyvern, young mages must undergo the Elemental Trials to prove their worth. A determined girl named Alia enters the trials, eager to showcase her fire magic. However, she soon discovers that the trials are being sabotaged by a dark force seeking to manipulate the elemental energies. With the help of her fellow contestants—a water mage and an earth shaper—Alia must navigate dangerous challenges and unravel the conspiracy. In a heart-stopping finale, she learns that true mastery of magic comes from collaboration and understanding the balance of elements.",
            "Legends tell of the Elders, ancient beings who hold the wisdom of Wyvern\'s past. When a mysterious blight begins to spread across the land, a young scholar named Lira seeks to uncover the Elders\' secrets. Joined by a brave knight and a mysterious herbalist, Lira embarks on a quest to find the Elders\' lost artifacts that can heal the land. As they confront challenges and uncover hidden truths, Lira learns the importance of respecting nature and the wisdom of those who came before. In a dramatic confrontation, they must face the source of the blight, using the Elders\' wisdom to restore balance to Wyvern.",
            "In the kingdom of Wyvern, tales of the Wyvern King\'s shadow—a powerful specter that brings misfortune—spread fear among the populace. A brave young woman named Rhea decides to confront the legend, determined to uncover the truth. Along with her loyal friends—a witty bard and a skilled hunter—she embarks on a journey to find the Wyvern King\'s lair. As they unravel the mysteries surrounding the king\'s shadow, they learn that it is a manifestation of unresolved grief. In an emotional climax, Rhea confronts the shadow, helping it find peace and ultimately lifting the curse from the kingdom.",
            "Every year, the Wyvern Spirits gather for a grand dance, a celebration of life and magic. When a dark sorcerer seeks to disrupt the dance to steal its power, a young dancer named Elin teams up with a gifted musician and a brave warrior. Together, they must protect the spirits and ensure the dance continues. As they journey through enchanting landscapes and face the sorcerer\'s minions, they discover the importance of harmony and friendship. In a breathtaking finale, they must perform the dance themselves, channeling the spirits\' energy to defeat the sorcerer and restore peace to Wyvern.",
            "The Wyvern Stone, a powerful artifact, is said to hold the essence of the wyverns themselves. When it is stolen by a rival kingdom, a young prince named Alaric sets out to reclaim it. Joined by a fierce female knight and a wise advisor, Alaric embarks on a perilous quest to infiltrate the rival kingdom. As they face political intrigue and treachery, Alaric learns about leadership and sacrifice. In a climactic battle, they confront the rival kingdom\'s forces, ultimately reclaiming the Wyvern Stone and solidifying a new alliance, proving that strength lies not just in power, but in understanding and cooperation."
        ],
        "Xenomorph":[
            "In the heart of Xenomorph, a hidden temple is discovered deep beneath the surface. A team of archaeologists led by Dr. Lena Farrow uncovers ancient inscriptions that speak of a powerful entity known as the Ancients, who once ruled the land. As they delve deeper, they accidentally awaken a slumbering force that begins to wreak havoc across the region. The team must race against time to decipher the ancient texts and find a way to appease the Ancients before they unleash their fury on the world. In a breathtaking climax, Lena learns that the key to stopping the chaos lies within the secrets of her own lineage.",
            "Every decade, the greatest warriors of Xenomorph gather for the Trials—a series of brutal challenges to determine the next Champion. When a mysterious challenger emerges, claiming to possess a power that can shift the balance of the realm, a seasoned champion named Kellan must confront not only his rivals but also his own doubts. As Kellan navigates the trials, he discovers that the mysterious challenger has a dark secret that could endanger all of Xenomorph. In a dramatic finale, Kellan must choose between his ambition and the greater good, proving that true strength comes from within.",
            "In a world divided by warring factions, an uneasy alliance is formed between two rival clans when a common threat—a marauding beast known as the Shadow Wyrm—begins to terrorize their lands. Leaders of both clans, Asha and Torin, must put aside their differences and unite their people to face the impending danger. As they embark on a perilous journey to uncover the origins of the Shadow Wyrm, they encounter ancient ruins and forgotten magic. Along the way, Asha and Torin discover the true meaning of leadership and sacrifice. In a climactic battle, they must confront the beast and their own prejudices, learning that unity is their strongest weapon.",
            "An ancient artifact known as the Heart of Xenomorph is rumored to hold immense power. When it goes missing from a sacred temple, a group of unlikely heroes—a cunning thief, a disillusioned knight, and a wise old mage—sets out to retrieve it. As they follow the trail of the thief, they discover that the artifact has the potential to corrupt those who wield it. Each character must confront their own desires and fears as they navigate treacherous landscapes and face off against dark forces intent on claiming the Heart for themselves. In a gripping finale, they realize that true power lies in selflessness and courage.",
            "In Xenomorph, whispers of a long-lost civilization resurface when a young historian named Elian stumbles upon an ancient library buried beneath the mountains. As he deciphers texts that reveal the history of the land, he learns about a cataclysmic event that destroyed the civilization. However, disturbing signs indicate that the past is repeating itself. Elian teams up with a fierce warrior and a gifted seer to prevent history from repeating. As they uncover hidden truths, they must confront not only external threats but also their own internal struggles. In a heart-stopping climax, they race against time to rewrite the fate of Xenomorph.",
            "In a secluded village, residents begin to disappear one by one, sparking fear and paranoia. A group of friends, led by the brave and resourceful Mira, decides to investigate the strange occurrences. As they dig deeper, they uncover a sinister plot involving an ancient cult that worships a dark deity. The cult has been using the villagers as sacrifices to gain power. Mira and her friends must band together to confront the cult, using their wits and skills to thwart the sacrifices. In a thrilling finale, they face off against the cult leader, discovering that the true power lies within the bonds of friendship.",
            "In a dystopian future where Xenomorph has been ravaged by war, a group of survivors takes refuge in the Last Stronghold, a fortified city that remains untouched by the chaos outside. Led by a determined leader named Jarek, they strive to rebuild their community. However, when an enemy faction breaches the stronghold\'s defenses, the residents must band together to defend their home. As Jarek navigates the challenges of leadership, he learns about sacrifice and resilience. In an action-packed climax, the survivors unite to reclaim their stronghold, proving that hope can thrive even in the darkest times.",
            "An ancient labyrinth is said to hold untold treasures, but it is also filled with deadly traps and mythical creatures. A group of adventurers—each with their own motives—enter the labyrinth in search of glory. Among them is a cunning rogue named Zara, who seeks riches, and a noble paladin named Rhys, who seeks redemption. As they navigate the twists and turns of the labyrinth, they must confront not only external dangers but also their own inner demons. In a gripping finale, they discover that the true treasure lies in their shared experiences and the friendships forged along the way.",
            "A long-forgotten prophecy foretells the return of an ancient evil that once threatened Xenomorph. As dark omens begin to surface, a young warrior named Kira finds herself at the center of the unfolding chaos. Guided by visions from the past, Kira must rally a diverse group of allies—including a skeptical mage and a reformed thief—to confront the resurgence of the ancient evil. As they uncover the truth behind the prophecy, they realize that their destinies are intertwined. In a heart-pounding climax, Kira must embrace her role as the key to stopping the impending darkness.",
            "In Xenomorph, fate is woven from threads of choice and consequence. A mysterious artifact known as the Weaver\'s Stone grants its holder the ability to glimpse into the future. When a power-hungry warlord seizes the stone, chaos ensues as he attempts to manipulate destiny for his own gain. A young seer named Elen, whose family was destroyed by the warlord, teams up with a group of rebels to reclaim the stone. As they embark on their mission, they face numerous challenges that test their resolve and commitment. In a thrilling climax, Elen discovers that true power lies not in altering destiny but in embracing the present."
        ],
        "Yutogen":[
            "In Yutogen, the Heart Crystal is the source of all magic, but when it shatters, chaos ensues across the realm. A skilled mage named Kaelin sets out on a quest to find the fragments and restore balance. Joined by a rogue thief named Lira and a stoic warrior named Garrick, they face treacherous landscapes and mystical creatures. As they collect the shards, they uncover a sinister plot by an ancient sorcerer who seeks to harness the crystal\'s power for himself. In a climactic battle, Kaelin must confront the sorcerer, learning that true power comes not from the crystal, but from the bonds forged along the journey.",
            "In the serene village of Eldara, strange echoes resonate from the ancient mountains, causing unease among the villagers. A curious young girl named Aria decides to investigate the source of the echoes. As she climbs the mountains, she discovers a hidden cave filled with ancient inscriptions and remnants of a long-lost civilization. Guided by the echoes, Aria uncovers a prophecy about a coming darkness. She must rally her friends, including a skeptical blacksmith and a wise elder, to prepare for the impending threat. In an emotional finale, Aria realizes that the echoes are not just warnings, but a call to action for the people of Yutogen.",
            "In the bustling city of Nyxport, a secretive organization known as the Guild of Shadows operates from the shadows, pulling strings behind the scenes. When a nobleman is assassinated, a young investigator named Elias is tasked with uncovering the truth. As he delves deeper, he discovers a web of deceit and betrayal that leads to the Guild. Teaming up with a spirited street urchin and a former Guild member, Elias navigates the treacherous underbelly of the city. In a heart-stopping climax, he must confront the leader of the Guild and expose the corruption that threatens to consume Nyxport.",
            "When an ancient family heirloom is stolen from the prestigious House of Thalia, Lady Seraphina embarks on a quest to retrieve it. The heirloom, a powerful amulet, is said to hold the essence of her ancestors. As she tracks the thief through the enchanted forests of Yutogen, she encounters mythical creatures and discovers her own latent abilities. Along the way, she forms an unlikely alliance with a disgraced knight and a mischievous fae. Together, they must confront the dark forces that seek the amulet for their own nefarious purposes. In a climactic showdown, Seraphina learns the true meaning of heritage and bravery.",
            "In the oppressive kingdom of Pyronia, where fire magic is strictly controlled, a group of rebels known as the Flamekeepers rises against tyranny. Led by the fierce and determined Arin, they seek to restore freedom to the land. When a powerful artifact that could turn the tide of the rebellion is stolen, Arin must venture into the heart of enemy territory to retrieve it. Along the way, she faces betrayal from within and discovers hidden truths about her own lineage. In a fiery climax, Arin confronts the tyrant and ignites the spark of hope in her people.",
            "A sacred order known as the Guardians of Yutogen protects the realm from dark forces. When an ancient evil awakens, the Guardians must gather their strength. A young recruit named Finn, eager to prove himself, discovers a hidden prophecy that speaks of a champion who can wield the power of the ancients. As Finn embarks on a quest to unlock his potential, he faces trials that test his resolve and character. With the help of seasoned Guardians and unexpected allies, he learns that being a champion is not just about power, but also about compassion and sacrifice. In a thrilling finale, Finn must unite the Guardians to confront the rising darkness.",
            "In the enchanted glades of Yutogen, the annual Dance of the Fae is a celebrated event that binds the realm\'s magic. However, when a powerful enchantress attempts to steal the dance\'s magic for herself, the balance of the land is threatened. A spirited fae named Lyra and a human bard named Tarek must work together to protect the dance. As they gather allies from different realms, they face challenges that test their friendship and trust. In a vibrant and magical climax, Lyra and Tarek learn that true magic comes from unity and celebration, saving the Dance of the Fae from ruin.",
            "The coastal town of Rivermist faces destruction as unnatural tides threaten to engulf it. A gifted sailor named Mira feels a deep connection to the ocean and embarks on a quest to discover the cause. Alongside her childhood friend, a talented water mage named Rowan, they delve into the mysteries of the ocean and encounter mythical sea creatures. As they uncover a plot involving an ancient sea god, they must unite the townsfolk to protect their home. In an epic battle against the tides, Mira learns that the ocean\'s power is both a gift and a responsibility.",
            "In Yutogen, a hidden realm exists parallel to the world known as the Veil. When a curious scholar named Elowen accidentally discovers a portal to the Veil, she is thrust into a world of enchantment and danger. As she explores this new reality, she learns about a looming threat that could spill over into her own world. With the help of a brave warrior from the Veil and a mischievous spirit, Elowen must find a way to close the portal and protect both realms. In a breathtaking finale, she discovers her true purpose as a bridge between worlds.",
            "In a secluded village, an ancient tome reveals the lost knowledge of the Ancients, powerful beings who once shaped Yutogen. A young apprentice named Kael seeks to unlock the secrets of the tome, hoping to harness the Ancients\' magic. However, his ambition attracts the attention of dark forces that wish to exploit this knowledge. Joined by a wise mentor and a fierce protector, Kael embarks on a journey to safeguard the tome and prevent it from falling into the wrong hands. In a heart-stopping climax, he learns that true legacy lies not in power, but in wisdom and the choices one makes."
        ],
        "Zerath":[
            "In the heart of Zerath, an ancient artifact known as the Celestial Orb maintains the balance between light and darkness. When the orb shatters, chaos erupts across the land. A young mage named Elara discovers that she has a unique connection to the shards of the orb. Together with a stoic warrior named Kael and a clever rogue named Nyra, they embark on a perilous quest to recover the shards and restore harmony. As they face dark forces and treacherous landscapes, Elara learns that true strength comes from embracing her past and the bonds forged with her companions. In a climactic showdown, they confront the dark entity seeking to claim the orb\'s power.",
            "In a hidden village, the elders speak of a prophecy that foretells the arrival of a hero who will save Zerath from impending doom. When a seemingly ordinary blacksmith named Jorin discovers an ancient sword embedded in a stone, he is thrust into a journey he never anticipated. Joined by a spirited huntress named Lira and a wise old sage, Jorin learns that the sword holds immense power tied to the fate of the realm. As they uncover the truth behind the prophecy, they face trials that challenge their resolve and beliefs. In a thrilling climax, Jorin must embrace his destiny and wield the sword to confront the darkness threatening to engulf Zerath.",
            "Deep within the forests of Zerath lies the ruins of an ancient kingdom, long forgotten by time. When an adventurous archaeologist named Mira uncovers a hidden entrance, she awakens the dormant spirits of the kingdom. Guided by a spirit named Aelion, Mira must navigate the remnants of the kingdom while uncovering its tragic past. Along the way, she encounters a skeptical knight and a mischievous thief who join her quest. As they piece together the history, they discover a dark force seeking to reclaim the kingdom for itself. In a heart-wrenching finale, Mira learns that forgiveness and understanding are key to breaking the curse.",
            "In the bustling city of Nareth, a powerful underground organization known as the Guild of Shadows manipulates events from the shadows. When a beloved noble is murdered, a tenacious investigator named Selene is determined to uncover the truth. As she delves into the dark underbelly of the city, she uncovers a conspiracy that reaches the highest echelons of power. With the help of a charming thief and a disgraced knight, Selene navigates danger and deception. In a shocking twist, she learns that the line between justice and revenge can blur, forcing her to make a choice that will alter the course of her life forever.",
            "In Zerath, the four elemental spirits—earth, air, fire, and water—have always lived in harmony. However, when an elemental imbalance occurs, the spirits become restless, causing chaos across the land. A determined young elemental guardian named Thalia is chosen to investigate the source of the disturbance. Accompanied by her childhood friend, a fire-wielding warrior named Kaden, Thalia embarks on a quest to restore balance. Along the way, they face elemental creatures and uncover hidden truths about the spirits\' origins. In a climactic showdown, Thalia learns that true harmony comes from understanding and respecting the forces of nature.",
            "In the magical city of Eldoria, a legendary alchemist\'s secrets have been lost for centuries. When a young apprentice named Rowan discovers a hidden lab filled with ancient texts and potions, he becomes obsessed with unlocking the alchemist\'s legacy. However, his quest attracts the attention of dark forces seeking the alchemist\'s most dangerous creation. With the help of a talented healer and a cunning rogue, Rowan must navigate treacherous challenges to protect the knowledge. In a thrilling finale, he realizes that true power lies not in the pursuit of knowledge but in the responsibility that comes with it.",
            "In the oppressive kingdom of Daroth, the ruling council enforces strict laws that suppress magic. A courageous leader named Aria rallies a group of rebels known as the Shadowborn to fight for their freedom. When a powerful artifact that could turn the tide of the rebellion goes missing, Aria must infiltrate the council\'s stronghold to retrieve it. Along the way, she faces betrayal and discovers hidden truths about her own lineage. In a heart-pounding climax, Aria learns that the greatest weapon against tyranny is not just magic, but unity and hope.",
            "In the mystical realm of Zerath, dreamweavers have the ability to manipulate dreams and realities. When a dark force begins to invade dreams, causing nightmares to spill into the waking world, a young dreamweaver named Lira must confront her fears. Teaming up with a brave knight and a resourceful bard, Lira ventures into the dreamscape to confront the source of the nightmares. As they journey through surreal landscapes, they learn that confronting one\'s fears is the key to overcoming darkness. In a breathtaking finale, Lira faces the embodiment of her nightmares, proving that hope can shine even in the darkest of places.",
            "In the enchanted Whispering Forest, trees hold the memories of the past. When a powerful sorceress seeks to harness these memories for her own gain, the balance of nature is threatened. A young herbalist named Finn discovers that he can communicate with the trees. Guided by the wisdom of the forest, Finn must unite a group of unlikely allies—a gruff ranger, a spirited dryad, and a skeptical scholar—to stop the sorceress. As they navigate the forest\'s secrets, they learn the importance of preserving history. In a climactic showdown, Finn discovers that true strength comes from understanding and respecting the natural world.",
            "Every century, the Trial of the Ancients is held to test the worthiness of those seeking the title of Guardian of Zerath. A young warrior named Kiera dreams of becoming a Guardian but must prove herself in a series of grueling challenges. Joined by her loyal friend, a clever bard named Jorin, they face physical and mental trials that test their strength and resolve. Along the way, Kiera learns about the true meaning of sacrifice and bravery. In an epic finale, she must confront her deepest fears and prove that the heart of a Guardian lies not in power, but in compassion and courage."
        ],
        "Dark_Army": [
            "In the shadowy recesses of the forsaken castle of Valthor, the powerful necromancer Malakar toiled for years, searching for a way to bring the dead back to life. One stormy night, he discovered an ancient ritual that required the blood of a thousand fallen warriors. Gathering their bones and spirits, he conducted the dark ceremony under the blood moon. As he recited the incantation, the ground shook and shadows coalesced into a single card: the Shadow Legionnaire. This card allowed Malakar to summon legions of spectral soldiers, bound to his will, fighting with the ferocity of their lost lives, and spreading terror in the realm of Domanus.", 
            "In the desolate marshes of Eldrath, a reclusive druid named Nyssa sought to commune with nature\'s darkest elements. One fateful day, she found an ancient tome buried in the muck, detailing how to harness the blood of mythical beasts. Driven by ambition, she captured a wyvern and, using its blood, created the Beastmaster card. This powerful card granted her the ability to control dark creatures from the marsh, commanding them to rise from the depths and join her in battle, turning the tide against her enemies with terrifying ferocity.", 
            "A coven of warlocks, jealous of each other\'s power, decided to unite their essences to create a card that would elevate them above all others. In a dark ritual lit by flickering candlelight, they fused their souls into the Warlock\'s Pact. This card contained the essence of their combined magic, unleashing devastating spells that could obliterate entire armies. However, their bond was not without consequence; their fates were intertwined, leading to treachery and betrayal that echoed throughout their lives, forever binding them in a cycle of darkness.", 
            "Selene, a sorceress renowned for her mastery over the elements, sought a way to harness the raw power of storms. During a fierce tempest, she climbed to the highest peak of the Stormbreaker Mountains. As lightning struck the ground, she captured its energy in a crystal, creating the Stormbringer card. This card allowed her to summon fierce storms, unleashing thunder and lightning upon her enemies, turning the battlefield into a chaotic maelstrom. However, each use drained her own life force, teaching her the heavy cost of wielding such power.", 
            "In the dark depths of the Abyssal Caves, a cunning thief named Aidan stumbled upon an ancient artifact known as the Soulbinder. This relic held the power to trap souls within cards, allowing the wielder to command them. Driven by greed, Aidan crafted the Soulbound card, binding the spirits of those he had wronged to do his bidding. With each soul captured, his power grew, but so did the whispers of their rage. Eventually, the spirits demanded their freedom, leading Aidan down a path of confrontation and redemption he never expected.", 
            "In the kingdom of Daroth, the tyrant king sought to maintain control through fear. He ordered his soldiers to gather the blood of his enemies and use it to create the Bloodlust card. During a gruesome festival of war, this card was forged, thriving on the violence and chaos of battle. Each time an enemy fell, the card empowered the king\'s forces, making them stronger and more ruthless. However, as the bloodlust consumed them, the soldiers became mindless, losing their humanity and becoming mere instruments of destruction, haunted by the ghosts of those they killed.", 
            "In the alchemical sanctum of the city of Eldoria, a brilliant but morally ambiguous alchemist named Zarek discovered the secret to harnessing decay. He gathered rare herbs and the essence of the most toxic creatures to create the Plaguebearer card. This card unleashed virulent diseases upon his enemies, weakening their ranks before a battle. However, the plague also began to affect Zarek, consuming him slowly. As he watched his own body wither, he realized that every creation has a price, and sometimes, that price is too high.", 
            "In the heart of the Whispering Woods, a group of witches gathered under the full moon to cast a powerful spell. From this ritual, they forged the Witches\' Brew card, capable of manipulating fate itself. This card could twist the outcomes of events, causing confusion and betrayal among enemies. However, as the witches used the card to gain power, they found themselves trapped in a web of their own making, as fate turned against them, leading to their downfall in a spectacularly ironic twist.", 
            "The tale of the Vengeful Spirit card is rooted in tragedy. Once a hero who fought for justice, the spirit named Kaelan was betrayed by those he trusted most. His soul lingered on the mortal plane, filled with wrath and sorrow. A dark sorceress, sensing his pain, captured his essence and created the Vengeful Spirit card. This card allowed its wielder to unleash Kaelan\'s fury upon their enemies, haunting them with visions of betrayal. Yet, the card also held Kaelan\'s desire for redemption, forcing its wielder to confront their own choices and the cost of vengeance.", 
            "In the ancient ruins of an otherworldly temple, a council of ancient beings convened to forge the Master of Shadows card. This card was the culmination of all their dark knowledge and power, allowing its wielder to control the forces of darkness itself. As the card was crafted, the beings merged their essences into it, creating a sentient force. However, they soon realized that their collective power could not be contained. In a climactic battle, the Master of Shadows turned against its creators, becoming a force of chaos that reshaped the very fabric of Domanus, forever altering the balance of power."
        ],
        "Light_Army": [
            "In the radiant city of Aetheria, a noble knight named Sir Cedric sought a way to protect his realm from the encroaching darkness. Guided by the whispers of ancient spirits, he discovered a forgotten temple where the light of the stars converged. There, he crafted the Guardian of Light card, infused with the essence of celestial beings. This card allowed him to summon ethereal warriors, shimmering with divine energy, to shield the innocent and strike down evil with unyielding resolve.",
            "High atop the sacred mountain of Solara, the wise priestess Elara gazed into the celestial skies, longing to harness the power of the sun. After years of meditation, she summoned the Sunstone, a radiant gem that glowed with immense energy. With this gem, she created the Sunfire card, capable of unleashing searing rays of light that burned away shadows and healed the wounded. This card became a beacon of hope, inspiring the people of Domanus to stand against despair.",
            "In the enchanted forest of Lumoria, a group of druids gathered to unite their powers in harmony with nature. They performed a sacred ritual, calling upon the spirits of the forest to forge the Nature\'s Guardian card. This card embodied the essence of the flora and fauna, allowing its wielder to summon ancient beasts and verdant guardians. These creatures fought fiercely to protect the land, restoring balance and peace wherever darkness threatened to encroach.",
            "A valiant sorceress named Lyra sought to channel the healing energies of the world. After a harrowing battle left her village in ruins, she ventured into the heart of the Crystal Caverns, where she discovered the Luminescent Crystals. With these crystals, she forged the Healing Light card, which radiated warmth and rejuvenation. This card could mend wounds and revitalize the weary, empowering those who fought for justice and kindness.",
            "In the ancient archives of the Celestial Order, a scholar named Orion stumbled upon an ancient scroll detailing the creation of protective wards. Inspired by its teachings, he crafted the Shield of Valor card, imbuing it with the knowledge of countless battles fought for justice. This card created an impenetrable barrier around its wielder, deflecting dark magic and ensuring that the light would never be extinguished as long as courage remained.",
            "During a celestial alignment, the stars shone brighter than ever, and the celestial beings descended to share their wisdom. A courageous paladin named Aric seized the moment to craft the Starblade card, which held the power of the cosmos. This card transformed into a weapon of pure light, able to cut through any darkness, and imbued its wielder with celestial strength, enabling them to vanquish evil with every swing.",
            "In the twilight of a forgotten age, a group of warriors known as the Dawnbringers sought to restore hope to a world ravaged by despair. They traveled to the Valley of Radiance, where they discovered the Essence of Dawn. With this essence, they created the Dawn\'s Embrace card, which spread light across the battlefield, inspiring allies and disheartening foes. It became a symbol of unity and strength, reminding all that hope can shine even in the darkest of times.",
            "In the heart of the Crystal Glade, an ancient spirit named Seraphiel revealed the existence of the Harmony card. This card could amplify the positive emotions of love and compassion, allowing its wielder to unite allies and heal rifts between them. With the Harmony card, warriors could work together seamlessly, combining their strengths and efforts to overcome even the most formidable foes with grace and unity.",
            "A young scribe named Thalia, longing for adventure, discovered a hidden prophecy that spoke of a card infused with the power of dreams. She journeyed into the Dreamweaver\'s Realm, where she crafted the Dreamcatcher card. This card allowed its wielder to delve into the dreams of others, inspiring courage and creativity. As they fought, they could weave dreams into reality, turning nightmares into visions of hope and possibility.",
            "Finally, in the sacred Temple of Light, the Grand Oracle foresaw the coming darkness and gathered the greatest minds of the Light Army. Together, they created the Luminara card, a culmination of their collective wisdom and power. This card acted as a conduit for divine energy, amplifying the light\'s influence across Domanus. With the Luminara card in hand, its wielder could summon a brilliant aura that illuminated the path of righteousness, leading others away from despair and into the embrace of hope."
        ],
        "Void_Monster_Army": [
            "In the depths of the Abyss, where light dared not venture, a creature known as the Void Wyrm slumbered for eons. A power-hungry sorcerer named Malphar sought to awaken the beast and bind it to his will. Through dark rituals involving forbidden tomes and the sacrifice of his own followers, he created the Wyrmcaller card. This card allowed him to summon the Void Wyrm, unleashing its destructive fury upon the world. However, with each summoning, Malphar lost a piece of his humanity, becoming more like the monster he controlled.",
            "In a cursed village, whispers of a nightmarish creature known as the Shadow Behemoth spread fear among the inhabitants. Driven by curiosity, a young alchemist named Elenora ventured into the darkness, determined to uncover the truth. In a forbidden cave, she discovered the essence of the Behemoth, a swirling mass of shadows. With this essence, she crafted the Behemoth\'s Wrath card, which granted her the ability to unleash its primal rage. Yet, as she wielded the card, she felt its insatiable hunger clawing at her mind, blurring the line between hunter and prey.",
            "The malevolent sorceress Nyx delved into the ancient ruins of a long-lost civilization, seeking the power of the Void. She unearthed an ancient relic known as the Eye of Oblivion, capable of seeing into the depths of the void. Using the Eye, she forged the Void Stalker card, which allowed her to summon twisted creatures from the abyss. Each creature came with its own dark history, and as they emerged, they brought chaos and despair, feeding on the fear of those who dared to stand against her.",
            "A notorious bandit named Korrin sought to harness the power of darkness to become the ultimate thief. He stumbled upon the ruins of an ancient temple dedicated to the Void, where he discovered the Shard of Night. With the shard, he created the Shadowblade card, which transformed his weapons into instruments of shadow. This card granted him the ability to strike unseen, slipping through the shadows like a wraith. However, the more he relied on the card, the more he felt the shadows consuming his soul, turning him into a mere puppet of the void.",
            "In a hidden sanctuary, a group of mages experimented with the essence of fear, believing it to be the key to ultimate power. They created the Nightmare card, which manifested the darkest fears of their enemies into physical forms. As the mages unleashed the nightmares upon the world, they quickly lost control, realizing too late that the nightmares fed on their own fears as well. Each time they cast the card, the line between reality and nightmare blurred, leading them into a maelstrom of madness.",
            "Deep within the chasms of the Void Realm, an ancient entity known as the Harbinger of Despair awaited its moment to rise. A cult of dark worshippers, drawn to its power, performed a ritual to bind its essence to a card. They created the Harbinger\'s Call, which summoned forth the entity\'s minions to do their bidding. Yet, the cultists soon found themselves ensnared by the very darkness they sought to control, as the Harbinger demanded ever-increasing sacrifices, leaving only despair in its wake.",
            "In the twilight of an age long forgotten, a warrior named Tharok forged a pact with a creature from the void known as the Eclipsed Guardian. Together, they created the Eclipse card, which granted Tharok unparalleled power but at a great cost. Each time he wielded the card, the void encroached further into the world, threatening to consume all light. Tharok found himself torn between his duty to protect and the allure of the power that threatened to engulf him completely.",
            "An enigmatic figure known only as the Voidcaller wandered the lands, collecting fragments of ancient horrors. In a dark ritual, he combined these fragments to forge the Horror Manifest card. This card could bring forth manifestations of the most primal fears, sending enemies into a frenzy of terror. However, as the Voidcaller unleashed the horrors, he realized that they were not merely illusions but real threats, causing destruction and chaos wherever they appeared.",
            "In a remote village plagued by disappearances, an old witch named Morwenna was accused of summoning creatures from the void. In truth, she had created the Echo of the Abyss card, a reflection of her own loneliness and despair. This card allowed her to summon echoes of lost souls, who wandered the earth seeking solace. However, each use of the card drew her closer to the void, threatening to swallow her spirit into the darkness she sought to escape.",
            "Finally, a fallen angel named Seraphiel, banished from the heavens, sought redemption through the void. He discovered the Celestial Void card, which contained the power to create an army of twisted angels, corrupted by despair. With this card, Seraphiel could unleash legions of dark seraphim to wage war against the realms of light. Yet, as he commanded his new army, he battled with his own inner demons, questioning whether he could ever truly find redemption or if he was destined to be a harbinger of darkness."
        ],
        "Void_Spell_Army": [
            "In the depths of the Shadowrealm, a powerful sorceress named Vespera sought the knowledge of the ancients. She discovered a forbidden grimoire hidden within a crumbling temple, detailing dark incantations capable of bending reality. From this tome, she crafted the Spell of Oblivion card, allowing her to erase entire memories and events from existence. As she wielded the card, Vespera felt the weight of the void pulling at her own memories, threatening to erase her very essence if she continued to use its power.",
            "The notorious warlock Thorne, obsessed with control, ventured into the Abyss to seek the fabled Essence of the Void. After enduring trials of madness and temptation, he acquired a vial of this potent energy. He infused it into the Shadowbind card, which granted him the ability to ensnare his foes in tendrils of darkness, immobilizing them while feeding on their fears. But with each casting, the void\'s whispers grew louder in Thorne\'s mind, driving him to question his own sanity as he became more entwined with the shadows.",
            "In the haunted ruins of Eldergloom, a group of desperate mages convened to harness the power of despair. They conjured the Grasp of Despair card, which could summon illusions of their enemies\' worst fears. However, as they unleashed the card upon their foes, they found themselves ensnared in the same illusions, confronted by their deepest regrets and failures. The line between reality and illusion blurred, leading to a catastrophic collapse of their minds, as the very spells they cast turned against them.",
            "Deep in the caverns of Dreadspire, an eccentric inventor named Lucian experimented with the Void\'s raw energies. He crafted the Echoes of the Abyss card, a device that could replicate and amplify the powers of others. This card allowed him to steal spells from rival sorcerers, turning their strengths against them. However, with each spell he borrowed, the echoes of the void began to overwhelm him, causing unpredictable surges of power that threatened to tear him apart as he fought for control over the chaos he had unleashed.",
            "In a forsaken library, an ambitious scholar named Mara discovered an ancient text that spoke of the Dark Convergence. Intrigued by its promise of ultimate power, she performed the ritual to create the Convergence card. This card enabled her to merge her spells with those of others, creating devastating combinations that could reshape the battlefield. Yet, the more she fused her magic with the void, the more her own identity began to fracture, leaving her vulnerable to the very forces she sou ght to control.",
            "A twisted sorcerer named Kael sought vengeance on the realm that wronged him. He forged the Vortex of Shadows card from the essence of captured souls, which could unleash devastating whirlwinds of darkness upon his enemies. As he unleashed the card, the howls of the trapped souls echoed in his ears, driving him into a frenzy of rage. Yet, with each use, he felt a piece of his own soul being siphoned away, leaving him increasingly hollow and consumed by his own hatred.",
            "In the cursed marshlands of Murkmire, a witch named Isolde discovered a way to weave the fabric of nightmares into spells. From her dark cauldron, she created the Nightmare Weaver card, capable of summoning nightmares that drained the life force from her enemies. However, as she wielded this power, Isolde began to experience her own nightmares manifesting in reality, forcing her to confront the darkness within herself and the consequences of manipulating such potent forces.",
            "A powerful entity known as the Whispering Shade roamed the Void, tempting mortals with promises of untold power. Many fell prey to its allure, but one mage named Garren resisted. Instead of succumbing, he captured the essence of the Shade and created the Shade\'s Grasp card. This card allowed him to channel shadows into powerful spells that struck fear into the hearts of his enemies. However, the more he wielded the card, the more he felt the Shade\'s influence creeping into his mind, urging him to abandon his no ble intentions.",
            "A forgotten cult, devoted to the ancient Void God, unearthed a relic known as the Void Sigil. With this sigil, they crafted the Corruption card, which tainted the spells of their enemies, twisting them into instruments of destruction. As they unleashed the card\'s power, they reveled in chaos, only to find that the corruption seeped into their own spells as well, leading to catastrophic consequences that turned their dark rituals against them in an unexpected twist of fate.",
            "Finally, an enigmatic sorcerer known only as the Harbinger sought to unite the power of the void. He crafted the Void Mastery card, which allowed its wielder to bend reality itself, manipulating time and space. Yet, as he unleashed the card\'s potential, he realized that the void had its own will, and it sought to escape the confines of his control. The power he sought to master became an uncontrollable force, threatening to engulf all of Domanus in a cataclysm of darkness and despair."
        ],
        "ArtKnight_Book": [
            "In the heart of the ancient city of Arcanum, a gifted scribe named Elowen stumbled upon a hidden chamber filled with relics of a forgotten order of knights. Among these treasures was a mysterious blank book, said to be enchanted by the spirits of legendary warriors. Driven by curiosity, Elowen began to write the tales of these knights within its pages. As she wrote, the ink shimmered with a life of its own, channeling the courage and valor of the knights, which began to manifest as illustrations that sprang to life. The ArtKnight Book became a living chronicle of heroism, inspiring all who dared to read it.",
            "Long ago, the last of the ArtKnights was captured by a malevolent sorceress seeking to harness their powers. In a desperate act, the knight, Sir Cedric, infused his essence into a sacred tome to preserve his legacy. He bound his soul to the pages, ensuring that the ArtKnight Book would awaken whenever the realm faced great peril. Centuries later, during a time of darkness, the book revealed its power, summoning the spirit of Sir Cedric to guide a new generation of heroes in their quest against the sorceress\'s dark reign.",
            "A renowned artist named Maris set out to create a masterpiece that captured the essence of bravery. With each stroke of her brush, she poured her heart into a canvas, but something was missing. One fateful night, she encountered a spectral knight who challenged her to capture true courage. Inspired, Maris painted the knight\'s tale, and as she finished, the ArtKnight Book materialized before her. The book absorbed her painting, granting it life and enabling the knight\'s spirit to guide her through trials, as the ArtKnight Book became a portal to the adventures of the courageous.",
            "In the Library of Elders, an ancient tome lay dormant, waiting for a worthy reader. One day, a curious young girl named Lyra discovered it while exploring the library\'s labyrinthine halls. As she opened the book, it began to glow, revealing the trials and tribulations of the ArtKnights. Enchanted by their bravery, Lyra began to read aloud, and with each word, the knights emerged from the pages to impart their wisdom. The book had chosen her as its new keeper, and she vowed to carry their stories forward, preserving their legacy for generations to come.",
            "A secretive order of mages known as the Luminaries sought to create a powerful artifact that could capture the essence of courage. They gathered rare materials, including the heart of a fallen star and the feather of a phoenix, to forge the ArtKnight Book. Through a complex ritual, they imbued the book with the spirits of legendary knights. When completed, the book not only chronicled their exploits but also granted its reader the strength to confront their own fears, becoming a beacon of hope in troubled times.",
            "An ambitious bard named Orin, desperate to make his mark, set out to collect the greatest tales of the ArtKnights. He traveled through treacherous lands, gathering stories from those who had witnessed their feats. After years of searching, he compiled these tales into a single manuscript. As he read his work by the light of a flickering campfire, the ArtKnight Book manifested, absorbing the stories and transforming Orin into a bardic knight, enabling him to live out the adventures he had chronicled.",
            "In a realm threatened by an ancient curse, a courageous princess named Selene sought a way to restore her kingdom. Guided by an old prophecy, she discovered a forgotten library where the ArtKnight Book lay hidden. To awaken its power, she had to perform a series of trials, each reflecting the virtues of the ArtKnights. With each trial she passed, the book revealed its secrets, teaching her the true meaning of bravery and sacrifice. In the end, the book became her ally, helping her to unite her people against the curse.",
            "A cunning thief named Rowan stumbled upon the ArtKnight Book while searching for treasure in a decaying castle. Intrigued, he opened the book and unwittingly activated its magic. The pages came alive, showcasing tales of valiant knights who had once fought for justice. To escape his life of crime, Rowan had to prove himself worthy by undertaking a quest inspired by the knights\' stories. The book guided him, transforming his heart from that of a thief to a true hero, as he learned the value of honor and bravery.",
            "During a fierce battle between light and darkness, a warrior named Aric fought valiantly but found himself overwhelmed. In his darkest moment, he prayed for strength, and the ArtKnight Book appeared before him. The book granted him visions of the greatest knights who had ever lived, inspiring him to rise and fight back. With newfound courage, Aric led his comrades to victory, and the book became a legendary artifact, passing through the hands of heroes for generations, reminding them of their duty to protect the realm.",
            "Finally, an ancient dragon, once a guardian of the realm, grew weary and fell into slumber. As darkness threatened Domanus, a brave young warrior named Elara sought the ArtKnight Book to awaken the dragon\'s spirit. She discovered that the book contained the dragon\'s memories, which needed to be retold. With every tale she recounted, the dragon\'s spirit stirred until it finally emerged, infused with the strength of the ArtKnights. Together, they united to face the encroaching darkness, proving that courage and hope can awaken even the oldest of legends."
        ],
        "ETC_Book": [
            "In a hidden valley shrouded in mist, an ancient order known as the Ethereal Cartographers sought to document the mysteries of the universe. They crafted the ETC Book using enchanted parchment made from the leaves of the Dreamweaver Tree, which granted the ability to capture visions and knowledge from other realms. As the cartographers inscribed their first entries, the book glowed with a celestial light, revealing maps of distant worlds and paths through time. However, with each revelation, the cartographers felt the weight of the knowledge they carried, realizing that such power could alter destinies.",
            "A curious scholar named Lysander discovered a fragment of a map that hinted at the location of the lost ETC Book. Driven by ambition, he embarked on a perilous journey through treacherous mountains and enchanted forests. After many trials, he found the book guarded by a spectral being known as the Keeper of Secrets. To gain access, Lysander had to answer riddles that tested his wisdom and resolve. Each correct answer unlocked a new chapter of the book, allowing him to grasp the intricacies of magic and science, yet the weight of forbidden knowledge began to haunt him.",
            "A brilliant but reclusive inventor named Valeria sought to create a device that could harness the raw power of the ether. She spent years crafting intricate mechanisms and combining them with shards of the Elemental Crystals. One fateful night, as she activated her creation, a rift opened, and from it emerged the ETC Book. The book absorbed Valeria\'s inventions and became a living compendium of arcane knowledge. However, with every entry, the book grew more sentient, whispering secrets that began to drive Valeria to the brink of madness.",
            "In the twilight of an age long forgotten, a sorceress named Aeloria forged the ETC Book using the tears of fallen stars. Each tear contained the memories of ancient civilizations, and as Aeloria inscribed their tales, the book pulsed with life. It became a vessel for their wisdom, teaching her the art of sorcery and the balance of power. Yet, with each story she recorded, Aeloria felt the sorrow of the stars, and the burden of their losses weighed heavily on her heart, forcing her to confront the sacrifices made for knowledge.",
            "In a bustling city filled with magic and intrigue, a group of young apprentices stumbled upon a hidden library while exploring the catacombs beneath their school. There, they discovered the ETC Book, cloaked in dust and mystery. As they began to read, the book revealed itself as a living entity, eager to share its secrets. Each apprentice was granted a unique power based on their desires, but with great power came the responsibility to protect the knowledge contained within. Together, they forged a bond, vowing to use the book\'s wisdom for good, but the shadows of jealousy began to stir among them.",
            "An enigmatic wanderer known only as the Traveler claimed to have once been a guardian of the ETC Book. He spoke of an ancient ritual that could awaken the book\'s dormant powers, but it required the essence of the four elemental forces: earth, air, fire, and water. A group of brave souls sought the Traveler, determined to complete the ritual. Through trials that tested their courage, wisdom, and sacrifice, they gathered the essences and finally performed the ceremony. As the book awakened, it revealed ancient prophecies and knowledge that reshaped their understanding of the world, but it also foretold of looming dangers that threatened all realms.",
            "In a realm governed by the rules of order, a rebellious young woman named Kaelin sought to challenge the status quo. She discovered an old folktale about the ETC Book, said to contain the power to break the chains of destiny. Guided by her dreams, she embarked on a quest to find it. Along her journey, she faced guardians of order, each presenting challenges that tested her determination. When she finally found the book, she unlocked its potential and created ripples in reality, altering her fate. However, the consequences of her actions began to unravel the very fabric of the world, forcing her to confront the balance between freedom and chaos.",
            "A legendary bard named Finn, known for his enchanting tales, found an ancient harp that resonated with the essence of the ETC Book. He realized that by playing the harp, he could channel the book\'s magic into his stories, bringing them to life. As he performed, the tales unfolded before the audience, revealing long-lost secrets of the realm. However, as he delved deeper into the book\'s narratives, he discovered dark truths that threatened the very heroes he admired, leaving him torn between honoring the past and reshaping the future.",
            "In a time of great conflict, a young scribe named Mira was tasked with documenting the war\'s history. While searching for inspiration, she encountered a mystical entity who revealed the existence of the ETC Book, containing the true stories of both victors and the vanquished. As she transcribed their tales, the book guided her to uncover the untold truths of war, revealing the pain and heroism behind every battle. Yet, with each story she wrote, Mira found herself becoming part of the narrative, experiencing the emotions and struggles of those who came before her.",
            "Lastly, an ancient being known as the Oracle foretold of an impending catastrophe that could consume the world. To avert this fate, a council of wise mages gathered to create the ETC Book, which would serve as a compendium of knowledge for future generations. They infused it with prophecies, spells, and wisdom from the ages. However, as the book was completed, the Oracle warned them that the knowledge contained within would only be unlocked by those pure of heart. The mages entrusted it to the guardians of the realm, knowing that its true power would only be revealed when the time was right."
        ],
        "Gemini_Book": [
            "In the ancient land of Dualis, where the forces of light and shadow coexisted in delicate balance, two twin sisters, Lyra and Selene, discovered an enchanted book during a celestial alignment. The Gemini Book was said to possess the power to harmonize opposites. As the sisters began to inscribe their thoughts and dreams within its pages, the book reacted, weaving their words into stunning illustrations that reflected their unique perspectives. However, with each entry, the book revealed a hidden truth: their bond was intertwined with the fate of their realm, and a looming darkness threatened to tear them apart.",
            "A brilliant but misunderstood mage named Elysian sought to create a powerful artifact that could unify the forces of creation and destruction. He meticulously gathered rare ingredients, including the essence of twilight and a shard of a fallen star. Through a series of complex rituals, he infused these elements into the Gemini Book, giving it the ability to reflect the duality of existence. As Elysian worked, he became increasingly obsessed with his creation, leading to unforeseen consequences that tested the very fabric of reality, challenging his understanding of balance.",
            "In a distant village, a young storyteller named Arlen longed to capture the tales of his ancestors. One fateful night, he stumbled upon the Gemini Book hidden beneath an ancient tree. When he opened it, the book responded to his heart\'s desires, manifesting the stories of both triumph and tragedy from his lineage. Each tale he recorded granted him deeper insights into the dual nature of humanity. However, as he delved into the book\'s depths, he uncovered a dark family secret that threatened to change his life forever.",
            "A renowned alchemist named Kaelis sought to unlock the secrets of the universe. To aid in her quest, she envisioned the Gemini Book as a guide to balance the elements of nature. Using her extensive knowledge, she crafted the book from rare materials: the pages woven from moonlight and the cover forged from the roots of the Eldertree. As she documented her experiments, the book began to absorb her thoughts, revealing hidden connections between the elements. Yet, as she pushed the boundaries of her experiments, she faced the wrath of nature, challenging her resolve and understanding of harmony.",
            "In a realm plagued by chaos, a hero named Thalion discovered the Gemini Book within the ruins of an ancient temple. Legend spoke of the book\'s ability to bring harmony to conflicting forces. As he began to write his own adventures within its pages, the book\'s magic awakened, illustrating his journey with vivid imagery. However, as Thalion wrote, he realized that the book also reflected the darkness within him. Each battle he faced not only tested his strength but also forced him to confront the shadows of his past, revealing the duality of his character.",
            "An ancient oracle, known for her wisdom, foresaw the creation of the Gemini Book as a means to preserve the balance of the cosmos. Gathering the finest scribes and artisans, she orchestrated the crafting of the book using ink made from the tears of the stars. As the scribes wrote, the book absorbed their intentions, becoming a living entity. However, the oracle warned that the knowledge contained within would only be revealed to those who embraced both their light and shadow. As time passed, many sought the book, but few could understand its true purpose, leading to trials that tested their hearts.",
            "A reclusive painter named Elara spent years creating a masterpiece that depicted the harmony of opposites. One day, she discovered the Gemini Book in an old art supply shop. The book responded to her creativity, transforming her brushstrokes into lifelike images that danced across its pages. As she painted her visions, she began to unravel the duality of her own emotions: joy intertwined with sorrow. The Gemini Book became her confidant, revealing the interconnectedness of all experiences. However, with each masterpiece, Elara found herself drawn into a world where the lines between reality and art began to blur.",
            "In a hidden corner of the world, a clandestine society known as the Guardians of Balance sought to create a powerful tome that could record the stories of the cosmos. They believed the Gemini Book would serve as a bridge between dimensions. Using threads of fate and echoes of time, they crafted the book with utmost care. As they wrote their chronicles, the book revealed insights into the past, present, and future, illuminating the connections between all beings. Yet, as they explored the depths of time, they uncovered the dangers of tampering with destiny, forcing them to confront their own choices.",
            "A curious young apprentice named Mira stumbled upon the Gemini Book while exploring an abandoned tower. Intrigued by its glowing pages, she began to write her dreams and aspirations. To her astonishment, the book responded by revealing visions of her future. Each time she wrote, the book illustrated the potential paths her life could take, showcasing the duality of choices. However, Mira soon realized that with each decision she documented, she felt the weight of the consequences grow heavier, leading her to question her desires and the very nature of fate.",
            "Finally, an enigmatic traveler known as the Weaver of Fates claimed to possess the secrets of the Gemini Book. He sought a group of chosen individuals to embark on a quest to unlock its potential. Together, they traversed realms and faced trials that tested their strengths and weaknesses. As they documented their journey within the book, it transformed into a tapestry of experiences, revealing the interconnectedness of their destinies. Ultimately, the Gemini Book taught them that true power lies not in the light or darkness, but in embracing the harmony between both."
        ],
        "Genshin_Book": [
            "In the tranquil land of Teyvat, an enigmatic scholar named Althea set out to create the Genshin Book, a compendium of elemental knowledge. To craft this legendary tome, she ventured to the sacred peaks of Liyue, where she collected the essences of all seven elements. Each essence shimmered with the power of nature and magic. As Althea began inscribing her discoveries, the book came to life, illustrating the history of Teyvat\'s elemental powers. However, as she delved deeper, she uncovered dark secrets of elemental corruption that could unravel the world\'s harmony.",
            "A wandering bard named Kael stumbled upon a hidden library in Mondstadt, where the Genshin Book was said to reside. Drawn by the legends of the past, he sought to uncover the stories of the fallen heroes of Teyvat. As he began to play his lute, the book responded, conjuring visions of ancient battles and glorious triumphs. With every note, the book revealed forgotten songs that held the essence of the elements. Yet, Kael soon realized that by reviving these stories, he was awakening dormant forces that sought vengeance.",
            "In the bustling city of Sumeru, a young alchemist named Lyra aspired to synthesize the ultimate potion. To achieve this, she believed the Genshin Book would hold the key. After a grueling journey through enchanted forests and across perilous mountains, she discovered the book guarded by a sentient creature known as the Archivist. To gain its wisdom, she had to solve riddles that intertwined with the fabric of nature. As she transcribed her findings, she found herself entangled in an age-old conflict between the elements that threatened to consume her.",
            "A group of misfit adventurers, each embodying a different element, banded together to find the legendary Genshin Book. Their journey took them through treacherous dungeons and hidden ruins, where they faced elemental guardians. When they finally located the book, they discovered it was not merely a collection of knowledge, but a sentient entity that reflected their collective spirit. As they wrote their adventures, the book revealed paths of destiny, showing them that their unity was the true power of Teyvat.",
            "An ancient prophecy foretold of a time when the Genshin Book would reveal itself to those pure of heart. A humble farmer named Elys sought to understand the elements that governed his crops. One day, while tilling the soil, he unearthed the book, shimmering with light. As he read, the book guided him in harnessing elemental magic to enrich his land. However, as his newfound power grew, so did the envy of those around him, leading to a confrontation that tested his values and the essence of harmony.",
            "A seasoned warrior named Thalia, weary from battles, discovered the Genshin Book while searching for a path to redemption. The book, filled with tales of valor and sacrifice, inspired her to confront her past mistakes. As she chronicled her journey of atonement, the book transformed her memories into vivid illustrations. Yet, with each entry, she faced the ghosts of her past, forcing her to reconcile with the choices that had led her to seek forgiveness.",
            "In a hidden temple deep within the Jade Forest, a wise monk named Jin unlocked the secrets of the Genshin Book through meditation and reflection. He learned that the book contained the essence of Teyvat\'s harmony, revealing how the elements interacted with one another. As he transcribed his insights, the book began to resonate with a calming energy. However, Jin soon discovered that external forces sought to disrupt this balance, prompting him to take action to protect the harmony of his world.",
            "An adventurous researcher named Corin was obsessed with uncovering the history of the archons. He believed that the Genshin Book contained the key to understanding their divine powers. After relentless pursuit, he unearthed the book beneath the ruins of an ancient shrine. As he translated its pages, the book revealed forgotten truths about the archons\' struggles and sacrifices. Yet, the more he learned, the more he realized that some truths were better left buried, leading him to question his quest for knowledge.",
            "A talented craftsman named Orin sought to create a masterpiece that embodied the essence of Teyvat. To guide him, he discovered the Genshin Book, which infused his creations with elemental magic. As he designed each artifact, the book illustrated its potential uses and the stories behind them. However, as his fame grew, he faced moral dilemmas about the power of his creations, forcing him to confront the ethical implications of wielding such magic.",
            "Lastly, an elusive entity known as the Celestial Weaver claimed to have crafted the Genshin Book itself. They invited a group of scholars and adventurers to explore its depths, promising revelations about the universe. As they entered the realm of the book, they were drawn into a tapestry of time and space, witnessing the intertwining fates of Teyvat\'s inhabitants. Each choice they made within the book altered the threads of destiny, challenging them to understand the impact of their actions on the world around them."
        ],
        "Iterious_Book": [
            "In the ethereal realm of Iteria, where time flowed like a river, a gifted scribe named Elowen sought to create a book that could capture the essence of moments. She gathered fragments of time from the Celestial Springs, infusing them into parchment crafted from the wings of time-frozen butterflies. As she wrote her first entry, the Iterious Book began to shimmer, reflecting events that had yet to unfold. However, with every story she penned, the lines between past and future blurred, leading Elowen to a revelation that could alter her destiny.",
            "A reclusive mage named Caelum discovered the Iterious Book in a hidden chamber beneath the Tower of Time. The book was rumored to hold the secrets of temporal magic. As Caelum studied its pages, he learned to manipulate time itself, creating loops and echoes of the past. Yet, as he experimented, he realized that altering time came with dire consequences, drawing the attention of ancient guardians who would do anything to protect the integrity of the timeline.",
            "In the bustling marketplace of Iteria, a young street artist named Mira found the Iterious Book left behind by an unknown traveler. Intrigued by its blank pages, she began to sketch the stories of those around her. With each stroke, the book came alive, depicting the emotions and dreams of the townspeople. However, as she unearthed their hidden truths, Mira discovered a dark secret that bound the lives of her neighbors, forcing her to choose between preserving their stories or revealing their burdens.",
            "A brilliant inventor named Thorne sought to create a device that could visualize the flow of time. He believed the Iterious Book held the key to understanding the mechanics of temporal travel. After extensive research, Thorne constructed a machine powered by the essence of the book. When he activated it, he was propelled into different timelines, witnessing alternate versions of his life. Yet, with each journey, he encountered versions of himself that challenged his choices, leading him to confront the nature of fate.",
            "A wise elder known as Lyric was tasked with preserving the history of Iteria. She discovered the Iterious Book, said to contain the knowledge of past civilizations. As she transcribed the tales of her ancestors, the book began to glow, revealing long-lost secrets of magic and technology. However, as she dove deeper into history, she learned of a forgotten conflict that threatened to resurface, and she had to rally her people to prevent the past from repeating itself.",
            "In the heart of the Twilight Forest, a daring explorer named Jaxon stumbled upon the Iterious Book guarded by ancient spirits. He was drawn to its promise of adventure and decided to document his journey through the forest. As he wrote, the book revealed hidden paths and secrets, guiding him toward untold treasures. However, he soon realized that the spirits were testing his courage and integrity, pushing him to prove himself worthy of the knowledge contained within the pages.",
            "A talented musician named Seraphina found the Iterious Book during a fateful performance. The book resonated with her melodies, transcribing the music into visual symphonies that depicted the flow of time. With each song she played, the book unfolded stories of love, loss, and redemption. Yet, as her fame grew, so did the pressure to maintain her artistic voice, leading her to confront the dichotomy of her passion and the expectations of the world around her.",
            "A courageous knight named Orion sought to protect his realm from dark forces threatening to disrupt the fabric of time. He learned of the Iterious Book, rumored to contain prophecies of the future. As he consulted the book, he was faced with visions of potential outcomes, forcing him to make critical decisions that would impact the lives of countless souls. Each choice weighed heavily on him, revealing the intricate connections between past actions and future consequences.",
            "An ambitious scholar named Thalia dedicated her life to unraveling the mysteries of time. She believed the Iterious Book was the key to unlocking the secrets of existence. Through relentless study, she managed to imbue the book with her own essence, allowing it to reflect her thoughts and emotions. As she documented her findings, she found herself entangled in a web of timelines that led her to confront her fears, desires, and the very nature of reality itself.",
            "Lastly, an enigmatic figure known only as the Timekeeper approached a group of adventurers, revealing that the Iterious Book was a living entity that needed protectors. They were chosen to embark on a quest to safeguard its power. As they traveled through time, they discovered the intricate threads that connected all beings. However, as they delved deeper into the book\'s essence, they faced a looming threat that sought to unravel the timeline itself, forcing them to unite and stand against the darkness."
        ],
        "Manhatan_Book": [
            "In the heart of the bustling city of Manhatan, a gifted artist named Alira yearned to capture the vibrant essence of her world. She believed the Manhatan Book could be a living canvas, reflecting the dreams and struggles of its citizens. After gathering rare inks made from crushed gemstones, she began to illustrate the stories of the city\'s diverse inhabitants. Each stroke of her brush brought the pages to life, but as she painted, she uncovered hidden desires and secrets that would challenge her perception of happiness.",
            "A reclusive scholar known as Eldrin discovered the Manhatan Book hidden in the library of forgotten tales. Intrigued by its promise of wisdom, he delved into its pages, where he found a map leading to lost artifacts scattered across the city. With every artifact he retrieved, the book revealed the stories behind them, intertwining history with the present. However, Eldrin soon realized that his quest awakened ancient guardians who would stop at nothing to protect the city\'s hidden legacy.",
            "In the smoky depths of the Manhatan underworld, a daring thief named Kael stumbled upon the Manhatan Book during a heist. Initially seeking fortune, he soon became enchanted by its power to reveal hidden truths. As he transcribed his escapades, the book began to resonate with his desires and regrets. However, the more he wrote, the more he found himself drawn into a web of intrigue, forcing him to confront the shadows of his past and the cost of his choices.",
            "A passionate musician named Selene believed that the Manhatan Book held the key to creating the perfect symphony. She gathered tales of love, loss, and joy from the city\'s residents and infused them into her compositions. As she played, the book absorbed her melodies, transforming them into vivid stories. Yet, as her fame grew, Selene faced the pressures of the music industry, challenging her authenticity and pushing her to rediscover the true essence of her art.",
            "In a remote corner of Manhatan, an eccentric inventor named Thorne sought to harness the power of dreams. He believed the Manhatan Book could serve as a bridge between reality and imagination. Through elaborate contraptions, he connected the book to the dreams of the city\'s inhabitants. As he transcribed their visions, the book transformed, reflecting their hopes and fears. However, Thorne soon discovered that manipulating dreams had unforeseen consequences, leading to a chaotic clash between fantasy and reality.",
            "A fearless journalist named Nyra aimed to uncover the truth behind Manhatan\'s myths. Armed with the Manhatan Book, she embarked on a journey to interview the city\'s most elusive figures. As she documented their stories, the book revealed a tapestry of interconnected lives, exposing a conspiracy that could alter the city's future. Yet, as she delved deeper, Nyra found herself entangled in danger, with powerful forces trying to silence her.",
            "An aging historian named Magnus devoted his life to studying the legends of Manhatan. When he stumbled upon the Manhatan Book, he believed it contained the answers to the city\'s mysteries. As he transcribed ancient tales, the book\'s magic awakened, bringing the legends to life. However, with each story, Magnus realized that the past was not as he had imagined, forcing him to reconcile his idealized views with the harsh realities of history.",
            "A gifted dreamweaver named Lyra sought to create a sanctuary for lost souls. She discovered that the Manhatan Book could capture the essence of their stories and bring them peace. As she collected the narratives of those who had suffered, the book transformed, weaving their experiences into a healing tapestry. Yet, as the stories intertwined, she faced a moral dilemma about how to honor their memories without losing her own identity in the process.",
            "An ambitious architect named Orin envisioned a grand structure that would symbolize unity in Manhatan. To bring his vision to life, he turned to the Manhatan Book, seeking inspiration from the city\'s rich history. As he explored its pages, he discovered architectural wonders lost to time. However, as he incorporated these designs, he encountered resistance from those who feared change, forcing him to navigate the fine line between innovation and tradition.",
            "Lastly, a mystical oracle known as Seraphine claimed that the Manhatan Book was destined to choose its keeper. She gathered a group of individuals, each with unique talents, to test their worthiness. As they faced trials set by the book, they unraveled secrets about themselves and the city. Ultimately, they learned that the true power of the Manhatan Book lay not in its contents but in the connections forged through their shared journeys."
        ],
        "Monster_Book": [
            "In a forgotten corner of the realm, an enigmatic sorcerer named Kellan sought to document the myriad monsters that roamed the land. He believed that by capturing their essence within the pages of the Monster Book, he could bridge the gap between fear and understanding. Gathering rare ingredients from the depths of the Shadow Woods, he infused the book with a magic that allowed it to record the attributes and stories of each creature he encountered. However, as he penned the first entry, he realized that the creatures were not merely monsters, but guardians of ancient secrets, each with its own tragic tale.",
            "A daring adventurer named Lira discovered the Monster Book while exploring the ruins of a long-lost city\'. Intrigued by its allure, she opened its pages to find vivid illustrations of beasts that had once roamed the earth. As she traveled the realm, collecting tales of encounters with these creatures, the book came alive with her own experiences. Yet, with each story she added, she found herself hunted by a monstrous entity that sought to reclaim its story from her, leading her on a treacherous quest to uncover the truth behind the creature's wrath.",
            "In a small village on the outskirts of the city\', a group of children discovered the Monster Book hidden beneath the roots of an ancient tree. Fascinated, they began to write their own stories about the mythical beasts they imagined. As they filled the pages with their tales, the book began to shimmer, transforming their childhood fears into tangible creatures that manifested in the world. Yet, as the children played, they unwittingly unleashed a creature born from their collective nightmares, forcing them to confront what they had created.",
            "A renowned scholar named Orin sought to compile the knowledge of every monster ever recorded. He believed the Monster Book could be the ultimate guide to understanding these beings. After years of research, he managed to conjure a portal that allowed him to witness the creatures in their natural habitats. As he documented their behaviors, he realized that the line between monster and misunderstood being was razor-thin. However, his relentless pursuit of knowledge attracted the attention of a powerful monster that sought to protect its kind from being exploited.",
            "A brave knight named Cedric, tasked with protecting the city\', uncovered the Monster Book in the ruins of an ancient castle. As he read its pages, he learned of legendary monsters that once roamed the realm. Inspired, he set out to hunt them, believing he could rid the world of their menace. However, as he faced each creature, he discovered that they were not the villains of the stories, but tragic figures shaped by circumstances, forcing him to rethink his role as a hero.",
            "A gifted artist named Sylas stumbled upon the Monster Book in a mysterious market. Enchanted by its allure, he began to illustrate the monsters described within. As he painted, the creatures began to emerge from the pages, bringing his art to life. Yet, as he infused his emotions into the illustrations, he found himself ensnared in a battle between the beauty of creation and the terror of the monsters, blurring the lines between artist and subject.",
            "In a hidden laboratory, a brilliant scientist named Dr. Elara sought to understand the biology of monsters. She believed that the Monster Book contained vital information that could help her create a serum to tame the wildest beasts. As she conducted experiments, she discovered that the book held a consciousness of its own, revealing the monsters\' deepest fears and desires. But as she delved deeper, she awakened a primal force that challenged her understanding of science and nature.",
            "A wandering bard named Finn came across the Monster Book in an old tavern. Intrigued, he began to sing the tales of each creature, hoping to charm them into friendship. As he strummed his lute, the creatures responded, revealing their stories through music and dance. However, he soon realized that not all monsters were eager for companionship; some harbored grudges against humanity, testing Finn\'s resolve as he sought to unite their worlds through song.",
            "A fierce warrior named Mira, driven by vengeance, found the Monster Book after a devastating attack on her village. She sought to learn about the monsters responsible for the destruction, hoping to take revenge. As she chronicled their tales, she discovered that the very monsters she sought to destroy were victims of a greater evil. This revelation forced her to confront her own motives and seek a path toward reconciliation instead of revenge.",
            "Lastly, a young apprentice named Riven stumbled upon the Monster Book in a dusty library. Entranced by its illustrations, he began to dream of becoming a monster tamer. As he trained to master the creatures depicted in the book, he realized that they were bound by ancient magic to protect the realm from dark forces. With the fate of the city\' at stake, Riven had to unite the monsters and harness their powers to confront an impending darkness that threatened to consume everything he loved."
        ],
        "NA_Book": [
            "In the mystical land of Domanus, a reclusive sage named Eldrin discovered an ancient scroll that spoke of a powerful tome known as the NA Book. Driven by curiosity, he embarked on a journey to gather the elements necessary to create this legendary book. He traveled across the land, collecting whispers of forgotten knowledge from the city's elders, each story weaving a tapestry of wisdom that would eventually fill the pages of the NA Book. However, as he wrote, he found himself entangled in a web of ancient rivalries that threatened to unravel his quest.",
            "A young sorceress named Lyra dreamed of crafting a book that would harness the raw energy of the universe. She believed the NA Book could channel the power of the stars themselves. To achieve this, she sought the guidance of the celestial beings that resided high above the city\'. As she performed her rituals, the sky lit up with cosmic energy, and the pages of the book began to glow. Yet, the more she sought power, the more she attracted the attention of a dark entity determined to claim her creation for itself.",
            "In a forgotten library, a passionate historian named Cedric stumbled upon the NA Book, its pages blank yet pulsating with potential. Driven by the desire to record the lost histories of the city\', he set out to gather stories from those who had lived through its most tumultuous times. Each tale he collected breathed life into the pages, but he soon realized that some stories held dark secrets that could reshape the city\'s future, leading him to question the morality of preserving certain truths.",
            "A fierce warrior named Kaela sought to create a legendary artifact that would record her adventures for future generations. She envisioned the NA Book as a living testament to her bravery. Gathering tales from her fellow warriors and chronicling her battles, Kaela infused the book with the essence of valor. However, with each entry, she uncovered a prophecy that foretold her own downfall, forcing her to confront her destiny and the choices she had made along the way.",
            "A curious inventor named Felix believed the NA Book could serve as a portal to other dimensions. He spent countless nights crafting intricate mechanisms to unlock its potential. As he wrote and illustrated fantastical worlds within the pages, he inadvertently opened a rift, allowing creatures from those dimensions to enter Domanus. As chaos ensued, Felix raced against time to close the portal and protect his city\' from the invasion of beings he had once only imagined.",
            "In the vibrant markets of the city\', a street artist named Mira found an ancient blank book. Inspired, she began to fill its pages with her art, capturing the beauty and struggles of everyday life. As she painted, the NA Book absorbed her emotions, creating a living narrative of the city\'s heart. Yet, her art also attracted the ire of a corrupt noble who sought to control her gift, forcing Mira to fight for her freedom and the authenticity of her work.",
            "An ambitious bard named Rowan sought to compose a symphony that would echo through the ages. He believed the NA Book could capture the melodies of the world. As he gathered stories and songs from the inhabitants of the city\', the book transformed, resonating with the harmony of their lives. However, as Rowan delved deeper into the book\'s magic, he found himself caught in a battle between light and darkness, where music could heal or destroy.",
            "A gentle healer named Elara believed that the NA Book could hold the key to understanding the secrets of life itself. She traveled to the city\'s oldest groves, gathering wisdom from nature and ancient spirits. Each entry she made blossomed with healing energy, but as she unlocked the book\'s secrets, she discovered a darker truth about the balance of life and death, forcing her to confront her own role in the cycle of existence.",
            "A timekeeper named Orion believed that the NA Book could chronicle the passage of time itself. He sought to capture moments from the city\'s past, present, and future. As he penned the stories of time, the book began to warp reality around him, blending timelines and creating alternate futures. Orion faced a dilemma: to preserve history or alter the fate of his city\', all while battling the consequences of time\'s fluid nature.",
            "Finally, a gifted dreamer named Nyx found the NA Book in the depths of her dreams. She believed it could manifest her visions into reality. As she wrote her dreams, the book brought her creations to life, but with every dream fulfilled, a nightmare emerged. Nyx had to learn to balance her imagination with responsibility, understanding that not all dreams were meant to be realized."
        ],
        "OP_Book": [
            "In a hidden workshop beneath the bustling city, an eccentric mage named Thalion decided to create a book unlike any other. The OP Book was to be a compilation of the most potent spells and artifacts known to the realm. Thalion gathered rare materials, including dragon scales and phoenix feathers, believing these components would imbue the book with extraordinary power. However, as he infused the spells into the pages, he inadvertently attracted the attention of dark forces that sought to claim the book for themselves.",
            "A brilliant alchemist named Selene dreamed of crafting the OP Book to preserve the secrets of her craft. She envisioned a tome that would adapt and evolve with every potion and elixir she created. As she collected ingredients from the farthest corners of the city, Selene discovered that the book had a will of its own, reacting to her emotions and intentions. Each experiment she documented transformed the book, leading her down a path where her successes and failures could become both a blessing and a curse.",
            "In a forgotten library, a young scholar named Elden stumbled upon an ancient manuscript detailing the creation of the OP Book. Intrigued, he followed the instructions meticulously, gathering knowledge from the city\'s elders and long-lost texts. As he penned the spells, he discovered that the book held echoes of its past creators, revealing their triumphs and tragedies. Elden realized that creating the OP Book meant shouldering the legacies of those who had come before him, blurring the line between creator and creation.",
            "A fearless warrior named Aric, seeking to document his legendary feats, decided to collaborate with a wise sage to create the OP Book. They believed it would serve as a guide for future heroes. Together, they traveled across the realm, collecting stories of bravery and valor from the inhabitants of the city. However, as they compiled the tales, they unwittingly summoned a formidable adversary who sought to erase the legacy they were attempting to preserve.",
            "An ambitious sorceress named Lira set out to craft the OP Book to capture the essence of magic itself. She believed it could contain every spell ever conceived. As she journeyed through the city, collecting knowledge from ancient artifacts and hidden shrines, the book began to pulse with energy. But with great power came great responsibility; Lira soon realized that her quest could tip the balance of magic in Domanus, forcing her to confront the ethical implications of her creation.",
            "A gifted bard named Fenwick envisioned the OP Book as a collection of songs that could influence the hearts of men. He traveled through the city, gathering melodies and tales from all walks of life. As he wrote, the book resonated with the emotions of those whose stories he captured. However, he soon discovered that not all songs were meant to be sung, and some melodies carried dark enchantments that could sway the minds of even the strongest warriors.",
            "A timekeeper named Orion believed the OP Book could document the fabric of time itself. He sought to record significant moments from the history of the city, hoping to create a timeless masterpiece. However, as he penned the entries, he found that altering even a single word could disrupt the very flow of history. Orion had to navigate the delicate threads of time while ensuring that the OP Book remained a true reflection of the past, present, and future.",
            "A noblewoman named Isolde, seeking to empower her people, envisioned the OP Book as a manual of strength and resilience. She gathered stories of perseverance from the city\'s most inspiring figures. As she compiled their tales, the book took on a life of its own, becoming a beacon of hope. Yet, as Isolde shared its teachings, she faced opposition from those who feared the empowerment of the masses, testing her resolve to create change.",
            "A reclusive inventor named Balthazar sought to blend technology and magic in the OP Book. He envisioned it as a tool that could enhance the abilities of those who wielded it. As he crafted intricate mechanisms and spells, he created a book that responded to the user\'s intent. However, Balthazar\'s innovations attracted the attention of rival inventors who sought to steal his creation, leading to a race to protect the OP Book and its powerful secrets.",
            "Finally, a wandering dreamer named Nyx found herself drawn to the OP Book, believing it could manifest her visions into reality. As she poured her dreams into its pages, the book transformed into a conduit of creation. However, Nyx soon learned that dreams could easily become nightmares, and she had to learn to navigate the thin line between imagination and reality to safeguard her creation from descending into chaos."
        ],
        "Othellonia_Book": [
            "In the heart of the enchanted city\, a renowned scholar named Elowen discovered fragments of an ancient manuscript hinting at the creation of the Othellonia Book. Intrigued, she began her quest to gather the lost knowledge hidden in the city\'s archives. As she pieced together the stories of past creators, Elowen realized that the book would not only contain spells but also the essence of those who had once wielded power. Little did she know, her pursuit would awaken a long-dormant guardian intent on protecting the secrets of the past.",
            "A gifted artist named Kaelan envisioned the Othellonia Book as a canvas for his vibrant dreams. He believed that by painting his visions, he could bring magic to life. As he roamed the bustling markets of the city, capturing the essence of its people, Kaelan infused the book with colors that danced across the pages. However, with each stroke of his brush, he found himself trapped in a vivid world of his own making, where reality blurred with imagination, and the lines between creator and creation began to fade.",
            "An ambitious mage named Fennel sought to create the Othellonia Book to serve as a guide for aspiring spellcasters. He believed that by compiling the wisdom of the city\'s greatest sorcerers, he could unlock the true potential of magic. Fennel traveled to the highest peaks and deepest caverns, gathering spells and insights. But as he penned each entry, he uncovered a prophecy that warned of a great imbalance in the magic of Domanus, forcing him to confront the implications of his creation.",
            "In a secluded glade, a wise druid named Aeloria decided to document the natural magic of the world in the Othellonia Book. She believed that by recording the harmonious balance of nature, she could teach future generations to respect the earth. As she transcribed her observations, the book began to resonate with the energy of the flora and fauna around her. Yet, as she delved deeper into her studies, she realized that some secrets of nature were best left undiscovered, and her quest could unleash forces beyond her control.",
            "A time traveler named Orion stumbled upon the Othellonia Book in a distant future, where it was revered as a relic of wisdom. Intrigued, he used his knowledge to alter its contents, hoping to influence the past. However, each change he made rippled through time, creating unintended consequences. As he faced the chaotic fallout of his actions, Orion had to navigate the complex threads of fate to restore balance to the timeline while safeguarding the book\'s integrity.",
            "A courageous knight named Sir Cedric aimed to write the Othellonia Book as a testament to the valor and bravery of the city\'s protectors. He gathered tales from veterans and heroes, believing that their stories could inspire hope. As he chronicled their adventures, the book began to manifest the spirit of heroism, but it also attracted the attention of dark forces who sought to extinguish that light. Sir Cedric found himself in a battle not only for the book but for the very soul of his city.",
            "A clever rogue named Mira aimed to create the Othellonia Book as a collection of secrets and skills for those living in the shadows. She traveled through the underbelly of the city, gathering wisdom from thieves, assassins, and spies. Each entry was filled with cunning strategies and survival tactics. Yet, as she compiled these tales, Mira realized that the knowledge could easily fall into the wrong hands, leading to chaos and betrayal among the city\'s underworld.",
            "A visionary inventor named Leon sought to integrate technology and magic within the Othellonia Book. He believed that the fusion of the two could revolutionize the way magic was used. As he crafted intricate mechanisms and wrote spells that enhanced his inventions, the book transformed into a living tool. However, as he pushed the boundaries of innovation, Leon encountered unforeseen glitches that threatened to destabilize the delicate balance between technology and sorcery.",
            "An enigmatic oracle named Seraphine had a vision of the Othellonia Book as a chronicle of destiny itself. She believed that by writing the fates of individuals, she could alter the course of events in the city. As she inscribed prophecies and dreams, the book began to reflect the choices of those who read it, shaping their destinies. However, Seraphine soon learned that tampering with fate could lead to dire consequences, and she had to decide whether to embrace her power or let fate run its course.",
            "Finally, a humble bard named Arin envisioned the Othellonia Book as a testament to the stories of everyday life in the city. He believed that every voice mattered and sought to include tales from all walks of life. As he collected stories from common folk, the book blossomed with the rich tapestry of humanity. Yet, as Arin wove these narratives together, he realized that some stories contained truths that were better left untold, challenging him to balance honesty with compassion."
        ],
        "SAO_book": [
            "In a realm where technology and magic intertwined, a visionary programmer named Akira embarked on a journey to create the SAO Book. He envisioned it as an immersive experience that could capture the essence of virtual worlds. To bring his idea to life, Akira traveled to the city, where he sought the help of skilled mages and engineers. Together, they combined ancient spellcraft with modern coding, creating a digital tome that would revolutionize how stories were told. However, their ambitious project inadvertently opened a portal to an alternate dimension, unleashing forces they could not control.",
            "A talented game designer named Mira discovered an ancient artifact during her exploration of the city. This artifact whispered secrets of a forgotten civilization and inspired her to create the SAO Book, a guide to unlocking the mysteries of virtual realities. As she documented her findings, Mira infused the book with powerful spells that could alter the very fabric of the game worlds. Yet, the deeper she delved into the artifact's magic, the more she realized it had its own agenda, threatening to merge reality with the virtual realm in unforeseen ways.",
            "A young hacker named Riku believed that the SAO Book could be a tool for revolutionizing the digital landscape. He sought to create a manual for aspiring hackers, detailing techniques to navigate the complexities of virtual security. As Riku compiled his knowledge, he faced opposition from powerful corporate entities that sought to silence him. The book quickly became a target, and Riku had to navigate a dangerous game of cat and mouse, all while trying to protect the secrets he had unearthed.",
            "An aspiring writer named Yuna envisioned the SAO Book as a platform for sharing stories from across the virtual worlds. She gathered tales from players around the city, hoping to create a rich anthology that showcased the diversity of experiences. However, as she wove their narratives into the book, she uncovered a dark conspiracy among players who had lost themselves in their virtual personas, leading her to question the true meaning of identity in a world where reality and fantasy blurred.",
            "A wise sage named Jareth sought to create the SAO Book as a living archive of wisdom and knowledge for future generations. He believed that by documenting the teachings of both ancient and modern thinkers, he could bridge the gap between the two worlds. As he traveled through the city, gathering insights, he found that the book had a consciousness of its own, responding to the emotions and intentions of its readers. Jareth soon realized that creating a book with such power came with responsibilities that could change the course of history.",
            "A skilled warrior named Kael wanted to craft the SAO Book to serve as a guide for heroes in training. He aimed to compile strategies, combat techniques, and tales of valor from the city. As he sought out experienced fighters, he inadvertently attracted the attention of malevolent beings who sought to thwart his mission. Kael found himself in a race against time to complete the book before the dark forces could eliminate the knowledge he was striving to preserve.",
            "A brilliant scientist named Sera dreamed of merging consciousness with the digital world through the SAO Book. She aimed to document the experiences of players and their interactions within virtual environments. As she conducted experiments in her lab, the book began to evolve, capturing emotions and memories in a way that no one had anticipated. However, Sera soon discovered that her experiments had unintended side effects, threatening the stability of both the virtual and real worlds.",
            "A charismatic bard named Arin sought to create the SAO Book as a collection of songs that resonated with the heart of the virtual realm. He believed that music could connect players on a deeper level. As he traveled the city, gathering melodies and lyrics, he infused the book with enchanted notes. Yet, as the music played, Arin realized that some songs had the power to manipulate emotions, leading to unforeseen consequences in the relationships between players.",
            "A mysterious oracle named Nyx envisioned the SAO Book as a prophecy of the future of gaming. She believed that by documenting the trends and changes within virtual worlds, she could foresee the paths they would take. As she wrote her predictions, the book began to reveal glimpses of possible futures, but with each revelation, Nyx struggled with the weight of knowledge and the ethical implications of altering fate through her writings.",
            "Finally, a curious child named Leo stumbled upon an unfinished version of the SAO Book hidden within a forgotten corner of the city. Captivated by its potential, he decided to complete the book by gathering stories and experiences from his friends. As they shared their adventures, the book came to life, connecting the community in ways they never imagined. Yet, as Leo realized the power of their collective stories, he understood that the true magic of the SAO Book lay not in the tales themselves but in the bonds they forged."
        ],
        "Tanhagan_Book": [
            "In the mystical land of Tanhagan, a legendary scribe named Eldrin embarked on a quest to create a book that would capture the essence of all magical creatures. With a quill made from the feather of a phoenix, he traveled through enchanted forests and treacherous mountains, documenting the lore of fairies, dragons, and ancient spirits. However, as he wrote, he discovered that the more he recorded, the more these creatures came to life on the pages, blurring the lines between reality and imagination.",
            "A brilliant alchemist named Lyra believed that the Tanhagan Book could hold the secrets of potions and spells lost to time. Gathering rare ingredients from the farthest reaches of the kingdom, she experimented tirelessly to unlock the mysteries of alchemical transformation. Yet, in her pursuit of knowledge, she accidentally unleashed a powerful elixir that threatened to engulf Tanhagan in chaos, forcing her to find a way to reverse her creation before it was too late.",
            "In the heart of the city, a young bard named Farren sought to fill the Tanhagan Book with songs and tales of heroism. He traveled from village to village, collecting stories of brave warriors and their deeds. But as Farren wove these narratives into the book, he noticed that the heroes from his tales began to manifest in the real world, drawn by the power of his words. Farren soon realized that with great power came great responsibility, as these heroes needed guidance in their newfound existence.",
            "A mysterious oracle named Seraphine envisioned the Tanhagan Book as a chronicle of prophecies and destinies. As she wrote about the future of Tanhagan, she found herself entwined in a web of fate that threatened her own existence. Each prophecy she penned altered the fabric of reality, leading her to a race against time to rewrite the destinies she had inadvertently changed, while grappling with the weight of foreknowledge.",
            "A cunning thief named Kael saw the Tanhagan Book as a means to unlock hidden treasures and ancient artifacts. He infiltrated the grand library of Tanhagan, stealing fragments of forbidden texts to create his own version of the book. However, as he pieced together the lore, he attracted the attention of powerful guardians who would stop at nothing to protect their secrets. Kael soon found himself in a perilous game of cat and mouse, as he fought to uncover the truth while evading capture.",
            "A devoted historian named Mira dedicated her life to preserving Tanhagan\'s history through the creation of the Tanhagan Book. As she unearthed ancient scrolls and artifacts, she discovered a long-lost civilization that had once thrived. But her quest for knowledge awakened spirits of the past, who were not pleased with her meddling. Mira had to navigate the delicate balance between honoring their legacy and protecting her own life from the vengeful spirits she inadvertently disturbed.",
            "A talented artist named Orion sought to illustrate the wonders of Tanhagan within the pages of the Tanhagan Book. He traveled to distant lands, capturing the beauty of landscapes and creatures. Yet, as he painted, his brush strokes infused the illustrations with life, causing them to leap off the pages. Orion soon found himself in a fantastical adventure, as his creations took on a life of their own, leading him on a journey through the very worlds he had captured in his art.",
            "A wise elder named Thalion believed that the Tanhagan Book could serve as a guide to the future of magic in the land. He gathered the greatest minds of the era to share their insights and philosophies. As he compiled their teachings, however, he encountered a dark force that sought to suppress the knowledge within the book. Thalion had to rally the scholars to defend their work and ensure that the wisdom of the past would shine through the darkness of ignorance.",
            "A humble farmer named Elara stumbled upon the Tanhagan Book while tending to her fields. Intrigued by its promise of magic, she began to experiment with the spells within. Her small farm flourished, but her newfound abilities attracted the attention of a powerful sorceress who saw Elara as a threat. As the sorceress plotted to reclaim the book, Elara had to harness her inner strength and learn the true meaning of power, not just in magic, but in her heart.",
            "Finally, a curious child named Leo discovered the unfinished Tanhagan Book hidden in a forgotten corner of the library. Fascinated, he gathered stories from friends and family to fill its pages. As Leo and his friends shared their adventures, the book began to weave their narratives into a grand tapestry of Tanhagan\'s future. Unbeknownst to them, their collective imagination had the power to shape the destiny of their world, teaching them that the true magic of storytelling lay in their unity and creativity."
        ],
        "Tensei_shitara_Slime_Datta_Ken_Book": [
            "In a realm where magic intertwines with reality, a reclusive author named Shiro found an ancient tome that spoke of reincarnation and transformation. Inspired by the tale of a slime gaining consciousness, Shiro set out to weave a narrative that transcended traditional storytelling. As he wrote, his words seemed to shimmer with magic, drawing the attention of various creatures who longed to be part of his world, transforming the manuscript into a living legend.",
            "An ambitious sorceress named Mira believed that the Tensei shitara Slime Datta Ken Book could contain powerful spells that could alter the fate of their world. She delved deep into forbidden magic, infusing the pages with the essence of slimes she captured. However, the more she tried to control the magic, the more unpredictable it became. She soon learned that some powers were not meant to be contained, leading her on a dangerous journey of self-discovery and redemption.",
            "A young boy named Riku stumbled upon a mysterious library in the heart of a bustling city. Among the dusty shelves, he found the Tensei shitara Slime Datta Ken Book, filled with tales of adventure and camaraderie. Captivated by its stories, Riku shared the book with his friends, inadvertently bringing the characters to life. Together, they embarked on a quest to understand the magic of friendship and the strength it bestowed, uncovering secrets hidden within the pages.",
            "In a village beset by darkness, a brave warrior named Kael sought the Tensei shitara Slime Datta Ken Book to find a way to save his people. Guided by cryptic prophecies written within the book, Kael journeyed through treacherous lands, facing challenges that tested his resolve. Each step he took not only revealed more about the book's origins but also transformed him in unexpected ways, blurring the line between hero and monster.",
            "A curious scholar named Elara dedicated her life to studying the magic of slimes. Her research led her to the Tensei shitara Slime Datta Ken Book, believed to hold the key to mastering slime magic. As she experimented with the spells within, she accidentally created a sentient slime companion named Lumo. Together, they unraveled the mysteries of the book, discovering the bonds between magic and nature, while navigating the challenges of their evolving relationship.",
            "A guild of adventurers stumbled upon the Tensei shitara Slime Datta Ken Book during one of their quests. Intrigued by its tales of transformation, they decided to recreate the legendary slime\'s journey within their own lives. Each member took on a different aspect of the slime\'s adventures, leading to hilarious mishaps and profound lessons about teamwork and resilience as they learned to appreciate their unique strengths.",
            "A lonely mage named Sorin believed that by documenting his life in the Tensei shitara Slime Datta Ken Book, he could finally connect with the world. As he poured his heart into the pages, he discovered a hidden power that allowed his emotions to manifest as magical slimes. These slimes became his friends, teaching him about the importance of vulnerability and the bonds that transcend loneliness, ultimately changing his fate.",
            "A mischievous trickster named Jiro found the Tensei shitara Slime Datta Ken Book in a market stall. Seeing it as an opportunity for mischief, he started rewriting the stories for his amusement. However, his antics attracted the attention of a powerful guardian who sought to protect the book's true essence. Jiro\'s journey transformed from mere trickery to a quest for redemption, forcing him to confront his own identity and the impact of his actions.",
            "A noble queen, desperate to bring peace to her war-torn kingdom, sought guidance from the Tensei shitara Slime Datta Ken Book. Within its pages, she discovered tales of unity and resilience among various factions. Inspired, she organized a summit based on the book\'s teachings, uniting enemies and forging bonds that had long been severed, ultimately changing the course of history in her realm.",
            "Finally, a child named Nia, who always felt out of place, found solace in the Tensei shitara Slime Datta Ken Book. The stories of transformation resonated deeply with her, encouraging her to embrace her uniqueness. As she shared the tales with her classmates, she inspired them to see their own potential. Together, they learned that even the smallest beings could make a difference, and that true strength lies in accepting oneself."
        ],
        "Touhou_Book": [
            "In the mystical land of Gensokyo, a young shrine maiden named Reimu Hakurei stumbled upon an ancient artifact buried deep within the shrine\'s grounds. This artifact, pulsating with magical energy, was a forgotten tome known as the Touhou Book. As Reimu opened its pages, she discovered tales of powerful beings and legendary battles that shaped Gensokyo. The stories not only chronicled past events but also revealed the secrets of the magic that flowed through the land. Intrigued, Reimu embarked on a quest to uncover the truth behind each tale, hoping to protect Gensokyo from emerging threats.",
            "A reclusive artist named Yukari Yakumo, known for her ability to manipulate boundaries, decided to create the Touhou Book as a means to document the intricate relationships among the residents of Gensokyo. Using her powers, she gathered snippets of conversations, memories, and dreams from various inhabitants. Each entry she wrote transformed into vivid illustrations, bringing the characters to life within the pages. However, as the book grew, so did the complexity of the stories, weaving a web of intrigue and unforeseen consequences that affected everyone in Gensokyo.",
            "The enigmatic magician Marisa Kirisame, always in search of powerful artifacts, heard whispers of the Touhou Book that contained untold magic. Believing it could grant her immense power, she embarked on a thrilling adventure to find the book\'s hidden location. Along the way, Marisa encountered various adversaries and allies, each with their own connection to the book. As she pieced together the fragments of the stories within, she realized that the true magic lay not in the power the book promised, but in the friendships and bonds formed during her journey.",
            "A dedicated historian named Sakuya Izayoi aimed to preserve the history of Gensokyo by compiling the tales of its inhabitants into the Touhou Book. Her meticulous nature allowed her to gather stories from everyone, from the lowest youkai to the highest deities. However, as she collected the tales, Sakuya discovered that some stories were lost to time and memory. Determined to revive these forgotten tales, she traveled through time, encountering pivotal moments in Gensokyo\'s history and bringing back the voices that had been silenced, ultimately enriching the book\'s legacy.",
            "The Touhou Book began as a simple diary belonging to a little fairy named Cirno. Filled with childish scribbles and playful anecdotes about her daily adventures, the book\'s magic was awakened when Cirno accidentally spilled a potion on it. The stories transformed into grand adventures, where Cirno found herself facing powerful foes and forming unlikely alliances. As her tales became more dramatic and exciting, Cirno learned valuable lessons about friendship, bravery, and the consequences of her actions, evolving from a carefree fairy into a true heroine.",
            "A curious tengu journalist named Aya Shameimaru decided to document the events surrounding the Touhou Book. With her unique perspective, she interviewed various characters and collected their thoughts on the book\'s significance in Gensokyo. As Aya delved deeper, she uncovered hidden conflicts and unresolved tensions that had existed for centuries. The book became a reflection of the delicate balance between harmony and chaos, prompting Aya to confront her own biases and ultimately reshape her understanding of the world around her.",
            "In an attempt to harness the power of storytelling, the wise sage Kanako Yasaka sought to create a book that would change the fate of Gensokyo. She believed that the Touhou Book could rewrite reality itself. To achieve this, she enlisted the help of the wind goddess, Suwako Moriya. Together, they infused the book with divine essence and imbued it with the ability to bring tales to life. However, as the stories unfolded, they began to unravel the fabric of Gensokyo, forcing Kanako and Suwako to confront the dangers of wielding such immense power.",
            "The Touhou Book became the subject of a fierce competition among Gensokyo\'s most talented writers. Each character sought to contribute their own story, hoping to leave a mark on the book\'s pages. As they crafted their tales, rivalries and alliances formed, leading to unexpected outcomes. Through laughter, tears, and fierce determination, the characters discovered that the true essence of the Touhou Book lay not in individual glory, but in the shared experiences and the collective strength of their community.",
            "In a moment of desperation, the inhabitants of Gensokyo faced a great calamity that threatened to erase their existence. A brave group of characters banded together to create the Touhou Book as a means of preserving their stories and memories. Through intense struggles and sacrifices, they poured their souls into the book, ensuring that their legacy would survive even in the face of oblivion. As the book became a vessel of hope, it also transformed into a beacon of resilience, inspiring future generations to remember their past.",
            "The Touhou Book itself became sentient, absorbing the emotions and experiences of its readers. It began to communicate with them, guiding them on their own journeys of self-discovery. Each interaction created a unique narrative, intertwining the lives of the characters with those of the readers. As they shared their stories, the Touhou Book evolved into a living chronicle of Gensokyo\'s adventures, solidifying its place as a cherished treasure that would forever inspire those who sought to explore its pages."
        ],
        "Xenoraphine_Book": [
            "In the ethereal realm of Xenoraphine, where dreams and reality intertwine, a visionary scholar named Elara discovered a mystical manuscript hidden deep within the ruins of an ancient temple. This manuscript contained fragments of stories from different dimensions, each resonating with the energies of their respective worlds. Elara, driven by an insatiable curiosity, began the arduous task of piecing together these fragments, unwittingly awakening powerful entities that would soon challenge her every step.",
            "A young sorceress named Nyx, fascinated by the stories of heroes and legends, sought to create the Xenoraphine Book as a way to capture the essence of bravery. She traveled through various realms, collecting tales of valor from warriors, mages, and mythical creatures. As she gathered these stories, Nyx discovered that some heroes bore dark secrets. The book became a reflection of their struggles, revealing that bravery often came hand in hand with sacrifice and redemption.",
            "A reclusive artist named Thalion stumbled upon the Xenoraphine Book while searching for inspiration. The book, however, was no ordinary tome; it had the ability to manifest the art created from its pages. Intrigued, Thalion began to illustrate the stories within, breathing life into each character and scene. As the illustrations came alive, they started to spill out into the real world, blurring the lines between creation and creator, leading to chaos and unforeseen adventures.",
            "Deep within the enchanted forests of Xenoraphine, a group of ancient guardians known as the Sentinels decided to forge the Xenoraphine Book to protect their realm. Each Sentinel contributed a story from their rich history, infusing the book with protective magic. However, as the tales intertwined, they uncovered a prophecy foretelling an impending darkness that would threaten their existence. Together, they had to decipher the hidden meanings within their stories to thwart the coming doom.",
            "A daring explorer named Kaelan embarked on a quest to find the legendary Xenoraphine Book, rumored to contain the lost knowledge of the ancients. Along his journey, Kaelan encountered various challenges and met peculiar beings who guided him with their stories. Each encounter enriched the book\'s pages, revealing the interconnectedness of all life. In the end, Kaelan learned that the true treasure lay not in the book itself, but in the wisdom gained through his experiences and the bonds formed along the way.",
            "In a world where emotions shaped reality, a young empath named Lira discovered that her ability to feel the emotions of others allowed her to tap into their stories. Driven by compassion, she began to compile the tales of love, sorrow, and triumph in the Xenoraphine Book. As she wrote, she realized that each story held the power to heal wounds and bridge divides. The book transformed into a beacon of hope, uniting disparate realms through shared experiences and empathy.",
            "The ancient dragon Sorath, protector of Xenoraphine, grew weary of the conflicts plaguing his realm. He decided to create the Xenoraphine Book as a means to teach harmony and understanding among the races. Sorath summoned the wisest beings from across the land to share their stories of unity. As the tales were woven together, they revealed the beauty of cooperation and the strength found in diversity, inspiring generations to live in peace.",
            "In a desperate attempt to change their fate, a council of witches conspired to create the Xenoraphine Book, believed to grant the power of foresight. However, their ambition led to unintended consequences as the book began to show future events in a chaotic and fragmented manner. The witches realized that knowledge of the future came with great responsibility. They had to confront their own desires and the ethical implications of their creation to restore balance to their world.",
            "A bard named Elysia, gifted with the ability to weave magic into music, sought to capture the melodies of the Xenoraphine Book. With each song she composed, Elysia unlocked hidden stories and secrets within the pages. The melodies resonated throughout the realm, enchanting listeners and bringing them together in joyous celebration. Yet, she soon discovered that not all stories were meant to be sung; some held sorrow that needed to be respected, leading her on a journey of emotional exploration.",
            "The Xenoraphine Book became a living entity, absorbing the thoughts and emotions of those who read it. It began to interact with readers, guiding them through their own stories and helping them confront their fears and aspirations. As individuals shared their experiences, the book grew richer, becoming a collective memoir of the realm\'s inhabitants. It transformed into a symbol of unity, reminding everyone that their stories, no matter how small, contributed to the greater narrative of Xenoraphine."
        ],
        "Monster": [
            "In the heart of the Abyssal Woods, where sunlight barely penetrated the thick canopy of twisted trees, a tribe of shadowy monsters thrived. These creatures, known as the Umbral, were guardians of ancient secrets hidden within the forest. Legends spoke of a cursed artifact that granted immense power to its wielder, but at a terrible cost. As explorers ventured into the woods, they were drawn deeper by whispers of the artifact, unaware that the Umbral would protect their domain at all costs.",
            "The Whispering Caves, a labyrinthine network beneath the mountains, served as the home of the eerie Echo Beasts. These monsters communicated through haunting echoes that could confuse even the most seasoned adventurers. One day, a daring hero entered the caves seeking fame, but the deeper he delved, the more he lost his sense of direction. As the echoes grew louder, the Echo Beasts began to play with his mind, blurring the line between reality and illusion. It became a race against time to escape before he was consumed by the darkness.",
            "Nestled in the Frozen Wastes, the Frost Titans ruled the desolate landscape with an icy grip. These colossal creatures fed on the despair of lost travelers, drawing strength from their fears. When a group of wanderers stumbled into their domain, they found themselves battling not only the physical might of the Titans but also their own inner demons. As the harsh blizzards raged, alliances formed and shattered, leading to a gripping tale of survival amidst the frozen horrors.",
            "The Swamp of Sorrows, filled with murky waters and grotesque flora, was the breeding ground for the Sludge Monsters. Each night, they emerged from the depths, searching for lost souls to drag into their realm. A local villager, driven by grief after losing a loved one to the swamp, decided to venture into the depths to uncover the truth behind the Sludge Monsters. What she discovered was a web of sorrow that connected the monsters to the town, and she had to decide whether to confront the darkness or succumb to it herself.",
            "In the desolate Ruins of Eldara, a place once vibrant with life, the Bone Golems now roamed. These towering creatures, constructed from the remnants of fallen warriors, held the memories of their past lives. A curious archaeologist set out to study the ruins but inadvertently awakened the Bone Golems. As they relived their final battles, the archaeologist had to navigate their haunting memories while uncovering the truth behind the tragedy that befell Eldara. The lines between monster and man blurred as history came alive.",
            "Deep in the Enchanted Marsh, the Spirit Wraiths floated silently, drawing in unsuspecting travelers with their ethereal beauty. Legends claimed they were once guardians of the forest, transformed by betrayal. When a young ranger sought to restore balance, she had to confront her own betrayal from the past. As she journeyed deeper into the marsh, she learned that the Spirit Wraiths could show her not only her mistakes but also the path to redemption, culminating in a poignant battle between hope and despair.",
            "The Mountain of Whispers was home to the elusive Shadow Serpents, creatures that could blend seamlessly into their surroundings. These monsters were feared for their ability to steal memories, leaving victims lost and hollow. When a brave warrior sought to reclaim his stolen memories, he ventured into the mountain, confronting the serpents in a gripping tale of identity and the power of remembrance. Each encounter forced him to relive his past, leading to revelations that would change him forever.",
            "The Gloomy Abyss, a bottomless chasm shrouded in darkness, was inhabited by the Nightmares, monstrous entities that feasted on fear itself. A courageous child from a nearby village, plagued by nightmares, ventured into the abyss seeking answers. Along the way, she encountered manifestations of her deepest fears, each more terrifying than the last. As she faced them one by one, she discovered that the true monster was not the Nightmares, but the fears that resided within her own heart.",
            "In the Valley of Lost Souls, where the fog hung thick and memories faded, the Phantom Beasts roamed freely. These creatures were said to be the remnants of those who had perished without closure. A grieving widow set out to find her late husband, believing he had become one of the Phantoms. As she journeyed through the valley, she encountered the memories of those who had lost their way, ultimately leading to a heartfelt confrontation that would either set them free or doom them to wander forever.",
            "The Lava Pits, a treacherous landscape of molten rock, served as the lair of the Fire Drakes. These fearsome monsters were born from the fury of the earth itself, each one a manifestation of nature's wrath. A reckless treasure hunter sought the rumored Heart of Flame, said to grant unimaginable power. However, as he delved into the pits, he soon realized that the true power lay in understanding the balance of nature, leading to a thrilling escape that would test his courage and cunning."
        ],
        "Medal": [
            "In the ancient city of Eldoria, a legendary blacksmith named Theron toiled day and night. His goal was to create a medal that could grant its wearer unmatched courage. After years of experimenting with rare metals and enchanting gems, he discovered a hidden forge deep within the mountain. It was said to be blessed by the gods. With each strike of his hammer, the forge emitted a radiant glow, infusing the medal with divine energy. However, as the final touches were made, dark forces sought to steal his creation, leading to an epic battle that would test Theron\'s resolve and creativity.",
            "The sorceress Lyria was known for her mastery of ancient magic. She believed that medals could harness the power of the elements. One fateful night, during a lunar eclipse, she gathered the essences of fire, water, earth, and air. With her incantations echoing through the night, she forged a medal that could control storms. But the power within was volatile. When a rival sorcerer learned of her creation, he unleashed chaos in an attempt to claim it for himself. The ensuing battle between Lyria and her adversary would determine not only the fate of her medal but also the balance of nature itself.",
            "In the depths of the Whispering Forest, an enigmatic alchemist named Eldrin was said to possess knowledge of life and death. Driven by a desire to create a medal that could revive the fallen, he ventured into the Shadow Realm to gather rare ingredients. The journey was fraught with dangers, including encounters with malevolent spirits. As he combined the elements in his hidden laboratory, he accidentally awakened an ancient curse. Eldrin now had to face the very spirits he had hoped to manipulate, leading to a heart-pounding tale of redemption and sacrifice.",
            "The skilled artisan Nira was renowned for her intricate designs. One day, she stumbled upon a forgotten book of ancient techniques that promised to create a medal infused with the power of dreams. Intrigued, she began her work, but the more she crafted, the more she became trapped in a web of her own nightmares. With each medal she created, fragments of her fears seeped into reality. Nira had to confront her deepest anxieties to break free and finish the medal, resulting in a thrilling journey of self-discovery and empowerment.",
            "A wandering bard named Kael believed that music held the key to the heart and soul. He sought to create a medal that could amplify the emotions of its wearer. Traveling from town to town, Kael collected melodies and harmonies, crafting the perfect composition. However, an envious rival sought to silence him, believing that music should be a weapon, not a gift. The bard's quest turned into a symphony of duels and melodies, where he had to prove that music could unite rather than divide, leading to a climactic performance that would change everything.",
            "In the skies above, a visionary inventor named Selene dreamed of crafting a medal that could grant the ability to fly. Using her knowledge of engineering and magic, she designed intricate mechanisms and enchantments. However, as she tested her creation, a tragic malfunction sent her spiraling down to the ground. Determined to rise again, Selene embarked on a journey to gather lost blueprints from legendary inventors. Her quest was filled with peril, but each challenge brought her closer to the ultimate design, culminating in a breathtaking aerial showdown against those who doubted her dreams.",
            "Deep in the volcanic region, a reclusive mage named Korrin sought to harness the power of magma to create a medal of strength. After enduring trials of fire and heat, he successfully forged the medal, but its power came with a price. As word spread, warriors from far and wide flocked to claim the medal for themselves, unaware that it would awaken the fury of the volcano. Korrin had to protect his creation from those who wished to exploit it while grappling with the consequences of his ambition, leading to a dramatic confrontation between nature and ambition.",
            "The wise sage Elara believed that every medal should tell a story. She set out on a journey to gather tales from different cultures and weave them into her designs. However, as she traveled, she discovered that not all stories were meant to be told. A cursed tale threatened to consume her, and she had to unravel the mystery behind it before it was too late. With the help of unlikely allies, Elara embarked on a race against time, navigating through treacherous landscapes to save herself and the tales she cherished.",
            "The famed warrior and smith, Brax, sought to create a medal that would symbolize unity among the warring clans of his homeland. He envisioned a design that merged the emblems of each clan into one harmonious piece. However, his endeavor was met with skepticism and hostility. As tensions rose, Brax organized a tournament to prove the strength of unity. With each battle fought, the medal took on new meaning, ultimately leading to a heart-stirring moment where the clans had to choose between vengeance and solidarity.",
            "The inventor Asher, obsessed with the mechanics of time, aimed to create a medal that could manipulate time itself. Through relentless experimentation, he created a device that could momentarily freeze time. But the consequences were dire; he soon realized that tampering with time attracted the attention of a powerful timekeeper. Asher found himself embroiled in a dangerous game, racing against the clock to protect his invention from those who would use it for destruction. The final showdown tested not only his ingenuity but also his understanding of time\'s true nature."
        ],
        "Border": [
            "In the realm of Eldoria, an ancient architect named Alaric dedicated his life to constructing a great wall to protect his people from encroaching darkness. He poured every ounce of his spirit into the stone, believing that the stronger the wall, the safer his city would be. However, as the final stone was set, he felt a part of his life force drain away. In the end, the wall stood tall, but Alaric was left a shadow of his former self, watching over his creation with a bittersweet sense of fulfillment, knowing he had given his essence to protect his home.",
            "The sorceress Morgana sought to create a magical barrier to shield her village from malevolent spirits that roamed the night. In her quest, she discovered an ancient ritual that required the sacrifice of one's own vitality. Undeterred, she chanted the incantation, feeling the warmth of her life ebb away. As the shimmering border materialized, it glowed brightly, banishing the spirits. Yet, Morgana was forever changed, becoming a guardian bound to the barrier, sacrificing her freedom for the safety of her people.",
            "The famed warrior Korrin, known for his bravery, embarked on a quest to create a border that would define the territory of his clan. He forged a pact with ancient spirits, promising his strength and life in exchange for their protection. As the border materialized, Korrin felt his life force being siphoned away. When the last boundary was drawn, he collapsed, but the border became a legendary symbol of his clan's resilience, immortalizing Korrin’s sacrifice in their history.",
            "Elowen, a master druid, sought to create a living border using the very essence of nature. To do this, she had to offer her own lifeblood to awaken the ancient trees that would form the border. With each drop of blood, she felt the connection to the forest deepen, but also sensed her vitality fading. As the trees grew tall and protective, Elowen transformed into a spirit of the woods, forever intertwined with the boundary she had created, watching over nature with unwavering devotion.",
            "The architect Renna envisioned a grand fortress with fortified borders that could withstand any siege. To achieve her dream, she sought the help of an ancient entity who demanded a heavy price. With each brick laid, Renna felt her life force being consumed by the fortress. When the last gate was sealed, the fortress stood impregnable, but Renna faded into legend, her spirit forever bound to the walls she had built to safeguard her people.",
            "A reclusive alchemist named Varyn aimed to create a mystical border to separate the realms of magic and mundane. He sacrificed his physical form, infusing his essence into the border itself. As the boundary shimmered into existence, Varyn became a specter, guarding the line between worlds. Those who dared to cross felt his presence, and stories of the alchemist's sacrifice became whispers of warning among those who sought power beyond the veil.",
            "The warrior-poet Lyra sought to create a border that would not only protect her people but inspire them through song. She infused her melodies into the very fabric of the land, each note a boundary of hope. However, the power required took a toll on her spirit. As she sang the final note, she felt her essence intertwine with the land, transforming her into a legend whose songs would echo through the ages, giving strength to those who heard them.",
            "An old sage named Eldrin was tasked with creating a border to protect the sacred sites of magic from corruption. He drew upon ancient texts, binding his lifeforce to the spells inscribed within. Each incantation required a part of him, and as he completed the final spell, Eldrin vanished, leaving behind a shimmering barrier that pulsed with protective energy. The border stood firm, but his name became a solemn reminder of the price paid for the safety of their sacred grounds.",
            "The mysterious shadow weaver Seraphis aimed to craft a border that would cloak the hidden realm of dreams from nightmares. In a dark ritual, he offered his shadow to the void, weaving it into the fabric of the dream world. As the border solidified, Seraphis felt the darkness consuming him. Though the nightmares were kept at bay, he became a part of the shadows he created, forever watching over the realm he had sacrificed everything to protect.",
            " In the depths of the frozen north, the ice mage Kaelan sought to create a border of eternal winter to keep out those who threatened his land. He summoned the ice spirits, bartering his warmth for their power. With each frost that formed, Kaelan felt his warmth drain away until he was nothing but a husk of ice and magic. The border of winter stood tall, a testament to his sacrifice, while Kaelan became a spirit of frost, guarding the boundary for eternity."
        ],
        "Achievement": [
            "In the realm of Valoria, a noble knight named Seraphis embarked on a quest to defeat the Dark Dragon, a beast that had terrorized the land for centuries. Knowing that this would require more than mere strength, he sought the wisdom of the ancient seer who warned him that achieving glory would come at a price. With each dragon slain, Seraphis felt a piece of his soul fade. Upon defeating the creature, he became a legend, but his spirit was forever bound to the dragon's lair, a guardian of the achievement he had sacrificed so much to attain.",
            "The mage Elara sought to master the arcane arts, aiming to create a spell that would alter time itself. She poured her very essence into the spellbook, each incantation drawing from her life force. As she completed the final spell, time shifted around her, but Elara vanished into the fabric of reality. The spell was perfected, granting her the title of the Timeless Sorceress, but she was lost to the ages, her achievement echoing in the whispers of magic.",
            "In a distant village, a humble blacksmith named Thalion desired to forge the strongest sword in existence. To do this, he made a pact with the Fire Elementals, offering his vitality as the price for their flames. As he hammered the metal, he felt his strength wane, but the blade grew more powerful. When he completed the sword, it became a legend known as Flameheart, but Thalion was left a frail old man, his life essence forever entwined with the weapon he created.",
            "The healer Lyra sought to develop a potion that could cure any ailment. She ventured into the forbidden forest to gather rare ingredients, sacrificing her health and well-being. Each concoction required her vitality, draining her lifeforce little by little. When she finally perfected the potion, she was celebrated as the Grand Alchemist, but she became a frail shadow of herself, her achievements overshadowed by the cost of her extraordinary skill.",
            "The architect Rion aimed to build the tallest tower in the kingdom, a symbol of hope and perseverance. To do so, he called upon the spirits of the wind, pledging his energy in exchange for their strength. As he worked, he felt his life force diminish with every brick laid. When the tower reached its pinnacle, it stood as a marvel of engineering, but Rion faded into obscurity, his spirit forever entwined with the very structure he had sacrificed everything to create.",
            "A bard named Caelum dreamed of composing a song that would unite all realms. He traveled far and wide, collecting melodies from different cultures, each note costing him a fragment of his memory. As he finally crafted the perfect song, he realized he had forgotten his own past. The song became a timeless anthem, but Caelum was left as a stranger in his own mind, his achievement resonating while he wandered lost in a sea of forgotten melodies.",
            "The warrior Aeloria sought to create an impenetrable shield to protect her people. She delved deep into the ancient arts of protection, each spell requiring a piece of her spirit. When she finally forged the shield, it glowed with magical energy, warding off all harm. However, Aeloria found herself unable to wield it, having given too much of herself. She became a sentinel of the shield, forever watching over her people but unable to join them in their battles.",
            "The scholar Isolde aspired to write a tome of knowledge that could enlighten generations. She locked herself in her study, pouring her intellect and passion into every page. The more she wrote, the more she felt her mind fracturing. Upon completing the tome, it became a revered masterpiece, but Isolde lost her sanity, becoming a ghostly figure, forever haunted by the brilliance of her own creation.",
            "The visionary artist Aurel sought to paint a mural that would capture the essence of life itself. To achieve this, he sacrificed his emotions, channeling them into each stroke. As the mural came to life, Aurel became an empty shell, devoid of feeling. The mural stood as a testament to his genius, but Aurel wandered through life, a silent observer of the very beauty he had once captured with such passion.",
            "The oracle Kael wished to create a prophecy that would guide his people to prosperity. He ventured into the depths of his soul, each vision costing him a piece of his destiny. When the prophecy was unveiled, it brought hope and fortune, yet Kael was left blind to his own future, forever a prisoner of his own foresight, his achievement illuminating paths for others while leaving him in darkness."
        ],
        "Title": [
            "In the ancient kingdom of Eldoria, a humble scribe named Elowen sought to document the greatest achievements of her time. She believed that true greatness should be recognized through titles that reflect the valor and wisdom of individuals. To do this, she traveled across the realm, collecting stories and experiences. With each tale she recorded, Elowen felt a weight upon her soul, as if the burden of history was claiming her spirit. Eventually, she created the 'Title of the Unyielding,' which honored those who stood against tyranny. Though she became revered as the historian of Eldoria, her own story faded into obscurity, a mere footnote in the annals of time.",
            "A fierce warrior named Thorne was driven to earn the title 'Champion of the Realm.' He trained tirelessly, facing countless foes in battle. Each victory granted him glory, but with every clash, he felt a piece of his humanity slip away. Thorne's relentless pursuit of honor consumed him, leading him to challenge the fiercest beasts and enemies. In a climactic battle against a legendary dragon, he emerged victorious, earning his title. Yet, as he held the trophy of his triumph, he realized he had become a shell of his former self, a warrior without a home or purpose, forever haunted by the price of his glory.",
            "The enchantress Seraphina sought to create a title that would inspire hope among her people. She delved into ancient magic, weaving spells to forge the 'Title of the Luminary.' However, each incantation required a sacrifice of her joy and light. As she crafted the title, darkness seeped into her heart. When she finally revealed the title, her people were uplifted, but Seraphina was left shrouded in shadows, her once-vibrant spirit diminished to a flicker of what it once was.",
            "In the land of Arcania, a brilliant scholar named Lysander wished to recognize intellectual achievements with the title 'Master of Knowledge.' He poured his life into his studies, sacrificing relationships and his health in pursuit of wisdom. When he completed his grand compendium, it became a cornerstone of learning. However, as he presented it to the world, he realized he could no longer engage with others, trapped in a world of intellect while his humanity withered away, leaving him an isolated genius.",
            "The bard Callista desired to create the 'Title of the Muse,' honoring those who inspired creativity and passion. She traveled from city to city, collecting stories and songs, giving her heart and soul to every performance. The more she sang, the more she felt her essence intertwining with her music. When she finally established the title, it resonated through generations, but Callista became lost in her melodies, her own voice drowned out by the echoes of inspiration she had unleashed.",
            "A valiant knight named Roderick sought to earn the title 'Guardian of the Realm' by protecting his homeland from invaders. He faced insurmountable odds, often placing himself in peril to save others. Each battle etched scars upon his body and soul, marking his journey. When he finally earned the title, it was celebrated across the kingdom, but Roderick found himself a haunted figure, the weight of his sacrifices leaving him longing for peace that would never come.",
            "The visionary architect Alaric aimed to create the title 'Master Builder,' recognizing those who shaped the landscapes of their cities. He poured years into designing an architectural marvel, pushing himself to exhaustion. As he constructed the masterpiece, he felt his health deteriorate, his dreams becoming a double-edged sword. When the building was unveiled, it stood tall and proud, yet Alaric was left bedridden, his achievement a bittersweet reminder of the life he sacrificed to create beauty.",
            "The healer Amara sought to bestow the title 'Savior of the Sick' upon those who selflessly cared for others. She dedicated her life to helping the ill, but in doing so, she neglected her own health. Each patient saved cost her a fragment of her vitality. When she finally announced the title, it became a beacon of hope, yet Amara found herself fading, a martyr of compassion, forever enshrined but never truly appreciated in her own right.",
            "The cunning rogue Vesper dreamed of earning the title 'Shadow of the Night,' honoring those who excelled in stealth and subterfuge. He honed his skills, sacrificing friendships and trust as he navigated the underbelly of society. When he finally earned the title, it came with a notorious reputation. Vesper became a ghost in the shadows, respected yet feared, unable to find solace or companionship, his triumph isolating him from the very world he once loved.",
            "The revered elder Sage Orion wished to create the title 'Wisdom of the Ages,' celebrating those who imparted knowledge across generations. He spent years teaching and sharing, sacrificing his own desires for the sake of his students. When the title was finally bestowed, it became a cherished legacy. However, Sage Orion found himself forgotten, overshadowed by the very wisdom he had imparted, living in the shadows of his own creation, a quiet guardian of knowledge without recognition."
        ],
        "Collaboration":[
            "Collaboration across anime worlds is a fascinating concept that ignites the imagination of fans everywhere. Imagine a vibrant tapestry where characters from diverse universes unite for epic adventures, sharing their unique abilities and philosophies. In one thrilling scenario, heroes like Naruto and Luffy join forces with the magical warriors of Fairy Tail to confront an ancient evil threatening the multiverse. Their distinct combat styles—Naruto\'s ninjutsu, Luffy\'s Gum-Gum powers, and Natsu\'s fire magic—create dynamic battles that showcase teamwork in the face of overwhelming odds."
        ],
        "CollborationEquipment":[
            "In the realm of anime collaborations, equipment becomes a crucial aspect that empowers characters to harness their unique abilities in dynamic gameplay. Imagine a game where iconic heroes from various anime universes equip themselves with specially designed gear that enhances their powers. For instance, Naruto might wield a kunai infused with chakra, allowing him to unleash powerful Rasengan attacks, while Luffy could don a pair of gloves that amplify his Gum-Gum abilities, enabling him to stretch further and strike harder. This collaboration equipment not only showcases each character\'s strengths but also introduces new tactical elements to the game. Characters like Goku could equip a legendary armor that boosts his energy levels, allowing him to tap into Ultra Instinct form more easily. Meanwhile, characters from magical worlds, like the wizards of Fairy Tail, could use enchanted staffs that channel their spells with greater potency. The synergy between characters also plays a vital role. When heroes like Edward Elric and Mikasa Ackerman combine their gear—perhaps a suit that enhances strength while providing alchemical boosts—they can create devastating combo attacks that blend their abilities. This not only enhances the gameplay but also emphasizes the importance of teamwork and strategy. As players traverse this vibrant anime universe, they can collect and upgrade collaboration equipment, unlocking new abilities and enhancing their favorite characters. This blending of powers and styles creates a rich and engaging experience, allowing fans to immerse themselves in the thrilling world of anime like never before."
        ],
        "Military":[
            "In a thrilling twist of fate, warriors from different dimensions and timelines are summoned to a world on the brink of chaos, each bringing their unique powers and abilities. This military coalition consists of divine heroes and fearsome demon lords, creating an unparalleled assembly of strength and strategy. Imagine a radiant angelic knight, wielding a celestial sword that cleaves through darkness, standing shoulder to shoulder with a cunning sorceress from a realm of shadows, her dark magic capable of bending the very fabric of reality. As these combatants unite, they form a formidable army poised to combat an impending evil threatening their newfound home. Characters from ancient mythologies, like a legendary Spartan or a fierce Valkyrie, lend their unmatched combat skills and tactical expertise. Meanwhile, modern-day warriors, equipped with advanced technology and weaponry, provide a stark contrast, utilizing precision and strategy to outmaneuver their foes. The game unfolds as players navigate a richly detailed world, engaging in epic battles that require careful coordination and teamwork. Each warrior\'s abilities can be enhanced through synergies; for instance, the divine knight\'s shield might bolster the sorceress\'s dark spells, creating devastating area effects. This collaboration not only showcases the diversity of their powers but also emphasizes the necessity of unity in the face of overwhelming odds. As the story progresses, players uncover ancient secrets and forge alliances, ultimately determining the fate of this world. Will they conquer the darkness together, or will the forces of chaos prevail? The blend of divine and demonic powers creates an exhilarating gameplay experience, where every decision counts, and every battle shapes the destiny of their collective existence."
        ],
        "Domanus":[
            "Story Domanus 1",
            "Story Domanus 2",
            "Story Domanus 3",
            "Story Domanus 4",
            "Story Domanus 5",
            "Story Domanus 6",
            "Story Domanus 7",
            "Story Domanus 8",
            "Story Domanus 9",
            "Story Domanus 10"
        ],
        "Domanus":[
            "Story Domanus 1",
            "Story Domanus 2",
            "Story Domanus 3",
            "Story Domanus 4",
            "Story Domanus 5",
            "Story Domanus 6",
            "Story Domanus 7",
            "Story Domanus 8",
            "Story Domanus 9",
            "Story Domanus 10"
        ],
    }
    if character in stories:
        return random.choice(stories[character])
#Generate database
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
                        story = get_story(current_name)
                        
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into cards values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")

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
                        story = get_story(current_name)
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into cards values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                        story = get_story(current_name)
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into cards values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                        story = get_story(current_name)
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into cards values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                    story = get_story(dir_name)
                
                    power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                    print("insert into books values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + dir_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story+"');")
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
                    story = get_story(dir_name)
                    
                    power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                    print("insert into army values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + dir_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                        story=get_story("CollborationEquipment")
                        name=name.encode('latin1', 'ignore').decode('latin1')
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")

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
                        story=get_story("CollborationEquipment")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                        story=get_story("CollborationEquipment")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                        story=get_story("CollborationEquipment")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                        story=get_story("CollborationEquipment")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into collaboration_equipments values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                story=get_story("Medal")
                
                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into medals values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'"+ story +"');")

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
                story=get_story("Achievement")
                
                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into achievements values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'"+story+"');")
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
                story=get_story("Title")

                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into titles values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'"+story+"');")
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
                story=get_story("Monster")

                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into monsters values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + "none" + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
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
                story=get_story("Border")
            
                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into borders values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'"+story+"');")
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
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + dir_name + "','" + current_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
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
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + dir_name + "','" + current_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
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
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + dir_name + "','" + current_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
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
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + dir_name + "','" + current_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
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
                            print("insert into equipments values (" + str(id) + ",'" + name + "','" + path + "','" + dir_name + "','" + current_name + "','"+set1_folder_name +"'," + str(0) + "," + str(power) + "," + str(health) +
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
                story=get_story("Collaboration")
            
                power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                print("insert into collaborations values (" + str(id) + ",'" + name + "','" + path + "'," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ str(per_health)+","+str(per_physical_attack) +","+ str(per_physical_defense)
                              + ","+str(per_magical_attack) +","+ str(per_magical_defense) + ","+str(per_chemical_attack) +","+ str(per_chemical_defense) + ","+str(per_atomic_attack) +","+ str(per_atomic_defense) + ","+str(per_mental_attack) +","+ str(per_mental_defense)+",'"+ story +"');")
                id=id+1      

def create_military_database():
    cards_dir="Military"
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
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="SR"
    clan=""
    price=100000
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            possible_values = [1.1, 1.2, 1.3, 1.4, 1.5]
            NumberRandom=random.choice(possible_values)
            if "SR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        story=get_story("Military")
                        
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into military values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")

                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        health=math.ceil(2000000*NumberRandom)
                        physical_attack=math.ceil(200000*NumberRandom)
                        physical_defense=math.ceil(200000*NumberRandom)
                        magical_attack=math.ceil(200000*NumberRandom)
                        magical_defense=math.ceil(200000*NumberRandom)
                        chemical_attack=math.ceil(200000*NumberRandom)
                        chemical_defense=math.ceil(200000*NumberRandom)
                        atomic_attack=math.ceil(200000*NumberRandom)
                        atomic_defense=math.ceil(200000*NumberRandom)
                        mental_attack=math.ceil(200000*NumberRandom)
                        mental_defense=math.ceil(200000*NumberRandom)
                        mana=200
                        rare="SSR"
                        if "Evolved" in name:
                            health=health*2
                            physical_attack=physical_attack*2
                            physical_defense=physical_defense*2
                            magical_attack=magical_attack*2
                            magical_defense=magical_defense*2
                            chemical_attack=chemical_attack*2
                            chemical_defense=chemical_defense*2
                            atomic_attack=atomic_attack*2
                            atomic_defense=atomic_defense*2
                            mental_attack=mental_attack*2
                            mental_defense=mental_defense*2

                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        story=get_story("Military")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into military values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name,extension=os.path.splitext(file_name)
                        health=math.ceil(5000000*NumberRandom)
                        physical_attack=math.ceil(500000*NumberRandom)
                        physical_defense=math.ceil(500000*NumberRandom)
                        magical_attack=math.ceil(500000*NumberRandom)
                        magical_defense=math.ceil(500000*NumberRandom)
                        chemical_attack=math.ceil(500000*NumberRandom)
                        chemical_defense=math.ceil(500000*NumberRandom)
                        atomic_attack=math.ceil(500000*NumberRandom)
                        atomic_defense=math.ceil(500000*NumberRandom)
                        mental_attack=math.ceil(500000*NumberRandom)
                        mental_defense=math.ceil(500000*NumberRandom)
                        mana=500
                        rare="UR"
                        if "Evolved" in name:
                            health=health*2
                            physical_attack=physical_attack*2
                            physical_defense=physical_defense*2
                            magical_attack=magical_attack*2
                            magical_defense=magical_defense*2
                            chemical_attack=chemical_attack*2
                            chemical_defense=chemical_defense*2
                            atomic_attack=atomic_attack*2
                            atomic_defense=atomic_defense*2
                            mental_attack=mental_attack*2
                            mental_defense=mental_defense*2

                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        story=get_story("Military")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into military values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        health=math.ceil(10000000*NumberRandom)
                        physical_attack=math.ceil(1000000*NumberRandom)
                        physical_defense=math.ceil(1000000*NumberRandom)
                        magical_attack=math.ceil(1000000*NumberRandom)
                        magical_defense=math.ceil(1000000*NumberRandom)
                        chemical_attack=math.ceil(1000000*NumberRandom)
                        chemical_defense=math.ceil(1000000*NumberRandom)
                        atomic_attack=math.ceil(1000000*NumberRandom)
                        atomic_defense=math.ceil(1000000*NumberRandom)
                        mental_attack=math.ceil(1000000*NumberRandom)
                        mental_defense=math.ceil(1000000*NumberRandom)
                        mana=1000
                        rare="LG"
                        if "Evolved" in name:
                            health=health*2
                            physical_attack=physical_attack*2
                            physical_defense=physical_defense*2
                            magical_attack=magical_attack*2
                            magical_defense=magical_defense*2
                            chemical_attack=chemical_attack*2
                            chemical_defense=chemical_defense*2
                            atomic_attack=atomic_attack*2
                            atomic_defense=atomic_defense*2
                            mental_attack=mental_attack*2
                            mental_defense=mental_defense*2 

                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        story=get_story("Military")
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into military values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'"+ story +"');")
                        id=id+1

def create_spell_database():
    cards_dir="Spell"
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
    critical_damage=0
    armor_penetration=0
    avoid=0
    absorbs_damage=0
    regenerate_vitality=0
    mana=100
    rare="SR"
    clan=""
    price=100000
    path=""
    for root, dirs, files in os.walk(cards_dir):
        current_dir=os.path.basename(root)
        current_name=""
        if current_dir not in ["LG", "UR", "SSR", "SR"]:
            current_name=current_dir
            # print(current_name)
        for dir_name in dirs:
            possible_values = [1.1, 1.2, 1.3, 1.4, 1.5]
            NumberRandom=random.choice(possible_values)
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
                        print("insert into spell values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ",'');")

                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        health=math.ceil(100*NumberRandom)
                        physical_attack=math.ceil(100*NumberRandom)
                        physical_defense=math.ceil(100*NumberRandom)
                        magical_attack=math.ceil(100*NumberRandom)
                        magical_defense=math.ceil(100*NumberRandom)
                        chemical_attack=math.ceil(100*NumberRandom)
                        chemical_defense=math.ceil(100*NumberRandom)
                        atomic_attack=math.ceil(100*NumberRandom)
                        atomic_defense=math.ceil(100*NumberRandom)
                        mental_attack=math.ceil(100*NumberRandom)
                        mental_defense=math.ceil(100*NumberRandom)
                        mana=1000
                        rare="LG"
                        price=5000000
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        description=""
                        if "Evironment" in current_name:
                            health=5000
                            physical_attack=5000
                            physical_defense=5000
                            magical_attack=5000
                            magical_defense=5000
                            chemical_attack=5000
                            chemical_defense=5000
                            atomic_attack=5000
                            atomic_defense=5000
                            mental_attack=5000
                            mental_defense=5000
                            description="'Increase 5000% for all military'"
                        elif "Increase" in current_name:
                            description="'Increase "+ str(health) +"% for all your military'"
                        elif "Decrease" in current_name:
                            description="'Decrease "+ str(health) +"% for all enemy military'"
                        power=calculate_power(health,physical_attack,physical_defense,magical_attack,magical_defense,chemical_attack,chemical_defense,atomic_attack,atomic_defense,mental_attack,mental_defense,
                                              speed,critical_rate,critical_damage,armor_penetration,avoid,absorbs_damage,regenerate_vitality)
                        print("insert into spell values (" + str(id) + ",'" + name + "','" + path + "','" + rare + "','" + current_name + "'," + str(0) + "," + str(power) + "," + str(health) + "," 
                              + str(physical_attack) + "," + str(physical_defense) + "," + str(magical_attack) + "," + str(magical_defense) + "," + str(chemical_attack) + "," + str(chemical_defense) 
                              + "," + str(atomic_attack) + "," + str(atomic_defense) + "," + str(mental_attack) + "," + str(mental_defense) + "," + str(speed) + "," + str(critical_damage) + "," + str(critical_rate) + "," + str(armor_penetration) 
                              + "," + str(avoid) + "," + str(absorbs_damage) + "," + str(regenerate_vitality) + "," + str(mana) + ","+ description +");")
                        id=id+1

#Generate Trading

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

def create_military_trade():
    cards_dir="Military"
    id=1
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
                        print("insert into military_trade values (" + str(id) + "," + str(23) + "," + str(500000) + ");")
                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into military_trade values (" + str(id) + "," + str(23) + "," + str(5000000) + ");")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into military_trade values (" + str(id) + "," + str(23) + "," + str(5000000) + ");")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into military_trade values (" + str(id) + "," + str(23) + "," + str(50000000) + ");")
                        id=id+1

def create_spell_trade():
    cards_dir="Spell"
    id=1
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
                        print("insert into spell_trade values (" + str(id) + "," + str(24) + "," + str(500000) + ");")
                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into spell_trade values (" + str(id) + "," + str(24) + "," + str(5000000) + ");")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into spell_trade values (" + str(id) + "," + str(24) + "," + str(5000000) + ");")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into spell_trade values (" + str(id) + "," + str(24) + "," + str(50000000) + ");")
                        id=id+1

#Generate chest

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

def create_chest_military():
    cards_dir="Military"
    id=1
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
                        print("insert into chest_military values (" + str(401) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into chest_military values (" + str(401) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into chest_military values (" + str(401) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into chest_military values (" + str(401) + "," + str(id) + "," + str(1) + ");")
                        id=id+1

def create_chest_spell():
    cards_dir="Spell"
    id=1
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
                        print("insert into chest_spell values (" + str(383) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
            if "SSR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into chest_spell values (" + str(383) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
            if "UR" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into chest_spell values (" + str(383) + "," + str(id) + "," + str(1) + ");")
                        id=id+1
            if "LG" in dir_name:
                current_dir =os.path.join(root,dir_name)
                for file_name in os.listdir(current_dir):
                    if file_name.endswith(".jpg") or file_name.endswith("png"):
                        name, extension=os.path.splitext(file_name)
                        path=os.path.join(current_dir,file_name)
                        path=path.replace("\\","/")
                        name=name.replace("_"," ")
                        print("insert into chest_spell values (" + str(383) + "," + str(id) + "," + str(1) + ");")
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
# create_military_database()
# create_spell_database()

#Chest book error

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
# create_military_trade()
# create_spell_trade()

# create_chest_equipment()
# create_chest_card()
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
# create_chest_military()
# create_chest_spell()
# create_chest_book()