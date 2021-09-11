#-------------------------------------------------------------------------------
# Name:        ConsoleGameEngine
# Purpose:     Python Game Engine for console
#
# Author:      Mizu
#
# Created:     10/09/2021
# Copyleft:    Mizu 2021
# Licence:     GPLv3
#-------------------------------------------------------------------------------

from time import time
from math import *
from sys import stdout
from os import system
from os import name as osname

class ConsoleGame:
    def __init__(self, name="Untitled", w=80, h=25):
        self.name = name
        self.w = w
        self.h = h
        self.updatenum = -1
        self.framenum = -1
        self.ingame = False
        self.savelocation = None
        self.starttime = 0
        self.lastupdatetime = 0

    def clear(self):
        system('cls' if osname == 'nt' else 'clear')

    def printXY(self, text, x, y):
        stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
        stdout.flush()

    def current_milli_time(self):
        return time() * 1000

    def gettime(self):
        return self.current_milli_time() - self.starttime

    def event_load(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass

    def event_quit(self):
        pass

    def quit(self):
        self.ingame = False
        self.event_quit()

    def mainloop(self):
        self.ingame = True
        self.starttime = self.current_milli_time()
        self.lastupdatetime = self.starttime
        self.event_load()
        while self.ingame:
            self.updatenum += 1
            self.update(self.gettime() - self.lastupdatetime)
            self.lastupdatetime = self.gettime()
            self.framenum += 1
            self.draw()


def main():
    class MyGame(ConsoleGame):
        def update(self, dt):
            self.dt = dt

        def draw(self):
            print(self.updatenum, self.framenum, self.gettime(), (self.updatenum+1)/(max(self.gettime(), 1)/1000), self.dt)

    my_game = MyGame()
    my_game.mainloop()

if __name__ == '__main__':
    main()
