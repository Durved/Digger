import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=pos)
        self.cell = self.rect.centerx // 64
        self.row = self.rect.centery // 64
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.cell = self.rect.centerx // 64
        self.row = self.rect.centery // 64
        cell_y = self.rect.top - self.row * 64
        cell_x = self.rect.left - self.cell * 64

        if keys[pygame.K_UP]:
            if cell_x == 0:
                self.rect.centery -= 2
            elif cell_x > 0:
                self.rect.centerx -= 2
            else:
                self.rect.centerx += 2
        elif keys[pygame.K_DOWN]:
            if cell_x == 0:
                self.rect.centery += 2
            elif cell_x > 0:
                self.rect.centerx -= 2
            else:
                self.rect.centerx += 2
        elif keys[pygame.K_LEFT]:
            if cell_y == 0:
                self.rect.centerx -= 2
            elif cell_y > 0:
                self.rect.centery -= 2
            else:
                self.rect.centery += 2
        elif keys[pygame.K_RIGHT]:
            if cell_y == 0:
                self.rect.centerx += 2
            elif cell_y > 0:
                self.rect.centery -= 2
            else:
                self.rect.centery += 2

    def update(self):
        self.input()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 448:
            self.rect.bottom = 448
        if self.rect.right > 640:
            self.rect.right = 640