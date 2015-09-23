
class Mario(Person):
    def __init__(self):
        Person.__init__(self, "mario", screenw / 10, screenh - screenh / (rows*2), screenh / (3 * rows),
                        int(screenh/(4*rows)), int(screenh / (10.0*rows)))
        self.climbing = False

    def jump(self):
        ##pygame.mixer.music.load('data/jump.ogg')
        Person.jump(self)

    def acceleration(self):
        if self.climbing:
            pass
        else:
            Person.acceleration(self)

    def move(self, direction):
        self.climbing = False
        Person.move(self, direction)

    def climb(self, direction):
        touched = pygame.sprite.spritecollide(self, ladders, False)
        if len(touched) != 0:
            self.speed_x = 0
            if direction == "up":
                self.speed_y -= screenh / (rows * 20)
            else:
                self.speed_y += screenh / (rows * 20)
            self.rect.x = touched[0].rect.x
            self.climbing = True
        else:
            self.jump()
            self.climbing = False

    def stopclimb(self):
        touched = pygame.sprite.spritecollide(self, ladders, False)
        if len(touched) == 0:
            self.jump()
            self.climbing = False
        else:
            self.speed_y = 0

    def collisionx(self):
        Person.collisionx(self)
        firetouched = pygame.sprite.spritecollide(self, fireballs, False)

        if len(firetouched) != 0:
            game.loselife()
        if len(self.touched)>0:
            if self.rect.y < screenh / rows:
                self.kill()
                game.gameover("You Won!")
