import pygame
from pygame.locals import *

import life
from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int=10, speed: int=10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_size = self.life.cols * cell_size, self.life.rows * cell_size
        self.screen = pygame.display.set_mode(self.screen_size)
        

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))
            
        pass

    
    def draw_grid(self) -> None:
        for y in range(self.life.rows):
            for x in range(self.life.cols):
                if self.grid[y][x] == 0:
                    cell_color = [255, 255, 255] #white
                else:
                    cell_color = [0, 255, 0]     #green
                pygame.draw.rect(self.screen,
                                 cell_color,
                                 (
                                     x * self.cell_size + 1,
                                     y * self.cell_size + 1,
                                     self.cell_size - 1,
                                     self.cell_size - 1
                                 ))
                
            pass

        
    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        self.is_pause = False
        
        self.grid = self.life.create_grid(randomize = True)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.is_pause = not self.is_pause
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        cell = grid[event.pos[1] // self.cell_size][event.pos[0] // self.cell_size]
                        cell = 1 if cell == 0 else 0
                        grid[event.pos[1] // self.cell_size][event.pos[0] // self.cell_size] = cell
                if event.type == QUIT:
                    running == False
            if self.is_pause:
                self.draw_lines()
                self.draw_grid()
            else:
                grid = self.life.get_next_generation()
                self.draw_lines()
                self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
        
        
    
 def main():
     game = GameOfLife(size=(48, 64))
     application = GUI(game)
     application.run()
        
 
if __name__ == "__main__":
    main()
        
