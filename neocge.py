#-------------------------------------------------------------------------------
# Name:        ConsoleGameEngine
# Purpose:     Python Game Engine for console
#
# Author:      Mizu
#
# Created:     04/03/2021
# Copyleft:    Mizu 2021
# Licence:     GPLv3
#-------------------------------------------------------------------------------

from blessed import Terminal
from time import time
from math import *
from sys import stdout
from os import system
from os import name as osname
import cursor, atexit
atexit.register(cursor.show)

term = Terminal()

class Buffer: # terminal print tool
    def __init__(self):
        self.term_buffer = [[None for j in range(term.width)] for i in range(term.height)]
    
    def clear_buffer(self):
        self.term_buffer = [[None for j in range(term.width)] for i in range(term.height)]
    
    def putchar_xy(self, text, x, y, colour = term.normal, bold = False):
        x = int(x)
        y = int(y)
        
        if len(text) != 1:
            raise Exception(f'expected string of length 1, got string of length {len(text)}')
        
        if y < 0 or y >= len(self.term_buffer):
            raise Exception('Attempted to put string out of bounds.')
        
        if x < 0 or x >= len(self.term_buffer[y]):
            raise Exception('Attempted to put string out of bounds.')

        
        char = {
            'content': text,
            'colour': colour,
            'bold': bold
        }

        self.term_buffer[y][x] = char
    
    def putstring_xy(self, text, x, y, colour = term.normal, bold = False):
        x = int(x)
        y = int(y)

        if y < 0 or y >= len(self.term_buffer):
            raise Exception('Attempted to put string out of bounds.')
        
        if x < 0 or x >= len(self.term_buffer[y]):
            raise Exception('Attempted to put string out of bounds.')

        for i in range(len(text)):
            if (x + i) >= len(self.term_buffer[y]):
                y += 1
            self.putchar_xy(text[i], (x + i) % len(self.term_buffer[0]), y, colour, bold)
    
    def compile_buffer(self):
        # use ansi escape codes to print buffer
        # https://en.wikipedia.org/wiki/ANSI_escape_code

        string = ''
        for i in range(len(self.term_buffer)):
            for j in range(len(self.term_buffer[i])):
                if not self.term_buffer[i][j] is None:
                    string += '\x1b[%d;%dH' % (i, j) + self.term_buffer[i][j]['colour'] + self.term_buffer[i][j]['content'] + term.normal if not self.term_buffer[i][j]['bold'] else term.bold('\x1b[%d;%dH' % (i, j) + self.term_buffer[i][j]['colour'] + self.term_buffer[i][j]['content'] + term.normal)
        
        return string
    
    def print_flush(self):
        print(term.home + term.clear + self.compile_buffer())
        self.clear_buffer()

class ConsoleGame:
    def __init__(self, name="Untitled"):
        self.buffer = Buffer()
        self.name = name
        self.updatenum = -1
        self.framenum = -1
        self.ingame = False
        self.savelocation = None
        self.starttime = 0
        self.lastupdatetime = 0

    def printXY(self, text, x, y):
        stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
        stdout.flush()

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
        cursor.show()
        self.event_quit()

    def mainloop(self):
        cursor.hide()
        self.ingame = True
        self._title(self.name)
        self.starttime = self.current_ms_time()
        self.lastupdatetime = self.starttime
        self.load()
        while self.ingame:
            self.updatenum += 1
            self.update(self.gettime() - self.lastupdatetime)
            self.lastupdatetime = self.gettime()
            self.framenum += 1
            self.draw()
            self.buffer.print_flush()