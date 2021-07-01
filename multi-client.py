from random import shuffle, randint
import keyboard
from rich.console import Console
from client import main

from six_player import six_player
from five_player import five_player
from four_player import four_player
from three_player import three_player

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



def multi():
    console.print("""\n\n\n\n\n\n\n\n\n\n\n\n\n
 _______  __   __  _______  ______    _______  __    _  _______  ___   __    _  _______
|       ||  | |  ||   _   ||    _ |  |   _   ||  |  | ||       ||   | |  |  | ||       |
|   _   ||  | |  ||  |_|  ||   | ||  |  |_|  ||   |_| ||_     _||   | |   |_| ||    ___|
|  | |  ||  |_|  ||       ||   |_||_ |       ||       |  |   |  |   | |       ||   |___
|  |_|  ||       ||       ||    __  ||       ||  _    |  |   |  |   | |  _    ||    ___|
|      | |       ||   _   ||   |  | ||   _   || | |   |  |   |  |   | | | |   ||   |___
|____||_||_______||__| |__||___|  |_||__| |__||_|  |__|  |___|  |___| |_|  |__||_______|
 _______  ___      __   __  _______
|       ||   |    |  | |  ||       |
|       ||   |    |  | |  ||    ___|
|       ||   |    |  |_|  ||   |___
|      _||   |___ |       ||    ___|
|     |_ |       ||       ||   |___
|_______||_______||_______||_______|  \n\n""", style="bold")
    console.print("The Rules: ", style="bold")
    console.print("In the dealing phase each player must write down their cards \non seperate pieces of paper. When asking revealing clues then \nthe whole group must allow the two parties a private showing. \nAll applicable Clue rules still apply. This is currently in Beta, \nso any feedback is appreciated! Keep on your toes and enjoy \nremote detectives!\n\n\n\n(3-6 Player modes are in development! Select 4 to continue...)")
    if keyboard.read_key() == "3":
        three_player()

        # break
    if keyboard.read_key() == "4":
        four_player()
        console.print("The Rules: ", style="bold")
        input("In the dealing phase each player must write down their cards \non seperate pieces of paper. When asking revealing clues then \nthe whole group must allow the two parties a private showing. \nAll applicable Clue rules still apply. This is currently in Beta, \nso any feedback is appreciated! Keep on your toes and enjoy \nremote detectives!\n\n\n(press enter to continue...)\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[blue bold]Player One[/blue bold]")
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter for Player One's hand...\n\n\n\n\n\n\n\n\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[blue bold]Player One[/blue bold]")
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\nHere comes your hand Player One! Keep it a secret and press enter \nwhen you are ready to pass...\n\n\n\n\n\n\n\n\n\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[blue bold]Player One[/blue bold]")
        input(f"\n\n\n\n\n\n\nPlayer One write this down! Keep your eye on the player on the top left \nof your zoom screen. They are acting suspicious.\n\nPLAYER ONE'S HAND: {player1}\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter when your records are straight.\n")

        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red bold]Player Two[/red bold]")
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer two here comes your deal. Make sure no one else can see. \nTrust no one. Press enter to continue...\n\n\n\n\n\n\n\n\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red bold]Player Two[/red bold]")
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\nKeep this close to your chest and press enter when you are ready to pass...\n\n\n\n\n\n\n\n\n\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red bold]Player Two[/red bold]")
        input(f"\n\n\n\n\n\n\nPlayer Two write this down! Watch out for the top right player on the call. They are shifty.\n\nPLAYER TWO'S HAND: {player2}\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter when your records are straight.\n")

        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[yellow bold]Player Three[/yellow bold]")
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter for Player Three's hand...\n\n\n\n\n\n\n\n\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[yellow bold]Player Three[/yellow bold]")
        input("\n\n\n\n\n\n\n\n\n\n\n\n\nHere comes your hand Player Three! Keep it a secret and press enter when you are ready to pass...\n\n\n\n\n\n\n\n\n\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[yellow bold]Player Three[/yellow bold]")
        input(f"\n\n\n\n\nPlayer Three write this down! Keep your eye on the player on the \nbottom left of your zoom screen. They are acting suspicious.\n\nPLAYER THREE'S HAND: {player3}\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter when your records are straight.\n")

        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[green bold]Player Four[/green bold]")
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer Four here comes your deal. Make sure no one else can see. \nTrust no one. Press enter to continue...\n\n\n\n\n\n\n\n\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[green bold]Player Four[/green bold]")
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\nKeep this close to your chest and press enter when you are ready to pass...\n\n\n\n\n\n\n\n\n\n")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[green bold]Player Four[/green bold]")
        input(f"\n\n\n\n\n\n\nPlayer Four write this down! Watch out for the top right player on the call. They are shifty.\n\nPLAYER FOUR'S HAND: {player4}\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter when your records are straight.\n")

        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to open/close)")
        console.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTHE CASE FILE\n\n\n\n\n\n\n\n\n\n\n\n", style="red")
        input(f"(press enter to open/close)")
        console.print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[red]THE CASE FILE[/red]: [white]{crime_file}[/white]\n\n\n\n\n\n\n\n\n\n\n\n")
        input(f"(press enter to Close The Case. Write down evidence if you want to remember.)")
    # main()
        # break
    if keyboard.read_key() == "5":
        five_player()
        # break
    if keyboard.read_key() == "6":
        six_player()
        # break
multi()
