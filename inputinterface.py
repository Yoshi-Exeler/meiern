from game import Game
from player import Player


class InputInterface:

    def __init__(self) -> None:
        pass

    def OnBeginTurn(self, g: Game, p: Player) -> None:
        raise NotImplementedError()

    def OnRolled(self, g: Game, p: Player) -> None:
        raise NotImplementedError()

    def OnJoinGame(self, g: Game, p: Player) -> None:
        raise NotImplementedError()
