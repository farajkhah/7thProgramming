import pygame
import sys


white = (255,255, 255)
yellow = (180, 180, 0)

def update_page(screen, text, rect0, txtsrf, Onit, active):
    screen.fill((255, 255, 255))
#    cntsrf = font.render(str(cnt), True, (0, 0, 255))
#    screen.blit(cntsrf, (300, 300))
    label = font.render("E-mail:", True, (0, 0, 0))
    screen.blit(label, (180, 300))
    inputsrf = font.render(text, True, (0, 255, 0))
    r1 = inputsrf.get_rect()
    x, y = r1.topleft
    width_input = max(160, r1.width+10)
    if active:
        pygame.draw.rect(screen, white, text_box, 0)
    else:
        pygame.draw.rect(screen, yellow, text_box, 0)
    pygame.draw.rect(screen, (0, 0, 0), (x + 295, y + 295, width_input, 40), 2)
    if text == '':
        inputsrf = font_first.render("write your name", True, (200, 200, 200))
        screen.blit(inputsrf, (300, 310))
    else:
        screen.blit(inputsrf, (300, 300))

    if Onit:
        pygame.draw.rect(screen, (155, 0, 0), rect0, 0)
        screen.blit(txtsrf, (100 + (50 - wi // 2), 100 + (50 - he // 2)))
    else:
        pygame.draw.rect(screen, (255, 0, 0), rect0, 0)
        screen.blit(txtsrf, (100 + (50 - wi // 2), 100 + (50 - he // 2)))


w = 800
h = 600

pygame.init()

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Class_March')
font = pygame.font.Font(None, 40)
font_first = pygame.font.Font(None, 20)
clock = pygame.time.Clock()
screen.fill((255,255,255))

rect0 = pygame.Rect(100, 100, 100, 100)
pygame.draw.rect(screen, (255,0,0), rect0, 0)
txtsrf = font.render("start", True, (255, 255, 0))
wi = txtsrf.get_width()
he = txtsrf.get_height()
screen.blit(txtsrf, (100 + (50 - wi//2), 100 + (50 - he//2)))
finished = False
cnt = 0
cntsrf = font.render(str(cnt), True, (255, 255, 0))
text = ''

inputsrf = font_first.render("write your name", True, (200, 200, 200))
r1 = inputsrf.get_rect()
x, y = r1.topleft
text_box = pygame.Rect(x + 295, y + 295, 160, 40)
pygame.draw.rect(screen, yellow, text_box, 0)
pygame.draw.rect(screen, (0,0,0), text_box, 2)

screen.blit(inputsrf, (300, 310))

label = font.render("E-mail:", True, (0,0,0))
screen.blit(label, (180,300))

active = False
Onit = False
#rect_input = (295,295, 160, 40)
#pygame.draw.rect(screen, (0, 0, 0), rect_input, 2)
text = ''

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
                update_page(screen, cnt, rect0, txtsrf, Onit, active)
            if text_box.collidepoint(e.pos):
                active = True
                update_page(screen, text, rect0, txtsrf, Onit, active)
            else:
                active = False
                update_page(screen, text, rect0, txtsrf, Onit, active)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                finished = True
            elif e.key == pygame.K_BACKSPACE:
                if active:
                    if len(text) > 0:
                        text = text[:-1]
                        update_page(screen, text, rect0, txtsrf, Onit,active)
                    else:
                        inputsrf = font_first.render("write your name", True, (200, 200, 200))
                        screen.blit(inputsrf, (300, 310))
            else:
                if active:
                    if len(text) < 15:
                        text = text + str(e.unicode)
                        update_page(screen, text, rect0, txtsrf, Onit, active)

    pygame.display.update()
    clock.tick(20)

pygame.display.quit()
pygame.quit()
sys.exit()
