import keyboard
import sys
import os
import time
import cursor
import atexit
import math

atexit.register(cursor.show)

def getCurrentTime():
    return time.time() * 1000

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printXY(text, x, y):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
    sys.stdout.flush()

class PyConsoleGame:
    def __init__(self):
        self.name = "Python Console Game Engine"
        self.size = [80, 30]
        self.saveLocation = None
        self.inGame = False
        self.timer = 0
        self.startTime = 0

    def create(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass

    def quit(self):
        self.inGame = False
        cursor.show()

    def start(self):
        cursor.hide()
        self.inGame = True
        self.startTime = time.time() * 1000
        if os.name == 'nt':
            os.system(f'title {self.name}')
            #os.system(f'mode {self.size[0]} {self.size[1]}')
        self.create()
        while self.inGame:
            prTimer = self.timer
            self.timer = time.time() * 1000 - self.startTime
            self.update(self.timer - prTimer)
            self.draw()