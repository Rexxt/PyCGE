import pycge
import newcge
import sys

class Game(pycge.PyConsoleGame):
    def __init__(self):
        super(Game, self).__init__()
        self.name = "PyCGE Example"
    
    def create(self):
        pycge.clear()

    def update(self, dt):
        self.dt = dt

    def draw(self):
        pycge.clear()
        pycge.printXY(f'{self.timer};{self.dt}',self.timer/1000+1,1)

class MyGame(newcge.ConsoleGame):
    def load(self):
        self.clear()

    def update(self, dt):
        self.dt = dt

    def draw(self):
        self.clear()
        self.printXY(f'{self.gettime()};{self.dt}',self.gettime()/1000+1,1)

if sys.argv[1] == "old":
    game = Game()
    game.start()
elif sys.argv[1] == "new":
    game = MyGame()
    game.mainloop()
else:
    print("example.py <old|new>")