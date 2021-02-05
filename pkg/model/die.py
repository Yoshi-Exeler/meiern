from random import randrange

class Die:
    __sides: int

    def __init__(self,sides) -> None:
        self.__sides = sides

    def Roll(self) -> int:
        return randrange(1,self.__sides)