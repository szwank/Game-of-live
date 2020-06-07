from Creature import Creature
from abc import abstractmethod


class Animal(Creature):
    def __init__(self, strength, initiative, field, gameboard):
        super(Animal, self).__init__(strength, initiative, field, gameboard)

    def action(self):
        self.__move()

    def __move(self):
        self.gameboard.move_creature(self)

    def collision(self, aggressor):
        if aggressor == self:
            self.__make_child()
        else:
            if aggressor.strangth < self.strength:
                aggressor.kill(self)
            else:
                self.kill(aggressor)

    def __make_child(self):
        self.gameboard.make_child(self)

    def set_field(self, field):
        self.__field = field