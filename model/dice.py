class Dice:
    __dice = []

    def __init__(self, dice):
        self.__dice = dice

    def Roll(self):
        for die in self.__dice:
            die.Roll()

    def GetValue(self):
        if len(self.__dice) != 2:
            raise IndexError("model-dice-getvalue-1:DICE_LENGTH_UNSUPPORTED")
        prim = max(self.__dice[0].GetValue(), self.__dice[1].GetValue())
        sec = min(self.__dice[0].GetValue(), self.__dice[1].GetValue())
        return 10*prim+sec

    @staticmethod
    def Bigger(a: int, b:int):
        if a != b:
            if a == 21:
                return True
            if b == 21:
                return False
            return a > b
        return False