from model import *
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
        print("Hello",p.GetName(),"it is your turn!")
        print("This is the First Turn of the Game, you need to roll the dice!")
        input()
        g.Roll()
        print("You Rolled",g.GetState().GetValue(),"What would you like to pass this as?")
        inpLabel = self.__getLabel(g,p)
        g.Pass(inpLabel)
        print("You Passed as",inpLabel)
        g.PassTurn()
    
    @overrides
    def OnBeginTurn(self, g: Game, p: Player):
        self.__clear()
        print("Hello",p.GetName(),"it is your turn!")
        print("You Recieved some dice from",g.GetLastPlayer().GetName(),"he says its a",g.GetLabel())
        print("What do you do? (Options: 'pass', 'challenge, 'roll')")
        self.__getSelection(g,p)

    # Gets the Input from the Console, until a valid number between 21 and 66 or 11 was entered
    def __getLabel(self,g: Game,p: Player):
        conv = 0
        while True:
            raw = input()
            conv = 0
            try:
                conv = int(raw)
                if self.__isValidLabel(conv) != True:
                    raise ValueError("invalid label")
                return conv
            except:
                print("Invalid input, please enter a Number between 21 and 66!")
    
    #isValidLabel will check wether or not this label can exist
    def __isValidLabel(self,inp):
        # Convert inp to a string
        inpstr = ""
        try:
            inpstr = str(inp)
        except:
            return False
        # Check that the Length is 2
        if len(inpstr) != 2:
            return False
        # Convert the First and Last Digit back to ints
        dig1 = 0
        dig2 = 0
        try:
            dig1 = int(inpstr[0])
            dig2 = int(inpstr[1])
        except:
            return False
        print(dig1,dig2)
        # Check that each digit is from 1-6
        if dig1 > 6 or dig1 < 1:
            return False
        if dig2 > 6 or dig2 < 1:
            return False
        # Check that digit one is larger than digit two
        if dig1 < dig2:
            return False
        # if we have reached this point the label must be valid
        return True
        

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
            print("Your Challenge was Successfull, it was a",g.GetState().GetValue(),"",g.GetLastPlayer().GetName()," Loses one point and is now at",g.GetLastPlayer().GetScore(),"Points")
            print(g.GetActivePlayer().GetName(),"gains one point and is now at",g.GetActivePlayer().GetScore())
            self.__handleRoll(g,p)
        else:
            g.GetLastPlayer().IncrementScore()
            g.GetActivePlayer().DecrementScore()
            print("Your Challenge was not Successfull, it was a",g.GetState().GetValue(),"",g.GetLastPlayer().GetName()," Gains one point and is now at",g.GetLastPlayer().GetScore(),"Points")
            print(g.GetActivePlayer().GetName,"looses one point and is now at",g.GetActivePlayer().GetScore())
            self.__handleRoll(g,p)

    def __handlePass(self,g: Game,p: Player):
        print("As what would you like to pass the dice?")
        inpLabel = self.__getLabel(g,p)
        # The Player must say a higher number
        if Dice.Bigger(g.GetLabel(),inpLabel):
            print("You have to claim a higher number")
            self.__handlePass(g,p)
        g.Pass(inpLabel)
        print("You Passed as",inpLabel)
        g.PassTurn()
        
    def __handleRoll(self,g: Game,p: Player):
        g.Roll()
        print("You Reroll the Dice and get",g.GetState().GetValue())
        self.__handlePass(g,p)
