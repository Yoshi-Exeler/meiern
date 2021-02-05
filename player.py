from typing import ByteString


class Player:
    __name: str
    __score: int

    def __init__(self,n) -> None:
        self.__name = n
        self.__score = 0

    def OnBeginTurn(self) -> None:
        pass

    def GetName(self) -> str:
        return self.__name