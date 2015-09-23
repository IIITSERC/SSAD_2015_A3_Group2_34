
class Donkey(Person):
    def __init__(self):
        Person.__init__(self, "donkey", 20, screenh/rows, screenh / (2 * rows), screenh / (2 * rows), screenw / 100)
        allsprites.add((self))

    def spewfire(self):
        if random.randrange(1000) < 5:
            fireball = Fireball(self.rect.x, self.rect.y + screenh / rows)
            fireballs.add(fireball)

    def update(self):
        Person.update(self)
        self.spewfire()
        if self.rect.x > game.firstrowsize - self.width:
            self.rect.x = game.firstrowsize - self.width
        if random.randrange(1000) < 50:

            if bool(random.getrandbits(1)):
                self.move("r")
            else:
                self.move("l")
            if bool(random.getrandbits(1)):
                self.stop()
