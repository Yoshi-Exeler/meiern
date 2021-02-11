class Player:
    __name: str
    __driver: None
    __score: int

    def __init__(self,n,d):
        self.__name = n
        self.__score = 0
        self.__driver = d

    def GetName(self):
        return self.__name

    def GetDriver(self):
        return self.__driver

    def DecrementScore(self):
        self.__score -= 1

    def IncrementScore(self):
        self.__score += 1

    def GetScore(self):
        return self.__score

