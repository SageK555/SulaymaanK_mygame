import pygame as og
from settings import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
            # for loop 
                self.data.apped(line.strip()) # <- anything not a number, we get rid of it (line.strip)
                #taking the empety list and putting stuff init - wha append does
        self.tilewidth = len(self.data[0])
        # the length of the entiire level is equal the length of level 0
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
