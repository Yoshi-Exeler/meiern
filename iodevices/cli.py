from model.game import *
from model.player import *
from util.override import *
from iodevices.iodriver import *
import os


class CLI(IODriver):

    def __init__(self):
        pass

    def __clear(self):
        os.system('cls' if os.name=='nt' else 'clear')

    @overrides
    def OnBeginGame(self, g: Game, p: Player):
        print("Hello ",p.GetName()," it is your turn!")
        print("This is the First Turn of the Game, you need to roll the dice!")
        input()
        g.Roll()
        print("You Rolled ",g.GetState().GetValue()," What would you like to pass this as?")
        inpLabel = int(input())
        g.Pass(inpLabel)
        print("You Passed as",inpLabel)
        g.PassTurn()
    
    @overrides
    def OnBeginTurn(self, g: Game, p: Player):
        self.__clear()
        print("Hello ",p.GetName()," it is your turn!")
        print("You Recieved some dice from",g.GetLastPlayer().GetName()," he says its a",g.GetLabel())
        print("What do you do? (Options: 'pass', 'challenge, 'roll')")
        self.__getSelection(g,p)

    def __getSelection(self,g: Game,p: Player):
        inp = input()
        if inp == 'challenge':
           self.__handleChallenge(g,p)
        if inp == 'pass':
            self.__handlePass(g,p)
        if inp == 'roll':
            self.__handleRoll(g,p)
        print("Unknown Input, please Try Again")
        self.__getSelection(g,p)

    def __handleChallenge(self,g: Game,p: Player):
        print("You Challenge the Word of",g.GetLastPlayer().GetName())
        success = g.Challenge()
        if success:
            g.GetLastPlayer().DecrementScore()
            g.GetActivePlayer().IncrementScore()
            print("Your Challenge was Successfull",g.GetLastPlayer().GetName()," Loses one point and is now at",g.GetLastPlayer().GetScore(),"Points")
            print(g.GetActivePlayer().GetName(),"gains one point and is now at",g.GetActivePlayer().GetScore())
            self.__handleRoll(g,p)
        else:
            g.GetLastPlayer().IncrementScore()
            g.GetActivePlayer().DecrementScore()
            print("Your Challenge was not Successfull",g.GetLastPlayer().GetName()," Gains one point and is now at",g.GetLastPlayer().GetScore(),"Points")
            print(g.GetActivePlayer().GetName,"looses one point and is now at",g.GetActivePlayer().GetScore())
            self.__handleRoll(g,p)

    def __handlePass(self,g: Game,p: Player):
        print("As what would you like to pass the dice?")
        inpLabel = int(input())
        g.Pass(inpLabel)
        print("You Passed as",inpLabel)
        g.PassTurn()
        
    def __handleRoll(self,g: Game,p: Player):
        g.Roll()
        print("You Reroll the Dice and get",g.GetState().GetValue())
        self.__handlePass(g,p)
