# pygame-assignment

Features
  - Everything is randomized
  - All values are interlinked to make the game scale well
  - Works with all resolutions above 600x600
  - Higher the resolution the bigger you can make the game
  - infinite generated levels
  - customisable
  - multiple donkeys

To help look through code
- Person --> Person
- Player --> Mario
- Donkey -->Donkey
- Board --> Screen (implemented by pygame)
- Fireball --> Fireball(made it a class of person to make the code more elegant)
- Used C-style library imports(exec) instead of python based modular imports(import), game's variables are heavily dependent on each other to make it smooth and scalable, hence many things had to be declared globally because passing and returning 10+ arguments is not viable
- implemented my own version of gravity, hence i didnt make a jump 2 moves up 2 moves down
- collisions not unified, many classes have different collision function addons which are handled by overrides
