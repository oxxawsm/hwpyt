import abc

from life import GameOfLife


class UI(abc.ABC):
    def __init__(self, life: GameOfLife) -> None:
        self.life = life

    def run(self) -> None:
        pass
