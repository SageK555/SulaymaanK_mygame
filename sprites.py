# this file was created by Sulaymaan Khan

import pygame as pg
from pygame.sprite import Sprite
from settings import *
import random
# Velocity
vec = pg.math.Vector2

#Anything under class ----- then that code is going to be used
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
        #acc means acceleration
        self.acc = vec(0,0)
        self.x = self.pos.x
        self.y = self.pos.y
        self.speed = 10
        #self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0
        #self.coins = 0
        self.dir = ''
# movement
#Function is defined by def
    def get_keys(self):
        #if key gets pressed movement will begin
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vy -=self.speed
        if keys[pg.K_a]:
            self.vx -=self.speed
        if keys[pg.K_s]:
            self.vy +=self.speed
        if keys[pg.K_d]:
            self.vx +=self.speed
        #if keys[pg.K_SPACE]:
            #self.jump()
            #print("trying to jump")
        # dir means direction
        if keys[pg.K_LSHIFT]:
            self.get_dir()
            self.dash()
#Dash attempt 2 with help
    #def get_dir(self):
            #if abs(self.vx) > abs(self.vy):
                #print("x is more")
                #if self.vx > 0:
                    #return (1,0)
                #elif self.vx < 0:
                    #return (-1,0)
            #if abs(self.vy)
    
    # Dash attempt 1
            #if keys[pg.K_w]:
                #self.vy -= 2
            #if keys[pg.K_a]:
                #self.vx -= 2
            #if keys[pg.K_s]:
                #self.vy += 2
            #if keys[pg.K_d]:
                #self.vx += 2
            print("ima big steppa")
# Shooting aim
        #if keys[pg.K_u]:
            #self.vy
        #if keys[pg.K_h]:
            #self.vy
        #if keys[pg.K_j]:
            #self.vy
        #if keys[pg.K_k]:
            #self.vy
# Collide with walls
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - TILESIZE
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - TILESIZE
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    #def collide_with_stuff(self, group, kill):
        #hits = pg.sprite.spritecollide(self, group, kill)
        #if hits:
            #if str(hits[0].__class__.__name__) == "Powerup":
                #print("I hit a powerup")
                #self.speed =+ 5
                #if str(hits[0].__class__.__name__) == "Coin":
                    #print("i hit a coin...")
                    #self.coins += 1
    def dash(self):
        self.vy
        self.vx
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y +=  self.vy * self.game.dt
    
    # reverse order to fix collision issues

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
        self.speed = 10
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
        #elif self.rect.colliderect(self.game.player):
            #self.speed *= -1
        #elif self.rect.colliderect(self):
            #self.speed *= -1
        
        # then it will move towards the other sode of the screen
        # if it gets to the bottom, then it move t the top of the screen
        # (display logic in the terminal)

class Wall(Sprite):
    #initialized to game, x and y movement if needed, and self
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

#class Powerup: 
    #def __init__(self, game, x, y):
        #self.game = game
        #self.groups = game.all_sprites, game.all_powerups
        #Sprite.__init__(self, self.groups)
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        #self.rect = self.image.get_rect()
        #self.image.fill(PINK)
        #self.rect.x = x * TILESIZE
        #self.rect.y = y * TILESIZE

#class Coin(Sprite):
    #def __init__(self, game, x, y):
        #self.game = game
        #self.groups = game.all_sprites, game.all_coins
        #Sprite.__init__(self, self.groups)
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        #self.rect = self.image.get_rect()
        #self.image.fill(YELLOW)
        #self.rect.x = x * TILESIZE
        #self.rect.y = y * TILESIZE

class LifeBAR(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_lifebar
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        

class Boss(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_boss
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((BIGTILESIZE, BIGTILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLACK)
        self.rect.x = x * BIGTILESIZE
        self.rect.y = y * BIGTILESIZE
        