import curses
import time
import pathlib

from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.save_path = save_path

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for i in range(1, len(self.life.curr_generation) - 1):
            for j in range(1, len(self.life.curr_generation[i]) - 1):
                if self.life.curr_generation[i][j]:
                    condit = '*'
                else:
                    condit = ' '
                screen.addch(i, j, condit)

    def run(self) -> None:
        screen = curses.initscr().derwin(
            len(self.life.curr_generation), len(self.life.curr_generation[0]), 0, 0
        )
        curses.curs_set(0)
        running = True
        while running:
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            self.life.step()

            if self.life.max_generation_over:
                running = False
            screen.refresh()
            
        screen.getch()
        curses.endwin()
        
if __name__ == "__main__":
    life = GameOfLife((15, 30), randomize = True)
    ui = Console(life, save_path=pathlib.Path("fileui.txt"))
    ui.run()
