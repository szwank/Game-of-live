from GameboardDisplay import GameboardDisplay
from Display import Display
from Point import Point
from Field import Field
from typing import Dict
from CreatureDisplayFactory import CreatureDisplayFactory
from utils import print_time

class RectangleFieldGameboardDisplay(GameboardDisplay):
    def __init__(self, upper_left_corner_gameboard_position: Point, height_in_pixels: int,
                 width_in_pixels: int):
        super(RectangleFieldGameboardDisplay, self).__init__(upper_left_corner_gameboard_position, height_in_pixels,
                                                             width_in_pixels)
        self.field_height = None
        self.field_width = None

    def display(self, gameboard):
        fields = gameboard.fields
        self.field_height = self._calculate_field_height(gameboard.height_in_fields)
        self.field_width = self._calculate_field_width(gameboard.width_in_fields)
        creatures = gameboard.creatures

        self.__display_fields(fields)

        for creature in creatures:
            upper_left_corner = self.__get_field_upper_left_corner(creature.field)
            creature_drawer = CreatureDisplayFactory.get_creature_drawer(creature)
            creature_drawer(upper_left_corner, self.field_height, self.field_width)

    def __display_fields(self, fields: Dict):
        for field in fields.values():
            upper_left_corner = self.__get_field_upper_left_corner(field)
            self.__display_field(upper_left_corner)

    def __get_field_upper_left_corner(self, field: Field):
        x = self.__get_upper_left_corner_field_x_position(field, self.field_width)
        y = self.__get_upper_left_corner_field_y_position(field, self.field_height)
        upper_left_corner = Point(x, y)
        return upper_left_corner

    def __get_upper_left_corner_field_x_position(self, field: Field, field_width: int):
        return field_width * field.horizontal_position_in_fields + self._upper_left_corner_gameboard_position.x

    def __get_upper_left_corner_field_y_position(self, field: Field, field_height: int):
        return self._upper_left_corner_gameboard_position.y - self.height_in_pixels +\
               field_height * field.vertical_position_in_fields

    def __display_field(self, upper_left_corner: Point):
        Display.rectangle(upper_left_corner, self.field_height, self.field_width)