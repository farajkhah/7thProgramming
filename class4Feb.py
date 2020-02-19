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

pygame.draw.line(surface, Green, (0, 0), (800,600), 5)
pygame.draw.rect(surface, blue, (100, 100, 50, 30), 2)
rect1 = pygame.draw.rect(surface, (255, 255, 255), (102, 102, 46, 26), 0)
pygame.draw.circle(surface, (255, 0, 255), (200, 300), 100, 0)
pygame.draw.polygon(surface, (255, 255, 0), [(300, 50), (250, 100), (350, 100)], 0)

while not finished:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finished = 1
            break
        if e.type == pygame.MOUSEMOTION:
            if rect1.collidepoint(e.pos):
                pygame.draw.rect(surface, (0, 0, 0), (102, 102, 46, 26), 0)
            else:
                pygame.draw.rect(surface, (255, 255, 255), (102, 102, 46, 26), 0)
        if e.type == pygame.MOUSEBUTTONUP:
            if rect1.collidepoint(e.pos):
                finished = 1
                break
    pygame.display.update()