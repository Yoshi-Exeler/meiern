from die import Die


class Dice:
    __dice: list[Die]

    def __init__(self, dice) -> None:
        self.__dice = dice

    def Roll(self) -> None:
        for die in self.__dice:
            die.Roll()

    def GetValue(self) -> int:
        prim = max(self.__dice[0], self.__dice[1])
        sec = min(self.__dice[0], self.__dice[1])
        return 10*prim+sec

    def Bigger(self, other_dice) -> bool:
        return self.GetValue() > other_dice.GetValue()
