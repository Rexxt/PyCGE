# PyCGE
 Python-based console game engine

## Usage
### New version
#### Setting up project
* Place `newcge.py` in your project folder
* In your main file, write:
```py
from newcge import ConsoleGame
```
#### Making a game
Now, let's make a simple program that displays the game time and the time between updates.
* Create a class that extends `ConsoleGame`:
```py
class MyGame(ConsoleGame):
```
* Now, let's set up a load event:
```py
    def event_load(self):
        self.clear()
        self.dt = 0
```
* Now, let's add a really simple update event:
```py
    def update(self, dt):
        self.dt = dt
```
* And now, let's print the text to the console
```py
    def draw(self):
        self.clear()
        self.printXY(f'{self.gettime()};{self.dt}', self.gettime()/1000+1, 1)
```
* Instantiate the `MyGame` class and call its mainloop function:
```py
class MyGame(ConsoleGame):
    def load(self):
        self.clear()
        self.dt = 0

    def update(self, dt):
        self.dt = dt

    def draw(self):
        self.clear()
        self.printXY(f'{self.gettime()};{self.dt}', self.gettime()/1000+1, 1)

mygame = MyGame()
mygame.mainloop()
```
* Now, run your main file. You should see the game time in milliseconds followed by the time between updates in milliseconds.