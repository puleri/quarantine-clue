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

for i in range(5):
    player1.append(name[i])
    name.remove(name[i])
for j in range(5):
    player2.append(name[j])
    name.remove(name[j])
for k in range(4):
    player3.append(name[k])
    name.remove(name[k])
for l in range(4):
    player4.append(name[l])
    name.remove(name[l])
# for card in range(21):
#     counter = 1
#         #deal cards here using deck.pop()
#         # print(deck.pop().__str__)  #just to prove it works randomly =P
#     for player in players:
#         if (name.index(name[card]) == 1):
#             player.append(name[card])
#             counter += 1
#             break
#         if (name.index(name[card]) == 2):
#             player.append(name[card])
#             counter += 1
#             break
#         if (name.index(name[card]) == 3):
#             player.append(name[card])
#             counter += 1
#             break
#         if (name.index(name[card]) == 4):
#             player.append(name[card])
#             counter = 0
#             break
#
#             # player.append(name[card])
#             print(name[card])
#             break

print("Player 1's hand: ", player1, "\nPlayer 2's hand: ",player2,"\nPlayer 3's hand: ", player3,"\nPlayer 4's hand: ", player4)
print(name)
