

class Princess(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('princess.png', -1)
        self.height= screenh / (2*rows)
        self.width= (screenh/(3*rows))
        self.image = pygame.transform.scale( self.image,( self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        cage = Wall(self.width,10,self.rect.x,self.rect.y + self.height)

