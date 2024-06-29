from window import Point, Line


class Cell:
    def __init__(self, hlwall, hrwall, htwall, hbwall, x1, x2, y1, y2, win):
        self.hlwall = hlwall
        self.hrwall = hrwall
        self.htwall = htwall
        self.hbwall = hbwall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.win = win
        self.visited = False

    def draw(self):
        c1 = Point(self.__x1, self.__y1)
        c2 = Point(self.__x2, self.__y1)
        c3 = Point(self.__x1, self.__y2)
        c4 = Point(self.__x2, self.__y2)
        top = Line(c1, c2)
        left = Line(c1, c3)
        right = Line(c2, c4)
        bot = Line(c3, c4)
        if self.hlwall:
            self.win.draw_line(left, "black")
        if self.hrwall:
            self.win.draw_line(right, "black")
        if self.htwall:
            self.win.draw_line(top, "black")
        if self.hbwall:
            self.win.draw_line(bot, "black")
        if self.hlwall is False:
            self.win.draw_line(left, "white")
        if self.hrwall is False:
            self.win.draw_line(right, "white")
        if self.htwall is False:
            self.win.draw_line(top, "white")
        if self.hbwall is False:
            self.win.draw_line(bot, "white")

    def draw_move(self, to_cell, undo=False):
        ccent1 = Point(calc_mid(self.__x1, self.__x2),
                       calc_mid(self.__y1, self.__y2))
        ccent2 = Point(calc_mid(to_cell.__x1, to_cell.__x2),
                       calc_mid(to_cell.__y1, to_cell.__y2))
        connect = Line(ccent1, ccent2)
        if undo is False:
            self.win.draw_line(connect, "red")
        else:
            self.win.draw_line(connect, "gray")


def calc_mid(n1, n2):
    if n1 == n2:
        return n1
    if n1 < n2:
        return n1 + abs(n2-n1)/2
    if n1 > n2:
        return n2 + abs(n1-n2)/2
