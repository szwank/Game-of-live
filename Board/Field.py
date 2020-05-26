from FieldInterface import FieldInterface
from Rectangle import Rectangle

class Field(FieldInterface):

    def __init__(self, height_in_fields, width_in_fields):
        self.__vertical_position_in_fields = height_in_fields
        self.__horisontal_position_in_fields = width_in_fields
        self.__occupied_by = None

    def get_occupant(self):
        return self.__occupied_by

    def occupy(self, occupant):
        self.__occupied_by = occupant

    @property
    def position(self):
        return self.__vertical_position_in_fields, self.__horisontal_position_in_fields

    @property
    def vertical_position_in_fields(self):
        return self.__vertical_position_in_fields

    @property
    def horizontal_position_in_fields(self):
        return self.__horisontal_position_in_fields