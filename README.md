# Quarantine Clue (Alpha)

## About
Quarantine clue is meant to make the game of clue accessible to folks who own the physical game and want to play with friends or family remotely. This game is designed to be minimally invasive and to place the focus on the zoom call and interpersonal communications.

---

## Technologies used
ATOM, Socket.io, selector, Python3

---

### Planning Strategy
In the first days of strategizing, I read countless documentation from the official Adobe ColdFusion page, from OrtuSolutions, and watching official videos on Youtube. Next came downloading and practicing basic uses of CommandBox and starting a CF project. When running the local server via CommandBox for the first time and using the <cfoutput> tags I began feeling confident with the new language. It was at this point I started to create the backend with Express which I am comfortable with. The point being to introduce less unknown variables to the learning process of learning ColdFusion. When connecting the front and backend I began seeing handshake issues and diverted to fixing this in Node and JS.

We decided to produce a minimal viable product before completing the Socket Middleware but still managed to establish a Socket Connection and Disconnect linked to the Chat Index CRUD Action.

---

#### Unsolved Issues
- All the data is displayed in one place.

- In the BETA I would like to have this solved by running a program that simply accepts commands asking the user "Player __ are you there? If you are ready press `space` to see your cards".

- I would then like the player to see their cards and be asked to "Press `space` again when you are ready to hide your cards."

- This would repeat for each player until finally the last player hides their cards and the next spaces reveal/hide the crime file.

---

#### Command(s)
| Place | Action   | Command               |
|--------|--------|------------------------|
| Terminal | runs file   | `python client.py`             |

