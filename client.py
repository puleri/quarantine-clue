from random import shuffle

player1 = []
player2 = []
player3 = []
player4 = []

players = [player1, player2, player3, player4]

class Card:
    def __init__(self,name):
        self.name = name

    # def __str__(self):
    #     print(self)


deck = list()
name = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Hall", "Study", "Library", "Billiard Room", "Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench", "Miss Scarlett", "Rev Green", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mrs. White"]

for n in name: #This is the code that actually makes a deck
    deck.append(Card(n))

shuffle(name)
for card in range(21):
    counter = 1
        #deal cards here using deck.pop()
        # print(deck.pop().__str__)  #just to prove it works randomly =P
    for player in players:
        if (name.index(name[card]) == 1):
            player.append(name[card])
            counter += 1
            break
        if (name.index(name[card]) == 2):
            player.append(name[card])
            counter += 1
            break
        if (name.index(name[card]) == 3):
            player.append(name[card])
            counter += 1
            break
        if (name.index(name[card]) == 4):
            player.append(name[card])
            counter = 0
            break

            # player.append(name[card])
            print(name[card])
            break

print(player1)
