from Animal import Animal


class Wolf(Animal):
    def __init__(self, field, gameboard):
        strength = 9
        initiative = 5
        super(Animal, self).__init__(strength=strength, initiative=initiative, field=field, gameboard=gameboard)

