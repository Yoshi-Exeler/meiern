from model.game import *
from model.gameconfig import *
from model.player import *
from iodevices.cli import *

gc = GameConfig()
gc.PlayerLimit = 2
g = Game(gc)
drv = CLI()
p1 = Player("Bob",drv)
drv2 = CLI()
p2 = Player("Alice",drv2)
g.AddPlayer(p1)
g.AddPlayer(p2)
