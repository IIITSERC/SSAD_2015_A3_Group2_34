
class Fireball(Person):
    def __init__(self, pos_x, pos_y):
        Person.__init__(self, "fireball", pos_x, pos_y, screenh / (3 * rows), screenh/(3*rows), screenw / 400)
        if bool(random.getrandbits(1)):
            self.move("r")
        else:
            self.move("l")

    def landed(self):
        if bool(random.getrandbits(1)):
            self.move("r")
        else:
            self.move("l")

    def collisionx(self):
        touched = pygame.sprite.spritecollide(self, walls, False)
        for block in touched:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
                self.speed_x = -self.speed_x
            elif self.speed_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                self.speed_x = -self.speed_x
                if self.rect.y > screenh - screenh / rows:
                    if self.rect.x <= 40:
                        self.kill()

    def collisiony(self):
        Person.collisiony(self)
        touched = pygame.sprite.spritecollide(self, ladders, False)
        if len(touched) != 0:
            if self.speed_y > 0:
                if random.randrange(100) < 20:
                    self.jump()
