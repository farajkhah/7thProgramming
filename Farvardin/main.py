import pygame
import First_page as fp
import Second_page as sp
import Game_page as gp
import defines as df
import sys


def main_page():
    w = 800
    h = 600
    del df.page_queue[:]
    df.page_pointer = 0
    df.page_queue.append("main")

    pygame.init()

    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Class_March')
    font = pygame.font.Font("times.ttf", 32)
    clock = pygame.time.Clock()
    screen.blit(pygame.image.load("1.jpg"), (0,0))
    w, h = pygame.display.get_surface().get_size()
    cols = [(0, 180, 0),(0, 230, 0)]
    finished = False
    Onitr = [0, 0, 0]

    page_title = font.render("You Are in the Main Page!", True, (0, 0, 255))

    txt_0 = font.render("First page", True, (255, 255, 255))
    txt_1 = font.render("Second page", True, (255, 255, 255))
    txt_2 = font.render("Start", True, (255, 255, 255))

    rect0 = pygame.Rect(w // 3 - 90, h // 2 - 20, 180, 40)
    rect1 = pygame.Rect((w * 2) // 3 - 90, h // 2 - 20, 180, 40)
    rect2 = pygame.Rect(w // 2 - 90, (h *4) // 5 - 20, 180, 40)
    pygame.draw.rect(screen, cols[1], rect0, 0)
    pygame.draw.rect(screen, cols[1], rect1, 0)
    pygame.draw.rect(screen, cols[1], rect2, 0)

    while not finished:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                finished = 1
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONUP:
                if rect0.collidepoint(e.pos):
                    df.page_pointer += 1
                    fp.first_page(screen, font)
                elif rect1.collidepoint(e.pos):
                    df.page_pointer += 1
                    sp.second_page(screen, font)
                elif rect2.collidepoint(e.pos):
                    df.page_pointer += 1
                    gp.game_page(screen, font)
            if e.type == pygame.MOUSEMOTION:
                if rect0.collidepoint(e.pos):
                    Onitr[0] = 1
                elif rect1.collidepoint(e.pos):
                    Onitr[1] = 1
                elif rect2.collidepoint(e.pos):
                    Onitr[2] = 1
                else:
                    Onitr[0] = 0
                    Onitr[1] = 0
                    Onitr[2] = 0

        if Onitr[0]:
            pygame.draw.rect(screen, cols[0], rect0, 0)
        elif Onitr[1]:
            pygame.draw.rect(screen, cols[0], rect1, 0)
        elif Onitr[2]:
            pygame.draw.rect(screen, cols[0], rect2, 0)
        else:
            pygame.draw.rect(screen, cols[1], rect0, 0)
            pygame.draw.rect(screen, cols[1], rect1, 0)
            pygame.draw.rect(screen, cols[1], rect2, 0)
        screen.blit(txt_0, ((rect0.width - txt_0.get_width())//2 + rect0.left, (rect0.height - txt_0.get_height())//2 + rect0.top))
        screen.blit(txt_1, ((rect1.width - txt_1.get_width())//2 + rect1.left, (rect1.height - txt_1.get_height())//2 + rect1.top))
        screen.blit(txt_2, ((rect2.width - txt_2.get_width())//2 + rect2.left, (rect2.height - txt_2.get_height())//2 + rect2.top))
        screen.blit(page_title, ((screen.get_rect().width - page_title.get_width())//2 + page_title.get_rect().left,
                                 screen.get_rect().height//5))
        pygame.display.update()
        clock.tick(20)


if __name__ == '__main__':
    main_page()
