from window import Window
from maze import Maze


def main():
    win = Window(800, 600)
    # p1 = Point(100, 300)
    # p2 = Point(700, 400)
    # p3 = Point(350, 150)
    # p4 = Point(800, 500)
    # cella = Cell(True, True, True, True, p1.x, p2.x, p1.y, p2.y, win)
    # cellb = Cell(True, True, True, True, p3.x, p4.x, p3.y, p4.y, win)
    m1 = Maze(20, 20, 15, 15, 20, 20, win)
    m1.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
