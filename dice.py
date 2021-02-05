from die import Die

class Dice:
    __dice: list[Die]

    def __init__(self,dice) -> None:
        self.__dice = dice

    def Roll(self) -> None:
        for die in self.__dice:
            die.Roll()

