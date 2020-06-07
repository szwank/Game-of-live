from Draw import Display


class WorldDisplay:
    def __init__(self, gameboard_display):
        self.__gameboard_display = gameboard_display

    def display(self, world):
        self.__display_board(world.board)

    def __display_board(self, board):
        self.__gameboard_display.display(board.gameboard)