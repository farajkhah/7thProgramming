import pygame

pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('paint')
Green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
color = [Green, blue, red]
surface.fill(red)
i = 0
finished = False
while not finished:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finished = 1
            break
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_F1:
                finished = 1
                break
        elif e.type == pygame.MOUSEBUTTONUP:
            print(e.pos)
        elif e.type == pygame.MOUSEMOTION:
            print(e.pos)
    pygame.display.update()