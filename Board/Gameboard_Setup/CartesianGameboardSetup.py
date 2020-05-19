from Geometry.Point import Point
from GameboardSetup import GameboardSetup
from Rectangle import Rectangle
from math import floor
from RectangleField import RectangleField
from GeometricFactory import GeometricFactory
from GeometricTransformator import GeometricAbstractTransformator

class CartesianGameboardSetup(GameboardSetup):
    def __init__(self, board, position: Rectangle, height_in_fields: int, width_in_fields: int, line_thickness: int = 1):
        super().__init__(board, position, height_in_fields, width_in_fields, line_thickness)

        self.field_height = self.__get_field_height()
        self.field_width = self.__get_field_width()

    def __get_field_height(self):
        return floor(self.position.height / self.height_in_fields)

    def __get_field_width(self):
        return floor(self.position.width / self.width_in_fields)

    def _draw_fields(self):
        for field in self.fields:
            field.draw()
            self._update_board()

    def _init_fields(self):
        for row_number in range(self.height_in_fields):
            self.__create_row_of_fields(row_number)

    def __create_row_of_fields(self, row_number):
        for column_number in range(self.width_in_fields):
            field_center = self.__get_field_center(column_number, row_number)
            field = RectangleField(self.board, field_center, self.field_height, self.field_width, self.line_thickness)
            self.fields.append(field)

    def __get_field_center(self, column_number, row_number):
        lower_left_corner = GeometricAbstractTransformator().get_lower_left_corner(self.position)
        x = lower_left_corner.x + round(self.field_width / 2) + self.field_width * row_number
        y = lower_left_corner.y + round(self.field_height / 2) + self.field_height * column_number
        return Point(x, y)

