

class Ladder(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, broken):
        pygame.sprite.Sprite.__init__(self)
        self.broken = broken
        ladders.add(self)
        if broken == True:
            self.image, self.rect = load_image('ladderbroken.png', -1)
            self.image = pygame.transform.scale(self.image, (laddersize, screenh / (2*rows)))

        else:
            self.image, self.rect = load_image('ladder.png', -1)
            self.image = pygame.transform.scale(self.image, (laddersize, screenh / rows))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y


