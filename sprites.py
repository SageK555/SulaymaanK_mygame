# this file was created by Sulaymaan Khan

import pygame as pg
from pygame.sprite import Sprite
from game.SulaymaanK_mygame.settings import *

class Player(Sprite):
    def __init__(self, game, x, y):
        self.group = game.all_sprites
        Sprite.__init_(self, self.group)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.x = x
        self.y = y
# self.speed = 10
    def get_keys(self):
        keys = pg.keys.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -=self.speed
        if keys[pg.K_a]:
            self.rect.x -=self.speed
        if keys[pg.K_s]:
            self.rect.y +=self.speed
        if keys[pg.K_d]:
            self.rect.x +=self.speed
    def update(self):
        self.get_keys()
        # self.rect.x += 1


class Mob(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image=pg.Surface((32,32))
        self.image.fill(GREEN)
        self.x=x
        self.y=y
    def update(self):
        # moving towards the side of the screen
        self.rect.x += self.speed
        # when it hits the side of the screen, it will move down
        if self.rect.x > WIDTH:
            print("off the screen")
            print(self.speed)
            print(self.rect.x)
            self.speed *= -1
            self.rect.y += 32

        # then it will move towards the other sode of the screen
        # if it gets to the bottom, then it move t the top of the screen
        # (display logic in the terminal)

class Wall(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
