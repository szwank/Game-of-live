from typing import Tuple


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def position(self) -> Tuple[int, int]:
        return (self.x, self.y)