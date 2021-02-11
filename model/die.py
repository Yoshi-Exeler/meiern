from random import randrange

class Die:
    __sides: int
    __value: int

    def __init__(self, sides):
        self.__sides = sides

    def Roll(self):
        self.__value = randrange(1, self.__sides)

    def GetValue(self):
        return self.__value
