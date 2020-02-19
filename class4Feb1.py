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

buffer = pygame.image.load('13.jpg')
buffer = pygame.transform.scale(buffer, (500, 400))
surface.blit(buffer, (150, 100))
pygame.draw.polygon(surface, (255, 255, 0), [(300, 100), (250, 150), (350, 150)], 0)
while not finished:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finished = 1
            break
    pygame.display.update()