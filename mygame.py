import pycge

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

game = Game()
game.start()