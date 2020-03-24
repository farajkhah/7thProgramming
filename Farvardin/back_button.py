import defines as df
import main as mp
import First_page as fp
import Second_page as sp
import Game_page as gp


def back(screen, font):
    df.page_pointer -= 1
    if df.page_queue[df.page_pointer] == "main":
        mp.main_page()
    elif df.page_queue[df.page_pointer] == "first":
        fp.first_page(screen, font)
    elif df.page_queue[df.page_pointer] == "second":
        sp.second_page(screen, font)
    else:
        gp.game_page(screen, font)
