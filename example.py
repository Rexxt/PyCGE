from time import sleep
import pycge
import newcge
import neocge
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

class MyNeoGame(neocge.ConsoleGame):
    def load(self):
        print(neocge.term.home + neocge.term.clear)

    def update(self, dt):
        self.dt = max(0, dt)

    def draw(self):
        self.buffer.clear_buffer()
        dt_height = int(self.dt)
        dt_height //= (self.dt // 10) * 10 + 1
        self.buffer.putstring_xy(f'{int(self.gettime())};{int(self.dt)}', self.gettime() // 100 + 1, dt_height)

if sys.argv[1] == "old":
    game = Game()
    game.start()
elif sys.argv[1] == "new":
    game = MyGame()
    game.mainloop()
elif sys.argv[1] == "neo":
    game = MyNeoGame()
    game.mainloop()
else:
    print("example.py <old|new|neo>")