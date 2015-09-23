__author__ = 'mukulhase'
class Person(pygame.sprite.Sprite):
    """Movable gravity affected class"""

    def __init__(self, name, pos_x, pos_y, height, width, speed):
        self.name = name
        self.initialpos = (pos_x,pos_y)
        self.screen = pygame.display.get_surface()
        self.width = width
        self.height = height
        self.jumpspeed = screenh/(rows*3)
        self.movespeed = speed
        self.speed_x = 0
        self.speed_y = 0
        self.acc_y = screenh/(rows*40)
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(name + '.png', -1)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.y = pos_y
        self.rect.x = pos_x

    def reset(self):
        self.rect.x,self.rect.y = self.initialpos

    def move(self, direction):
        if direction == "l":
            self.speed_x = -self.movespeed
        elif direction == "r":
            self.speed_x = self.movespeed

    def acceleration(self):
        self.speed_y = self.speed_y + self.acc_y

        if self.rect.y >= screenh - self.rect.height and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = screenh - self.rect.height

    def stop(self):
        self.speed_x = 0

    def collisionx(self):
        self.touched = pygame.sprite.spritecollide(self, walls, False)
        for block in self.touched:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
            elif self.speed_x < 0:
                self.rect.left = block.rect.right

    def jump(self):
        if self.speed_y <= screenh / 400 and self.speed_y >= -screenh / 400:
            self.speed_y = -self.jumpspeed

    def collisiony(self):
        touched = pygame.sprite.spritecollide(self, walls, False)
        for block in touched:
            if self.speed_y == 0:
                pass
            else:
                if self.speed_y > 0:
                    if self.speed_y > screenh / (20*rows):
                        self.landed()
                    self.rect.bottom = block.rect.top
                elif self.speed_y < 0:
                    self.rect.top = block.rect.bottom

                self.speed_y = 0

    def landed(self):
        pass

    def update(self):
        self.acceleration()
        self.rect.x += self.speed_x
        self.collisionx()
        self.rect.y += self.speed_y
        self.collisiony()
