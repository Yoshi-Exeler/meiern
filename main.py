from model import *
from iodevices import *

gc = GameConfig()
gc.PlayerLimit = 3
g = Game(gc)
drv = CLI()
p1 = Player("Bob",drv)
drv2 = CLI()
p2 = Player("Alice",drv2)
p3 = Player("Dieter",drv2)
g.AddPlayer(p1)
g.AddPlayer(p2)
g.AddPlayer(p3)
g.Start()
