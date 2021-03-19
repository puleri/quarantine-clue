from random import shuffle, randint

player1 = []
player2 = []
player3 = []
player4 = []

players = [player1, player2, player3, player4]

crime_file = []

rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Hall", "Study", "Library", "Billiard Room"]
weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
people = ["Miss Scarlett", "Rev Green", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mrs. White"]

# randomly take one of each for the crime file
scene_of_the_crime = rooms[randint(0, 8)]
murder_weapon = weapons[randint(0,5)]
murderer = people[randint(0,5)]
