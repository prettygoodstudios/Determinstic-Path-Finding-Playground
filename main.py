


from abc import ABC 
from env import Environment

class PathFindingStrategy(ABC):
    def findPath(enviroment: Environment, position: tuple) -> list:
        """Where path finding algorithm code will go takes an enviroment and a position"""

class ARAStrategy(PathFindingStrategy):
    def findPath(enviroment: Environment, position: tuple) -> list:
        """Where ARA path finding code will go"""

class Player:
    __x: int = 0
    __y: int = 0

    def play(self, pathFindingStategy: PathFindingStrategy) -> None:
        """Where will put player movement logic"""

    def getPosition(self) -> tuple:
        return (self.__x, self.__y)

    def __str__(self) -> str:
        return 'P'


if __name__ == "__main__":
    enviroment = Environment(30, 30, Player())
