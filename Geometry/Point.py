from typing import Tuple


class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def position(self) -> Tuple[int, int]:
        return self.__x, self.__y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y