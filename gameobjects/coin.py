
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('coin.png', -1)
        self.image = pygame.transform.scale(self.image, (screenh / (2 * rows), screenh / (2 * rows)))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        global score
        touched = pygame.sprite.spritecollide(self, allsprites, False)
        if len(touched) != 0:
            score+=1
            self.kill()
