from abc import ABC, abstractmethod 
from random import randint
from typing import Protocol

class Node(ABC):
    """ABC that all nodes in grid have"""
    @abstractmethod
    def consume(self) -> float:
        """The reward for landing on the node can be positive or negative"""

    @abstractmethod
    def solid(self) -> bool:
        """Indicates whether player can stand on space"""

    @abstractmethod
    def __str__(self) -> chr:
        """Will be character on board"""

    def reward(self) -> float:
        return self.__value

class Coin(Node):
    """They provide 5 reward"""
    __value: float = 5

    def consume(self) -> float:
        if self.__value  > 0:
            self.__value = 0
            return self.__value
        return 0
    
    def solid(self) -> bool:
        return False

    def __str__(self) -> chr:
        return 'C' if self.__value > 0 else str(Empty())

class Inferno(Node):
    __value: float = -20

    def consume(self) -> float:
        return self.__value

    def solid(self) -> bool:
        return False
    
    def __str__(self) -> chr:
        return 'I'

class Wall(Node):
    __value: float = 0

    def consume(self) -> float:
        return 0

    def solid(self) -> bool:
        return True

    def __str__(self) -> chr:
        return '|'

class Empty(Node):
    __value: float = 0

    def consume(self) -> float:
        return 0

    def solid(self) -> bool:
        return False

    def __str__(self) -> chr:
        return '_'

def nodeFactory(empty: bool) -> Node:
    roll = randint(1,10)
    if empty:
        return Empty()
    if roll == 1:
        return Wall()
    if roll == 2:
        return Inferno()
    if roll == 3:
        return Coin()
    return Empty()

class EnvironmentMarker(Protocol):

    @abstractmethod
    def getPosition(self) -> tuple:
        """Returns tuple of where to draw marker"""

    @abstractmethod
    def __str__(self) -> str:
        """Character to draw for marker"""

class Environment:
    """Enviroment that algo will explore"""
    __grid: list
    __player: EnvironmentMarker

    def __init__(self, width, height, player: EnvironmentMarker) -> None:
        self.__grid = [[ nodeFactory(row < 2 and col < 2 ) for col in range(width)] for row in range(height) ]
        self.__player = player

    def get(self, col: int, row: int) -> Node:
        return self.__grid[row][col]

    def width(self) -> int:
        return len(self.__grid[0])

    def height(self) -> int:
        return len(self.__grid)

    def __str__(self) -> str:
        o = ""
        for ri, row in enumerate(self.__grid):
            for ci, cell in enumerate(row):
                if (ci, ri) == self.__player.getPosition():
                    o += str(self.__player)
                else:
                    o += str(cell)
            o += "\n"
        return o 

    def __repr__(self) -> str:
        return str(self)
                      