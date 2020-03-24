import pygame

class Polygon:
    def __init__(self):
        self.pos_list_x = []
        self.pos_list_y = []
        self.type_list = []
        self.spd_list = []
        self.dir_list = []
        self.scale_list = []
        self.col_list = []
        self.colors = [(0,0,0), (255,0,0), (255,255,0), (0,255,0)]

    def add_polygon(self, p_type, x, y, spd, col, scale):
        self.pos_list_x.append(x)
        self.pos_list_y.append(y)
        self.type_list.append(p_type)
        self.spd_list.append(spd)
        if x > 400 and y > 300:
            p_dir = (-1, -1)
        elif x > 400:
            p_dir = (-1, 1)
        elif y > 300:
            p_dir = (1, -1)
        else:
            p_dir = (1, 1)
        self.dir_list.append(p_dir)
        self.scale_list.append(scale)
        self.col_list.append(col)
        return len(self.pos_list_x)-1

    def del_polygon(self, loc):
        del self.pos_list_x[loc]
        del self.pos_list_y[loc]
        del self.type_list[loc]
        del self.spd_list[loc]
        del self.dir_list[loc]
        del self.scale_list[loc]
        del self.col_list[loc]
        return len(self.pos_list_x)-1

    def update_pos(self, loc):
        self.pos_list_x[loc] += int(self.spd_list[loc] * (self.dir_list[loc][0]))
        self.pos_list_y[loc] += int(self.spd_list[loc] * (self.dir_list[loc][1]))

        if self.pos_list_x[loc] > 800 or self.pos_list_y[loc] > 600 or self.pos_list_x[loc] < 0 or self.pos_list_y[loc] < 0:
            return loc-1, self.del_polygon(loc)
        else:
            return loc, len(self.pos_list_x)-1

    def draw_object(self, loc, screen):
        try:
            if self.type_list[loc] == 0:        #circle
                pygame.draw.circle(screen, self.colors[self.col_list[loc]], (self.pos_list_x[loc], self.pos_list_y[loc]),
                                   12 * self.scale_list[loc], 0)
            elif self.type_list[loc] == 1:        #square
                pygame.draw.rect(screen, self.colors[self.col_list[loc]], (self.pos_list_x[loc], self.pos_list_y[loc], 25 * self.scale_list[loc],
                                                     25 * self.scale_list[loc]), 0)
            elif self.type_list[loc] == 2:        #X
                pygame.draw.line(screen, self.colors[self.col_list[loc]], (self.pos_list_x[loc], self.pos_list_y[loc]),
                                 (self.pos_list_x[loc] + 50, self.pos_list_y[loc] + 50), 2)
                pygame.draw.line(screen, self.colors[self.col_list[loc]], (self.pos_list_x[loc] + 50, self.pos_list_y[loc]),
                                 (self.pos_list_x[loc], self.pos_list_y[loc] + 50), 2)
        except:
            print("")

