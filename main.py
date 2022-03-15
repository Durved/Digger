from xml.etree.ElementTree import QName
import pygame
from map import MAP
from player import Player

pygame.init()
pygame.display.set_caption('Digger')

screen = pygame.display.set_mode((640, 480), 0, 32)
main_clock = pygame.time.Clock()

dirt_surf = pygame.Surface((64, 64))
dirt_surf.fill('brown')

for r_i, r in enumerate(MAP):
    for c_i, c in enumerate(r):
        if c == 'p':
            player = Player((c_i * 64, r_i*64))
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.update()
    MAP[player.row][player.cell] = ' '

    for r_i, r in enumerate(MAP):
        for c_i, c in enumerate(r):
            if c == 'd':
                screen.blit(dirt_surf, (c_i*64, r_i*64))
    screen.blit(player.image, player.rect)
    pygame.display.update()
    screen.fill('black')
    main_clock.tick(60)