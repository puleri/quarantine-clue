from random import shuffle

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
        #deal cards here using deck.pop()
        # print(deck.pop().__str__)  #just to prove it works randomly =P
        print(name[card])
