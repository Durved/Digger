import pygame
from map import MAP

class Gold(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=pos)
        self.cell = self.rect.centerx // 64
        self.row = self.rect.centery // 64
    


    def update(self):
        self.cell = self.rect.centerx // 64
        self.row = self.rect.centery // 64

        if MAP[self.rect.bottom // 64][self.cell] == ' ' or MAP[(self.rect.bottom + 60) // 64][self.cell] == ' ':
            self.rect.centery += 2

        # if self.row < 7:
        #     if MAP[self.row + 1][self.cell] == ' ':
        #         self.rect.bottom += 2
        #         MAP[self.row][self.cell] = ' '
        #     elif MAP[self.row][self.cell] == ' ':
        #         self.rect.bottom += 2
        #         if self.rect.bottom // 64 > self.row:
        #             self.rect.bottom = self.row * 64 + 64

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 448:
            self.rect.bottom = 448
        if self.rect.right > 640:
            self.rect.right = 640