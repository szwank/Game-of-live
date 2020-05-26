from GameboardSetupInterface import GameboardSetupInterface
from abc import abstractmethod
import pygame
from Point import Point
from Rectangle import Rectangle
from typing import List
from Field import Field

class Gameboard(GameboardSetupInterface):

    def __init__(self, height_in_fields: int, width_in_fields: int):

        self.__height_in_fields = height_in_fields
        self.__width_in_fields = width_in_fields
        self.__fields = self.__create_board()


    def __create_board(self):
        fields = []

        for height_position in range(self.__height_in_fields):
            row = []

            for width_position in range(self.__width_in_fields):
                row.append(Field(height_position, width_position))

            fields.append(row)

        return fields

    @property
    def fields(self):
        return self.__fields

    @property
    def height_in_fields(self):
        return self.__height_in_fields

    @property
    def width_in_fields(self):
        return self.__width_in_fields
