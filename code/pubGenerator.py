# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:56:53 2024

@author: k2366736
"""

# =============================================================================
# Pub name generator
# =============================================================================


import random
from colorist import magenta, blue, yellow, green

animals_list = [
    "Lion", "Eagle", "Owl", "Wolf", "Fox", "Bear", "Rabbit", "Deer", 
    "Horse", "Cow", "Pig", "Sheep", "Goat", "Chicken", "Duck", "Turkey", 
    "Peacock", "Swan", "Canary", "Trout", "Crab", "Turtle", "Frog", "Toad",
    "Snake", "Bat", "Hedgehog", "Squirrel", "Mouse", "Rat", "Hamster", "Otter",
    "Beaver", "Weasel", "Mole"
]

medieval_jobs_list = [
    "Blacksmith", "Baker", "Miller", "Carpenter", "Tailor", "Shoemaker", 
    "Weaver", "Cooper", "Tanner", "Butcher", "Fletcher", "Bowyer", "Armorer", 
    "Herald", "Chandler", "Farrier", "Bailiff", "Steward", "Reeve", 
    "Merchant", "Innkeeper", "Barber", "Apothecary", "Alchemist", "Scribe", 
    "Minstrel", "Jester", "Falconer", "Clerk", "Clergy", "Monk", "Nun", 
    "Priest", "Bishop", "Abbot", "Abbess", "Friar", "Mason", "Plumber", 
    "Gardener", "Huntsman", "Gamekeeper", "Stablemaster", "Falconer", 
    "Serf", "Vassal", "Knight", "Squire", "Lord", "Lady", "Baron", 
    "Count", "Earl", "Duke", "King", "Queen", "Page", "Herald", "Chamberlain",
    "Seneschal", "Castellan", "Yeoman", "Forester", "Wainwright", 
    "Wheelwright", "Cartwright", "Fishmonger", "Salter", "Tinker", 
    "Glazier", "Silversmith", "Goldsmith", "Cooper", "Potter", "Hatter", 
    "Spicer", "Cook", "Brewer", "Vintner", "Mercer", "Draper", "Peddler",
    "Scrivener", "Scabbardmaker", "Parchmenter", "Bookbinder", "Illuminator"
]

medieval_items_list = [
    "Sword", "Shield", "Helmet", "Armor", "Lance", "Bow", "Arrow", "Crossbow",
    "Dagger", "Axe", "Mace", "Spear", "Halberd", "Flail", "Quiver", "Gauntlet",
    "Breastplate", "Greaves", "Chainmail", "Tabard", "Tunic", "Doublet", 
    "Cloak", "Gown", "Hose", "Boots", "Sandals", "Belt", "Pouch", "Chalice", 
    "Goblet", "Tankard", "Candle", "Lantern", "Torch", "Scroll", "Manuscript", 
    "Parchment", "Quill", "Ink", "Book", "Tapestry", "Banner", "Flag", 
    "Standard", "Seal", "Ring", "Necklace", "Bracelet", "Crown", "Tiara", 
    "Scepter", "Orb", "Coin", "Purse", "Chest", "Coffer", "Key", "Lock", 
    "Hourglass", "Sundial", "Compass", "Map", "Banner", "Horn", "Lyre", 
    "Lute", "Harp", "Drum", "Fiddle", "Bagpipes", "Flute", "Clarion", 
    "Trumpet", "Organ", "Bell", "Plow", "Sickle", "Scythe", "Flail", 
    "Millstone", "Anvil", "Hammer", "Tongs", "Bellows", "Chisel", "File", 
    "Saw", "Adze", "Auger", "Wedge", "Basket", "Crate", "Barrel", 
    "Cask", "Keg", "Jar", "Jug", "Pot", "Pan", "Cauldron", "Skillet", 
    "Spit", "Ladle", "Spoon", "Fork", "Knife", "Pitcher", "Ewer", "Bowl", 
    "Plate", "Platter", "Napkin", "Towel", "Cloth", "Blanket", "Quilt", 
    "Curtain", "Rug", "Mat", "Pillow", "Cushion"
]

pub_adjectives_list = [
    "Cozy", "Charming", "Lively", "Bustling", 
    "Inviting", "Welcoming", "Friendly", "Intimate", "Warm",
    "Vibrant", "Snug", 
    "Comfortable", "Elegant", "Sophisticated", "Cheerful", 
    "Festive", "Stylish", "Relaxed", "Homely", "Hearty", "Pleasant",
    "Genteel", "Rustic", "Vintage", "Artistic",
    "Upbeat", "Radiant", "Eclectic", 
    "Sunny", "Mellow", "Luminous", "Alluring", "Magnetic", 
    "Welcoming", "Engaging", "Delightful", "Brisk", "Cheery", "Gracious", 
    "Whimsical", "Playful", "Sprightly", 
    "Dapper", "Elegant", "Grand", "Majestic",
    "Enchanting"
]

body_parts_list = [
    "Head", "Face", "Forehead", "Eyebrow", "Eye",
    "Eyelash", "Nose","Cheek", "Ear", "Lip",
    "Tooth", "Tongue", "Chin", "Jaw", "Neck", "Throat", "Shoulder", "Arm",
    "Elbow", "Wrist", "Hand", "Palm", "Finger", "Thumb", "Knuckle",
    "Nail", "Chest", "Breast", "Stomach", "Waist", "Hip", "Back",
    "Spine", "Leg", "Thigh", "Knee", "Calf",
    "Ankle", "Foot", "Heel", "Toe", "Skull",
    "Brain", "Temple", "Collarbone", "Rib", "Heart",
    "Lung", "Liver", "Kidney", "Spleen", "Vein", "Tendon",
    "Bone", "Nerve", "Pupil"
]

pub1 = "The {}'s {}"
pub2 = "The {} and the {}"
pub3 = "The {} {}"
pub4 = "The {} and {}"


while True:
    input('Press enter to generate a pub...')
    r = random.randint(0,3)
    if r == 0:
        magenta("\033[1m" + pub1.format(random.choice(animals_list+medieval_jobs_list),random.choice(body_parts_list+medieval_items_list)) + "\033[0m")
    elif r == 1:
        blue('\033[1m' + pub2.format(random.choice(animals_list+medieval_jobs_list+medieval_items_list),random.choice(animals_list+medieval_jobs_list)) + "\033[0m")
    elif r == 2:
        yellow('\033[1m' + pub3.format(random.choice(pub_adjectives_list),random.choice(medieval_items_list)) + "\033[0m")
    elif r == 3:
        green('\033[1m' + pub4.format(random.choice(animals_list+medieval_jobs_list+medieval_items_list),random.choice(medieval_items_list)) + "\033[0m")
        
    
