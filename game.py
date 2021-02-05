from die import Die
from gameconfig import GameConfig
from player import Player
from dice import Dice
from random import randrange

class Game:
    __config: GameConfig
    __players: list[Player]
    __active_player: Player
    __label: int
    __state: Dice

    def __init__(self,c) -> None:
        self.__config = c

    # Adds a Player to the Game and Checks wether or not the game should now start,
    # if the game should now start, it will be started.
    def AddPlayer(self,p) -> None:
        if len(self.__players) == self.__config.PlayerLimit:
            return
        self.__players.append(p)
        if len(self.__players) == self.__config.PlayerLimit:
            self.__startGame()

    # Initialize the Game and Set the Active Player at random
    def __startGame(self) -> None:
        self.__label = 0
        d1 = Die()
        d2 = Die()
        self.__state = Dice([d1,d2])
        self.__active_player = self.__players[randrange(0,len(self.__players))]

    # Resets the Entire Game State
    def __resetGame(self) -> None:
        self.__active_player = None
        self.__players = None
        self.__label = None
        self.__state = None

    # Pass turn to the Next Player in the Turncycle
    def __passTurn(self) -> None:
        idx = self.__players.index(self.__active_player)
        self.__active_player = self.__players[(idx+1) % len(self.__players)]

    # Checks wether or not the Current label is equivalent to the current state
    def Challenge(self) -> bool:
        return self.__label != self.__state

    # Pass will pass the Turn to the Next Player, with the label now being val
    def Pass(self, val) -> None:
        self.__label = val
        self.__passTurn()

    def Roll(self) -> None:
        pass