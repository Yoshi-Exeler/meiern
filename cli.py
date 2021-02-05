from player import Player
from inputinterface import InputInterface
from game import Game
from override import overrides

class CLI(InputInterface):

    def __init__(self) -> None:
        pass

    @overrides
    def OnBeginTurn(self, g: Game,p: Player) -> None:
        return super().OnBeginTurn(g)

    @overrides
    def OnJoinGame(self, g: Game,p: Player) -> None:
        return super().OnJoinGame(g)

    @overrides
    def OnRolled(self, g: Game,p: Player) -> None:
        return super().OnRolled(g)

