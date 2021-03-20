from random import shuffle, randint

# instantiate the individual player lists, combined player list, and the crime_file
player1 = []
player2 = []
player3 = []
player4 = []

players = [player1, player2, player3, player4]

crime_file = []

# instantiate rooms list, weapons list, and people list
rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Hall", "Study", "Library", "Billiard Room"]
weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
people = ["Miss Scarlett", "Rev Green", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mrs. White"]

# randomly pick one of each for the crime file
scene_of_the_crime = rooms[randint(0, 8)]
murder_weapon = weapons[randint(0,5)]
murderer = people[randint(0,5)]

# update lists without crime file cards
rooms.remove(scene_of_the_crime)
weapons.remove(murder_weapon)
people.remove(murderer)
