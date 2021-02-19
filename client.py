import pygame

# run with python client

width = 500
height = 500

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")

clientNumber = 0

class Card:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)


class Deck:
    def __init__(self):
        self.cards = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Hall", "Study", "Library", "Billiard Room", "Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench", "Miss Scarlett", "Rev Green", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mrs. White"]
        # self.build()


    # def build(self):
    #     for i in ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Hall", "Study", "Library", "Billiard Room", "Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench", "Miss Scarlett", "Rev Green", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mrs. White"]:
    #         self.cards.append(Card(i))

    def length(self):
        return len(self.cards)

    def return_cards(self, cards):
        self.cards.extend(cards)

    # def __str__(self):
    #     return("Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Hall", "Study", "Library", "Billiard Room", "Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench", "Miss Scarlett", "Rev Green", "Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mrs. White")
    #
    # def __repr__(self):
    #     return str(self)

class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.cards = deck.cards

    def deal(self):
        i=0
        for player in self.players:
            i+=1
            for card in range(i):

                player.cards.append(self.drawCard())

    def drawCard(self):
        drawnCard = self.deck.cards[0]
        self.deck.cards = self.deck.cards[0:]
        return drawnCard

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        # self.x = x
        # self.y = y
        # self.width = width
        # self.height = height
        # self.color = color
        # self.rect = (x,y,width,height)
        # self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

def return_cards(self, deck):
    deck.return_cards(self.cards)
    self.cards = []

# def redrawWindow(win, player):
#     win.fill((255,255,255))
#     player.draw(win)
#     pygame.display.update()
#
my_username = input("Username:")
def main():
    run = True
    # p = Player(50,50,100,100,(0,255,0))
    # clock = pygame.time.Clock()
    clueDeck = Deck()
    matt = Player("Matt")
    jo = Player("Jo")
    newGame = Game([matt, jo], clueDeck)
    newGame.deal()
    # print ([card for card in clueDeck.cards])
    print(clueDeck.cards)
    return_cards(clueDeck, clueDeck)
    # while run:
        # clocl.tick(60)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #         pygame.quit()
        # p.move()
        # redrawWindow(win, p)

main()
