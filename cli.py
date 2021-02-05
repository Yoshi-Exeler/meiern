from player import Player
from inputinterface import InputInterface
from game import Game
from override import overrides


class CLI(InputInterface):

    def __init__(self) -> None:
        pass

    @overrides
    def OnBeginTurn(self, g: Game, p: Player) -> None:
        print("Hello ",p.GetName()," it is your turn!")
        print("You Recieved some dice from ",g.GetLastPlayer().GetName()," , he say its ",g.__label)
        print("What do you do? (Options: 'pass', 'challenge, '')")
        inp = input()
        if inp == 'challenge':
            pass
        if inp == 'pass':
            pass
        if inp == 'roll':
            pass

    @overrides
    def OnJoinGame(self, g: Game, p: Player) -> None:
        return super().OnJoinGame(g)

    @overrides
    def OnRolled(self, g: Game, p: Player) -> None:
        return super().OnRolled(g)
