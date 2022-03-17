from copy import deepcopy
import pygame
from map import MAP
from player import Player
from gold import Gold

pygame.init()
pygame.display.set_caption('Digger')

screen = pygame.display.set_mode((640, 480), 0, 32)
main_clock = pygame.time.Clock()

dirt_surf = pygame.Surface((64, 64))
dirt_surf.fill('brown')

emerald_surf = pygame.Surface((32, 32))
emerald_surf.fill('green')

golds = pygame.sprite.Group()

for r_i, r in enumerate(MAP):
    for c_i, c in enumerate(r):
        if c == 'p':
            pos = (c_i * 64, r_i*64)
            player = Player(pos)
        if c == 'g':
            MAP[r_i][c_i] = 'd'
            golds.add(Gold((c_i * 64 + 16, r_i*64 + 16)))
        
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.update()
    for i in pygame.sprite.spritecollide(player, golds, False):
        if player.rect.bottom - i.rect.bottom > 32:
            player.rect.topleft = pos
        else:
            if i.rect.left - player.rect.left > 0 :
                if i.rect.right < 640:
                    i.rect.left = player.rect.right
            elif i.rect.left > 0:
                i.rect.right = player.rect.left
    golds.update()
    MAP[player.row][player.cell] = ' '

    for r_i, r in enumerate(MAP):
        for c_i, c in enumerate(r):
            if c == 'd':
                screen.blit(dirt_surf, (c_i*64, r_i*64))
            elif c == 'e':
                screen.blit(dirt_surf, (c_i*64, r_i*64))
                screen.blit(emerald_surf, (c_i*64+16, r_i*64+16))

    golds.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.update()
    screen.fill('black')
    main_clock.tick(60)