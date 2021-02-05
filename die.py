from random import randrange

class Die:
    __sides: int
    __value: int

    def __init__(self,sides) -> None:
        self.__sides = sides

    def Roll(self) -> int:
        self.__value = randrange(1,self.__sides)
        return self.__value