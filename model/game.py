from model.gameconfig import *
from model.die import *
from model.dice import *
from model.player import *
from random import randrange
from subprocess import call

class Game:
    __config: GameConfig
    __players = []
    __active_player: Player
    __last_player: Player
    __label: int
    __state: Dice

    def __init__(self, c):
        self.__config = c

    # Resets the Entire Game State
    def __resetGame(self):
        self.__active_player = None
        self.__players = None
        self.__label = None
        self.__state = None

    # Pass turn to the Next Player in the Turncycle
    def PassTurn(self): 
        self.__last_player = self.__active_player
        idx = self.__players.index(self.__active_player)
        self.__active_player = self.__players[(idx+1) % len(self.__players)]
        self.__active_player.GetDriver().OnBeginTurn(self,self.__active_player)

    # Public API

    # Adds a Player to the Game
    def AddPlayer(self, p):
        self.__players.append(p)

    # Checks wether or not the Current label is equivalent to the current state
    def Challenge(self):
        return self.__label != self.__state

    # Pass will pass the Turn to the Next Player, with the label now being val
    def Pass(self, val):
        self.__label = val

    # Roll will reroll the Dice
    def Roll(self):
        self.__state.Roll()
        return self.__state

   # Initialize the Game and Set the Active Player at random
    def Start(self):
        # Init Fields
        self.__label = 0
        d1 = Die(6)
        d2 = Die(6)
        self.__state = Dice([d1, d2])
        # Pick Random First Player
        self.__active_player = self.__players[randrange(
            0, len(self.__players))]
        # Prompt the first player
        self.__active_player.GetDriver().OnBeginGame(self,self.__active_player)

    #GET/SET
    def GetState(self):
        return self.__state

    def GetActivePlayer(self):
        return self.__active_player

    def GetLastPlayer(self):
        return self.__last_player

    def GetLabel(self):
        return self.__label
