# This file was created by: Sulaymaan Khan

# IMPORT ALL NECESSARY MODULES AND LIBRARIES
import pygame as pg
from game.SulaymaanK_mygame.settings import *
from game.SulaymaanK_mygame.sprites import *

# created a game class to instantiate later
# it will have all the necessary parts to run the game
class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen= pg.display.set_mode((WIDTH, HEIGHT))
        #name
        pg.display.set_caption("Sulaymaans' Game")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 50, 50)
        # instantiated a mob
        self.mob = Mob(self, 100,100)
        for i in range (60):
            Mob(self, i*randint(0,200))
        self.wall = Wall(200, 200)
        self.wall1 = Wall (400, 200)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.mob)
        self.all_sprites.add(self.wall)
        self.all_sprites.add(self.wall1)
        for i in range(6):
            print (i*TILESIZE)
            w = Wall(i*TILESIZE, 32)
            self.all_sprites.add(w)
        

    
    
    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000 
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        # pg.quit()
        # process
    def update(self):
        self.all_sprites.update()
        # output
        print(self.player.rect.colliderect(self.mob))
        pass
    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    
if __name__ == "__main__":
    g = Game()
    g.new()
    g.run()
