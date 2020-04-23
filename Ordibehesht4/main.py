import pygame
import sys
import readQ as rq

loc_list = [(10, 300), (10, 350), (200, 350), (10, 400), (200, 400)]


def update_page(screen, soal, rect0, txtsrf, Onit, file_pic):
    screen.fill((255, 255, 255))
    for i in range(len(soal)):
        cntsrf = font.render(soal[i], True, (0, 0, 255))
        screen.blit(cntsrf, loc_list[i])
    if Onit:
        pygame.draw.rect(screen, (155, 0, 0), rect0, 0)
        screen.blit(txtsrf, (100 + (50 - wi // 2), 100 + (50 - he // 2)))
    else:
        pygame.draw.rect(screen, (255, 0, 0), rect0, 0)
        screen.blit(txtsrf, (100 + (50 - wi // 2), 100 + (50 - he // 2)))


w = 800
h = 600
pygame.init()

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Class_March')
font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()
screen.fill((255,255,255))

rect0 = pygame.Rect(100, 100, 100, 100)
pygame.draw.rect(screen, (255,0,0), rect0, 0)
txtsrf = font.render("start", True, (255, 255, 0))
wi = txtsrf.get_width()
he = txtsrf.get_height()
screen.blit(txtsrf, (100 + (50 - wi//2), 100 + (50 - he//2)))
finished = False
file = open("quize.mhd", "rt")
cnt = 0
cntsrf = font.render(str(cnt), True, (255, 255, 0))
Onit = False
while not finished:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            finished = True
        if e.type == pygame.MOUSEMOTION:
            if rect0.collidepoint(e.pos):
                Onit = True
                pygame.draw.rect(screen, (155, 0, 0), rect0, 0)
                screen.blit(txtsrf, (100 + (50 - wi // 2), 100 + (50 - he // 2)))
            else:
                Onit = False
                pygame.draw.rect(screen, (255, 0, 0), rect0, 0)
                screen.blit(txtsrf, (100 + (50 - wi // 2), 100 + (50 - he // 2)))
        if e.type == pygame.MOUSEBUTTONUP:
            if rect0.collidepoint(e.pos):
                cnt += 1
                soal, gtrue, ap = rq.read_q(file, cnt)
                if soal == "NULL":
                    update_page(screen, ["Soalat be payan reside..."], rect0, txtsrf, Onit, ap)
                else:
                    print(gtrue)
                    update_page(screen, soal, rect0, txtsrf, Onit, ap)

    pygame.display.update()
    clock.tick(20)

pygame.display.quit()
pygame.quit()
sys.exit()
