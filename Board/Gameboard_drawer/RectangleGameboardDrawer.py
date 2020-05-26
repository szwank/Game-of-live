from AbstractGameboardDrawer import AbstractGameboardDrawer
from math import floor
from Rectangle import Rectangle
from Field import Field
from GeometricTransformer import GeometricTransformer
from Gameboard import Gameboard

class RectangleGameboardDrawer(AbstractGameboardDrawer):
    def __init__(self, gameboard: Gameboard, gameboard_position: Rectangle):
        super(RectangleGameboardDrawer, self).__init__(gameboard, gameboard_position)
        self.field_height = self.__get_field_height()
        self.field_width = self.__get_field_width()
        self.height_in_fields = gameboard.height_in_fields
        self.width_in_fields = gameboard.width_in_fields
        self.gameboard_translation_vector = self.__get_gameboard_translation_vector()

    def __get_display(self):


    def __get_field_height(self):
        return floor(self._gameboard_position.heigt / self._gameboard.height_in_fields)

    def __get_field_width(self):
        return floor(self._gameboard_position.width / self._gameboard.width_in_fields)

    def __get_gameboard_translation_vector(self):
        gameboard_upper_left_corner = self._gameboard_position.lower_left_corner
        return gameboard_upper_left_corner.x, gameboard_upper_left_corner.y

    def _draw_field(self, field: Field):
        field_translation_vector = self.__get_field_translation_vector(field)
        translated_field_position = GeometricTransformer.translate_rectangle(field.position, field_translation_vector)
        self._display.rectangle(translated_field_position)


    def __get_field_translation_vector(self, field):
        x_translation = self.field_height * field.horizontal_position_in_fields - round(self.field_height / 2) + self.gameboard_translation_vector[0]
        y_translation = self.field_width * field.vertical_position_in_fields - round(self.field_width / 2) + self.gameboard_translation_vector[1]
        return x_translation, y_translation

    def _get_gameboard_height_in_pixels(self):
        return self._gameboard.height_in_fields * self.field_height

    def _get_gameboard_width_in_pixels(self):
        return self._gameboard.width_in_fields * self.field_height