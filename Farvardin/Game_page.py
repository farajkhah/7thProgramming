import Object_class as oc
import pygame
import random as rn
import sys


def game_page(screen,font):
    clock = pygame.time.Clock()
    obj = oc.Polygon()
    ps = -1
    finished = False
    page_title = font.render("Press Enter Repeatedly to Create Objects...", True, (0, 0, 255))

    while not finished:
        i = 0
        screen.fill((255, 255, 255))
        screen.blit(page_title, (0, 0))
        while i <= ps:
            obj.draw_object(i, screen)
            i, ps = obj.update_pos(i)
            i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = 1
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    scale = rn.randint(1, 4)
                    ps = obj.add_polygon(rn.randint(0, 3), rn.randint(0, screen.get_rect().width),
                                    rn.randint(0, screen.get_rect().height), rn.randint(4, 8),
                                    rn.randint(0, 4), scale)

        clock.tick(60)
        pygame.display.update()

    return