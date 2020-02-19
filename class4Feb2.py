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
font = pygame.font.Font(None, 48)
txt_surf = font.render("First Name Last Name", True, (255, 255, 255))
buffer = pygame.image.load('13.jpg')
buffer = pygame.transform.scale(buffer, (500, 400))
surface.blit(buffer, (150, 100))
pygame.draw.polygon(surface, (255, 255, 0), [(300, 100), (250, 150), (350, 150)], 0)
surface.blit(txt_surf, (400 - int(txt_surf.get_size()[0] / 2), 300 - int(txt_surf.get_size()[1] / 2)))
pygame.mixer.init()
pygame.mixer.music.load('01Despacito.mp3')
pygame.mixer.music.play()

while not finished:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finished = 1
            break
        if e.type == pygame.KEYUP:
            pygame.mixer.music.pause()
    pygame.display.update()