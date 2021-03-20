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

# add cards to crime file
crime_file.append(scene_of_the_crime)
crime_file.append(murder_weapon)
crime_file.append(murderer)

# update lists without crime file cards
rooms.remove(scene_of_the_crime)
weapons.remove(murder_weapon)
people.remove(murderer)

deck_without_crime = rooms + weapons + people

shuffle(deck_without_crime)

# count up to deal the right amount of cards to each player (total 18 | 21 - 3 crime scene cards)
count = 0
while count < 5:
    player1.append(deck_without_crime[0])
    deck_without_crime.remove(deck_without_crime[0])
    count += 1
count = 0
while count < 5:
    player2.append(deck_without_crime[0])
    deck_without_crime.remove(deck_without_crime[0])
    count += 1
count = 0
#
while count < 4:
    player3.append(deck_without_crime[0])
    deck_without_crime.remove(deck_without_crime[0])
    count += 1
count = 0
while count < 4:
    player4.append(deck_without_crime[0])
    deck_without_crime.remove(deck_without_crime[0])
    count += 1

print("Player 1's hand: ", player1, "\nPlayer 2's hand: ",player2,"\nPlayer 3's hand: ", player3,"\nPlayer 4's hand: ", player4)
print("THE CRIME FILE: ", crime_file)
