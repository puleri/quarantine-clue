from random import shuffle, randint
from rich.console import Console

console = Console()

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

# print("Player 1's hand: ", player1, "\nPlayer 2's hand: ",player2,"\nPlayer 3's hand: ", player3,"\nPlayer 4's hand: ", player4)
# print("THE CRIME FILE: ", crime_file)

def main():
    console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nQuarentine Clue\n\n", style="blue")
    input("The Rules: In the dealing phase each player must write \ndown their cards on seperate pieces of paper. When asking revealing clues then \nthe whole group must allow the two parties a private showing. All applicable Clue rules still apply. \nThis is currently in Beta, so any feedback is appreciated! Keep on your toes and \nenjoy detectives!(press enter to continue...)\n\n\n\n\n\n\n\n\n\n\n\n")
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter for Player 1's hand...\n\n\n\n\n\n\n\n\n")
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHere comes your hand Player 1! Keep it a secret and press enter \nwhen you are ready to pass...\n\n\n\n\n\n\n\n\n\n")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 1 write this down! Keep your eye on the player on the top left \nof your zoom screen. They are acting suspicious.\n\nPLAYER ONE'S HAND: {player1}\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter when your records are straight.")

    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer two here comes your deal. Make sure no one else can see. \nTrust no one. Press enter to continue...\n\n\n\n\n\n\n\n\n")
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nKeep this close to your chest and press enter when you are ready to pass...\n\n\n\n\n\n\n\n\n\n")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 2 write this down! Watch out for the top right player on the call. They are shifty.\n\nPLAYER TWO'S HAND: {player2}\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter when your records are straight.")

    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter for Player 3's hand...\n\n\n\n\n\n\n\n\n")
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHere comes your hand Player 3! Keep it a secret and press enter when you are ready to pass...\n\n\n\n\n\n\n\n\n\n")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 3 write this down! Keep your eye on the player on the \nbottom left of your zoom screen. They are acting suspicious.\n\nPLAYER THREE'S HAND: {player3}\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter when your records are straight.")

    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer four here comes your deal. Make sure no one else can see. \nTrust no one. Press enter to continue...\n\n\n\n\n\n\n\n\n")
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nKeep this close to your chest and press enter when \nyou are ready to start...\n\n\n\n\n\n\n\n\n\n")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 4 write this down! Watch out for the top right player \non the call. They are shifty.\n\nPLAYER FOUR'S HAND: {player4}\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter when your records are straight.")

    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")
    input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE: {crime_file}\n\n\n\n\n\n\n\n\n\n\n\n(press enter to open/close)")

main()
