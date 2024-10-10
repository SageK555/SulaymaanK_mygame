# this file was created by Sulaymaan Khan

import pygame as pg
from pygame.sprite import Sprite
from settings import *
import random

vec = pg.math.Vector2

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
        self.pos = vec(x, y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.x = self.pos.x
        self.y = self.pos.y
        self.speed = 10
        #self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0
        self.coins = 0
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
        if keys[pg.K_SPACE]:
            self.jump()
            print("trying to jump")
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits [0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits [0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    def collide_with_stuff(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Powerup":
                print("I hit a powerup")
                self.speed =+ 5
                if str(hits[0].__class__.__name__) == "Coin":
                    print("i hit a coin...")
                    self.coins += 1
    def jump(self):
        self.vy
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y +=  self.vy * self.game.dt
    # reverse order to fix collision issues


        self.collide_with_stuff(self.game.all_powerups, True)
        self.collide_with_stuff(self.game.all_coins, True)

        self.rect.x = self.x
        self.collide_with_walls('x')
        
        self.rect.y = self.y
        self.collide_with_walls('y')


class Mob(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_walls
        Sprite.__init__(self, self.groups)
        self.game = game.all_sprites
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.category = random.choice([0,1])
    def update(self):

        # moving towards the side of the screen
        self.rect.x += self.speed

        hits =pg.sprite
        # when it hits the side of the screen, it will move down
        if self.rect.right > WIDTH or self.rect.left < 0:
            # print("off the screen...")
            self.speed *= -1
            self.rect.y += 32
        # elif self.rect.colliderect(self.game.player):
        #     self.speed *= -1
        # elif self.rect.colliderect(self):
        #     self.speed *= -1
        
        # then it will move towards the other sode of the screen
        # if it gets to the bottom, then it move t the top of the screen
        # (display logic in the terminal)

class Wall(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_walls
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        pass

class Powerup: 
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_powerups
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(PINK)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Coin(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_coins
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE