class Dice:
    __dice = []

    def __init__(self, dice):
        self.__dice = dice

    def Roll(self):
        for die in self.__dice:
            die.Roll()

    def GetValue(self):
        prim = max(self.__dice[0].GetValue(), self.__dice[1].GetValue())
        sec = min(self.__dice[0].GetValue(), self.__dice[1].GetValue())
        return 10*prim+sec

    def Bigger(self, other_dice):
        return self.GetValue() > other_dice.GetValue()
