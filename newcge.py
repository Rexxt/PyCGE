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

    def _resize(self, w, h):
        if osname == 'nt':
            system(f"mode {w} {h}")
        else:
            stdout.write(f"\x1b[8;{h};{w}t")

    def _title(self, t):
        if osname == 'nt':
            system(f"title {t}")
        else:
            system(f'echo -en "\033]0;{t}\a"')

    def current_ms_time(self):
        return time() * 1000

    def gettime(self):
        return self.current_ms_time() - self.starttime

    def load(self):
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
        self._title(self.name)
        self._resize(self.w, self.h)
        self.starttime = self.current_ms_time()
        self.lastupdatetime = self.starttime
        self.load()
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
