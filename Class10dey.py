import pygame

#initialize and create window
pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('paint')

#colors
Green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
color = [Green, blue, red]

surface.fill(red)
i = 0
finished = False

#main loop
while not finished:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finished = 1
            break
        if e.type == pygame.MOUSEBUTTONDOWN:
            print(e.pos)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_b:
                i = (i + 1)%3
                surface.fill(color[i])
    pygame.display.update()
