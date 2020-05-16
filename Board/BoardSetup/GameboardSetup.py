from abc import ABC, abstractmethod

class GameboardSetup(ABC):
    """Define BoardCreators interface"""

    @abstractmethod
    def create_board(self):
        pass

    @abstractmethod
    def get_board(self):
        pass
