import pathlib
import random
from random import randint
import typing as tp
import pygame

from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        array = []
        weight = self.rows
        height = self.cols
        if randomize == True:
            for i in range(weight):
                array.append([])
                for j in range(height):
                    array[i].append(random.randint(0, 1))
        else:
            for i in range(weight):
                array.append([])
                for j in range(height):
                    array[i].append(0)
        return array

    def get_neighbours(self, cell: Cell) -> Cells:
        gen = self.curr_generation
        i1 = cell[0]
        j1 = cell[1]
        neighbours = []
        for i in range(i1 - 1, i1 + 2):
            for j in range(j1 - 1, j1 + 2):
                if i >= 0 and j >= 0 and i < self.rows and j < self.cols:
                    if i1 == i and j1 == j:
                        None
                    else:
                        neighbours.append(gen[i][j])
        return neighbours

    def get_next_generation(self) -> Grid:
        gen = self.curr_generation
        new_gen = [[0 for j in range(len(gen[i]))] for i in range(len(gen))]
        for i in range(self.rows):
            for j in range(self.cols):
                arr = self.get_neighbours((i, j))
                if gen[i][j] == 1:
                    if (sum(arr) < 2 or sum(arr) > 3):
                        new_gen[i][j] = 0
                    else:
                        new_gen[i][j] = 1
                elif gen[i][j] == 0 and sum(arr) == 3:
                    new_gen[i][j] = 1
                else:
                    new_gen[i][j] = gen[i][j]
        self.curr_generation = new_gen
        return self.curr_generation

    def step(self) -> None:
        '''
        Выполнить один шаг игры.
        '''
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

        return self.curr_generation
        

    @property
    def is_max_generations_exceeded(self) -> bool:
        '''
        Не превысило ли текущее число поколений максимально допустимое.
        '''

        if self.generations >= self.max_generations:
            return True
        else:
            return False
        

    @property
    def is_changing(self) -> bool:
        '''
        Изменилось ли состояние клеток с предыдущего шага.
        '''

        if self.prev_generation == self.curr_generation:
            return False
        else:
            return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        '''
        Прочитать состояние клеток из указанного файла.
        '''

        with open('grid.txt', 'r') as f:
            arr = [i.split() for i in f]
            arr1 = [list(str(arr[i][0])) for i in range(len(arr))]
            arr2 = [[int(j) for j in arr1[i]] for i in range(len(arr1))]
            return arr2
        

    def save(self, filename: pathlib.Path) -> None:
        '''
        Сохранить текущее состояние клеток в указанный файл.
        '''

        find = open('saves.txt', 'w')
        num = [''.join(map(str, self.curr_generation[i])) for i in range(len(self.curr_generation))]
        num1 = '\n'.join(num)
        find.write(str(num1))
        find.close()
                   
        
life = GameOfLife((5, 5))
print(life.curr_generation)
print(life.from_file('grid.txt'))
print(life.save('saves.txt'))

'''
life = GameOfLife.from_file('glider.txt') 
print(life.curr_generation)
for _ in range(4):
    life.step()
print(life.curr_generation)
life.save(pathlib.Path('glider-4-steps.txt'))
'''
