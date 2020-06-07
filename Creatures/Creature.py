from abc import ABC, abstractmethod
from typing import Tuple
from Field import Field
# from Gameboard import Gameboard
import time

class Creature(ABC):
    def __init__(self, strength: int, initiative: int, field: Field, gameboard):
        self.__strength = strength
        self.__initiative = initiative
        self.__gameboard = gameboard
        self.__field = field
        self.__birthday = time.time()

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, aggressor):
        pass

    @property
    def position(self) -> Tuple:
        return self.__field.position

    @property
    def strength(self):
        return self.__strength

    @property
    def initiative(self):
        return self.__initiative

    @property
    def gameboard(self):
        return self.__gameboard

    @property
    def field(self):
        return self.__field

    @property
    def birthday(self):
        return self.__birthday

    def kill(self, creature):
        self.gameboard.kill(creature)