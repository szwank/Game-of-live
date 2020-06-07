from Gameboard import Gameboard


class Board:
    def __init__(self, gameboard: Gameboard, console_height: int = 300):
        self.height_in_fields = gameboard.height_in_fields
        self.width_in_fields = gameboard.width_in_fields
        self.console_height = console_height
        self.gameboard = gameboard

    # def __gameboard_height(self):
    #     return self.height_in_fields * self.field_height
    #
    # def __gameboard_width(self):
    #     return self.width_in_fields * self.field_width
    #
    # def __get_board_size(self) -> Tuple[int, int]:
    #     return (self.__get_board_width(), self.__get_board_height())
    #
    # def __get_board_width(self) -> int:
    #     return self.width_in_fields * self.field_width + 2 * self.gameboard_margin_width
    #
    # def __get_board_height(self) -> int:
    #     return self.height_in_fields * self.field_height + self.console_height + 2 * self.gameboard_margin_height

