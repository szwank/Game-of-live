

class Field:

    def __init__(self, horizontal_position_in_fields, vertical_position_in_fields):
        self.__vertical_position_in_fields = vertical_position_in_fields
        self.__horizontal_position_in_fields = horizontal_position_in_fields
        self.__occupied_by = None

    def get_occupant(self):
        return self.__occupied_by

    def occupy(self, occupant):
        self.__occupied_by = occupant

    def set_free(self):
        self.__occupied_by = None

    def is_occupied(self):
        return self.__occupied_by is not None

    def is_free(self):
        return self.__occupied_by is None

    @property
    def position(self):
        return self.__horizontal_position_in_fields, self.__vertical_position_in_fields

    @property
    def vertical_position_in_fields(self):
        return self.__vertical_position_in_fields

    @property
    def horizontal_position_in_fields(self):
        return self.__horizontal_position_in_fields