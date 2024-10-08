# this file was created by Sulaymaan Khan

import pygame as pg
from pygame.sprite import Sprite
from settings import *
import random

class Player(Sprite):
    def __init__(self, game, x, y):
        self.group = game.all_sprites
        Sprite.__init__(self, self.group)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        # self.rect.x = x
        # self.rect.y = y
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0
    def get_keys(self):
        keys = pg.keys.get_pressed()
        if keys[pg.K_w]:
            self.vy -=self.speed
        if keys[pg.K_a]:
            self.vy -=self.speed
        if keys[pg.K_s]:
            self.vy +=self.speed
        if keys[pg.K_d]:
            self.vy +=self.speed
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits [0].rec.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits [0].rec.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y +=  self.vy * self.game.dt


class Mob(Sprite):
    def __init__(self, x, y):
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game = game.all_sprites
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        self.rect.x = x
        self.rect.y = y
        self.category = random.choice([0,1])
    def update(self):

        # moving towards the side of the screen
        self.rect.x += self.speed
        # when it hits the side of the screen, it will move down
        if self.rect.x > WIDTH or self.rect.left < 0:
            #print("off the screen")
            print(self.speed)
            print(self.rect.x)
            self.speed *= -1
            self.rect.y += 32
        
        # then it will move towards the other sode of the screen
        # if it gets to the bottom, then it move t the top of the screen
        # (display logic in the terminal)

class Wall(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self.game = game
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class PowerUP: 