from model import *

class IODriver:

    def __init__(self,):
        raise NotImplementedError()

    def OnBeginGame(self,g:Game,p:Player):
        raise NotImplementedError()

    def OnBeginTurn(self, g: Game, p: Player):
        raise NotImplementedError()