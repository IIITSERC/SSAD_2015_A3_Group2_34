__author__ = 'mukul'
'''Message To TA's
To help look through code
Person --> Person
Player --> Mario
Donkey -->Donkey
Board --> Screen (implemented by pygame)
Fireball --> Fireball(made it a class of person to make the code more elegant)
Used C-style library imports(exec) instead of python based modular imports(import), game's variables are heavily dependent on each other to make it smooth and scalable, hence many things had to be declared globally because passing and returning 10+ arguments is not viable
implemented my own version of gravity, hence i didnt make a jump 2 moves up 2 moves down
collisions not unified, many classes have different collision function addons which are handled by overrides
'''
# !/usr/bin/python
import pygame
pygame.init()
execfile("gameobjects/person.py")
execfile("gameobjects/mario.py")
execfile("gameobjects/donkey.py")
execfile("gameobjects/fireball.py")
execfile("gameobjects/princess.py")
execfile("gameobjects/coin.py")
execfile("gameobjects/wall.py")
execfile("gameobjects/ladders.py")
import os
import random
import sys
import defaultvalues

def load_image(name, colorkey=None, scale=(100, 100)):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = pygame.transform.scale(image, scale).convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image, image.get_rect()


class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((screenw, screenh), 0, 32)
        self.state = "quit"
        self.firstrowsize = screenw * 4 / 5
        # self.currentScreen = "Game Menu"
        pygame.mixer.music.load('data/theme.ogg')
        pygame.mixer.music.play(-1)
        self.menu_items = (
        'Press any key to start', 'Keys :-', 'up->jump/climb', 'left/right-> go left/right', 'space->jump')

    def loselife(self):
        global lives
        print "lives "+ str(lives)
        lives = lives - 1
        if lives <= 0:
            game.state="lose"
            lives=3
            game.gameover("You ran out of lives")
        self.mario.reset()

    def start(self):
        pygame.display.set_caption('Game Menu')
        gm = GameMenu(self.screen, self.menu_items)
        if gm.run() == "play":
            self.play()
            print game.state
            while game.state == "retry" or game.state == "next":
                if game.state == "retry":
                    self.play()
                elif game.state == "next":
                    self.levelup()
                    self.play()
            pass

    def levelup(self):
        global rows
        global donkeycount
        currentlvl = rows + donkeycount
        if currentlvl % 5 == 0:
            donkeycount += donkeycount
        else:
            rows += 1

    def play(self):
        self.mainloop = True
        self.mario = Mario()
        for i in range(donkeycount):
            donkey = Donkey()
        princess = Princess(20, 20)
        allsprites.add((self.mario, princess))

        clock = pygame.time.Clock()
        pygame.display.flip()

        ladderpos = []
        positions = []
        positions.append([self.firstrowsize, 10, 0, 2 * screenh / (rows)])

        for i in range(2, rows):
            ldrpos = random.randint(20, 80) * (screenw / 100)
            x = random.randint(7, 9)
            ladderpos.append([ldrpos, screenh * (i + 1) / rows])
            pos = [0, 0, 0, 0]
            pos[0] = (ldrpos / 10) * x * ((i + 1) % 2) + ldrpos * ((i) % 2)
            pos[1] = 10
            pos[2] = (ldrpos / 10) * (10 - x) * ((i + 1) % 2)
            pos[3] = (screenh * (i + 1) / rows)
            positions.append(pos)
            other = screenw - ldrpos - laddersize
            pos = [0, 0, 0, 0]
            pos[0] = (other / 10) * x * (i % 2) + other * ((i + 1) % 2)
            pos[1] = 10
            pos[2] = ldrpos + laddersize
            pos[3] = (screenh * (i + 1) / rows)
            positions.append(pos)
            brokenladder = Ladder(random.randint(20, 80) * (screenw / 100), screenh * (i + 1.5) / rows, True)
            while random.randint(0, 10) <= 7.5:
                coin = Coin(random.randint(20, screenw - 20 - screenh / (2 * rows)), screenh * (i + 1.5) / rows)
                coins.add(coin)

        for pos in ladderpos:
            ladder = Ladder(pos[0], pos[1], False)

        positions.append([20, screenh, 0, 0])
        positions.append([20, screenh, screenw - 20, 0])
        positions.append([screenw - 40, 10, 0, 0])

        for pos in positions:
            wall = Wall(pos[0], pos[1], pos[2], pos[3])

        while self.mainloop:
            pygame.display.set_caption("Play Current Score = " + str(score))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.gameover("you quit")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game.gameover("You quit")
                    if event.key == pygame.K_LEFT:
                        self.mario.move("l")
                    if event.key == pygame.K_RIGHT:
                        self.mario.move("r")
                    if event.key == pygame.K_SPACE:
                        self.mario.jump()
                    if event.key == pygame.K_UP:
                        self.mario.climb("up")
                    if event.key == pygame.K_DOWN:
                        self.mario.climb("down")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.mario.speed_x < 0:
                        self.mario.stop()
                    if event.key == pygame.K_RIGHT and self.mario.speed_x > 0:
                        self.mario.stop()
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.mario.stopclimb()

            allsprites.update()
            fireballs.update()
            coins.update()

            self.screen.fill((0, 0, 0))
            ladders.draw(self.screen)
            allsprites.draw(self.screen)
            walls.draw(self.screen)
            fireballs.draw(self.screen)
            coins.draw(self.screen)
            clock.tick(60)
            pygame.display.flip()

        return True

    def gameover(self, text):
        game.mainloop = False
        game.cleanup()
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 30)
        font_color = (255, 255, 255)
        label = font.render("Game Over - " + text + ", your score: Coins: " + str(score) + " Time: " + str(
            pygame.time.get_ticks()) + " Score: " + str(score * (100000000 / (pygame.time.get_ticks() + 50))), 1,
                            (255, 255, 255))
        width = label.get_rect().width
        self.screen.fill((0, 0, 0))
        self.screen.blit(label, ((screenw / 2) - (width / 2), screenh / 2))
        label2 = font.render("Next Level -> n , Retry Level -> r, Quit -> q", 1, (255, 255, 255))
        width = label2.get_rect().width
        self.screen.blit(label2, ((screenw / 2) - (width / 2), screenh / 2 + label2.get_rect().height))
        pygame.display.flip()
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.state = "retry"
                        loop = False
                    elif event.key == pygame.K_n:
                        self.state = "next"
                        loop = False
                    elif event.key == pygame.K_q:
                        self.state = "quit"
                        loop = False
                if event.type == pygame.QUIT:
                    self.state = "quit"
                    loop = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "quit"
                    loop = False

    def cleanup(self):
        allsprites.empty()
        ladders.empty()
        fireballs.empty()
        coins.empty()
        walls.empty()


class GameMenu():
    def __init__(self, screen, items):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.items = items
        self.font = pygame.font.SysFont(None, 30)
        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, (255, 255, 255))
            width = label.get_rect().width
            height = label.get_rect().height
            posx = (screenw / 2) - (width / 2)
            t_h = len(items) * height
            posy = (screenh / 2) - (t_h / 2) + (index * height)
            self.items.append([item, label, (width, height), (posx, posy)])

    def run(self):
        mainloop = True
        nextflag = False
        while mainloop:
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                elif event.type == pygame.KEYDOWN:
                    mainloop = False
                    nextflag = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mainloop = False
                    nextflag = True

            self.screen.fill((0, 0, 0))

            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))

            pygame.display.flip()

        if nextflag == True:
            return "play"
        return "quit"


if __name__ == "__main__":
    score = 0
    lives = 3

    if "-d" in sys.argv:
        screenh = defaultvalues.screenh
        screenw = defaultvalues.screenw
        rows = defaultvalues.rows
        donkeycount = defaultvalues.donkeycount
    else:
        defaults = raw_input("Want to load defaults? (y/n) ")
        if defaults == "y":
            screenh = defaultvalues.screenh
            screenw = defaultvalues.screenw
            rows = defaultvalues.rows
            donkeycount = defaultvalues.donkeycount
        else:
            screenh = input("vertical res:- ")
            screenw = input("horizontal res:- ")
            rows = input("difficulty -> rows:- ")
            donkeycount = input("difficulty -> donkeys:- ")

    laddersize = screenh / (rows * 2)
    coins = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    fireballs = pygame.sprite.Group()
    ladders = pygame.sprite.Group()
    laddersize = screenh / (rows * 2)
    allsprites = pygame.sprite.Group()

    game = Game()
    game.start()
