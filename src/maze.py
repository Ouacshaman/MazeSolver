from cell import Cell
import random as r


class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win,
                 seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.seed = seed
        if seed is not None:
            # seed makes sure random are fixed to a value
            self.seed = r.seed(self.seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def get_cells(self):
        return self.__cells

    def __create_cells(self):
        for i in range(self.num_cols):
            temp = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                temp.append(Cell(True, True, True, True,
                                 x1, x2, y1, y2, self.win))
            self.__cells.append(temp)
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self.__draw_cells(i, j)

    def __draw_cells(self, i, j):
        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self):
        self.win.redraw()
        self.win.schedule_task(50, self.__animate)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].htwall = False
        self.__draw_cells(0, 0)
        self.__cells[self.num_cols-1][self.num_rows-1].hbwall = False
        self.__draw_cells(self.num_cols-1, self.num_rows-1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            temp = []
            if j > 0 and self.__cells[i][j-1].visited is False:
                temp.append((i, j-1))
            if j < self.num_rows-1 and self.__cells[i][j+1].visited is False:
                temp.append((i, j+1))
            if i > 0 and self.__cells[i-1][j].visited is False:
                temp.append((i-1, j))
            if i < self.num_cols-1 and self.__cells[i+1][j].visited is False:
                temp.append((i+1, j))
            if not temp:
                self.__cells[i][j].draw()
                return
            else:
                next_i, next_j = temp[r.randint(0, len(temp)-1)]
                if next_i == i-1:
                    self.__cells[i][j].htwall = False
                elif next_i == i+1:
                    self.__cells[i][j].hbwall = False
                elif next_j == j-1:
                    self.__cells[i][j].hlwall = False
                elif next_j == j+1:
                    self.__cells[i][j].hrwall = False
                self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self.__cells[i][j].visited = False

    def solve(self):
        if self.__solve_r(0, 0):
            return True
        else:
            return False

    def __solve_r(self, i, j):
        end = self.__cells[self.num_cols-1][self.num_rows-1]
        self.__animate()
        self.__cells[i][j].visited = True
        if self.__cells[i][j] == end:
            return True
        if self.__cells[i][j].htwall is False and i > 0:
            self.__cells[i][j].draw_move(self.__cells[i-1][j], False)
            res = self.__solve_r(i-1, j)
            if res:
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i-1][j], True)
        if self.__cells[i][j].hbwall is False and i < self.num_cols-1:
            self.__cells[i][j].draw_move(self.__cells[i+1][j], False)
            res = self.__solve_r(i+1, j)
            if res:
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i+1][j], True)
        if self.__cells[i][j].hlwall is False and j > 0:
            self.__cells[i][j].draw_move(self.__cells[i][j-1], False)
            res = self.__solve_r(i, j-1)
            if res:
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j-1], True)
        if self.__cells[i][j].hrwall is False and j < self.num_rows-1:
            self.__cells[i][j].draw_move(self.__cells[i][j+1], False)
            res = self.__solve_r(i, j+1)
            if res:
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j+1], True)
        return False
