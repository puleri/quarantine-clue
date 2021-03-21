# Quarantine Clue (Alpha)

## About
Quarantine clue is meant to make the game of clue accessible to folks who own the physical game and want to play with friends or family remotely. This game is designed to be minimally invasive and to place the focus on the zoom call and interpersonal communications.

---

## Technologies used
ATOM, Socket.io, selector, Python3

---

### Planning Strategy
In the first days of strategizing, I read countless documentation on creating card games from Google, and watching tutorial videos on Youtube. When I decided on a structure I began with my first client file. The first iteration printed a list to the console of all the cards. Next, I created new lists with each of the types of cards. The type lists are used to randomly deal one of each to the crime file before compiling to a singular deck. Finally the players are all dealt their hands. 

After getting all the parts functional I decided to go with a simple terminal "GUI" that requires an `enter` input to proceed through each step of the deal and finally created a toggle where you can see/hide the case file.

---

#### Unsolved Issues
- All the data is displayed on the terminal and is not formatted well.

- In V 1.0 I would like to have this solved by running a window/GUI that functions the same.

- There is no way to pull up each players hand after getting to the crime file. I could solve this by binding 1,2,3,4 to the corresponding players hands.

---

#### Command(s)
| Place | Action   | Command               |
|--------|--------|------------------------|
| Terminal | runs file   | `python client.py`             |

