# This file was created by: Sulaymaan Khan

# IMPORT ALL NECESSARY MODULES AND LIBRARIES
import pygame as pg
from settings import *
from sprites import *
from tilemap import *
from os import path

'''
Elavator pitch: I want to make a game that is a sidescroller boss-rush type game where your goal is to beat
all the bosses as fast as possible with nothing but a gun and a dash ability

GOALS: Beat all bosses within certain time limit
RULES: You can only take 3 hits, you can charge your gunshot to increase damage, you can equip 3 different guns (Shotgun, minigun, and revolver the starting weapon)
FEEDBACK: Charge meter for gun, 3 hearts (can only take 3 hits)
FREEDOM: You have x and y, charge gun, shoot, and dash

ALPHA GOAL: Add x and y movement, gun, chargeshot, dash, and tutorial boss
'''
# created a game class to instantiate later
# it will have all the necessary parts to run the game
# each class stands for 1 block
# the game class is created to organize the elements needed to create a game
class Game:
    # __init__ stands for initialize/ starts all components in code
    def __init__(self):
        pg.init()
        # pg.mixer is used for sound
        pg.mixer.init()
        self.screen= pg.display.set_mode((WIDTH, HEIGHT))
        #name
        pg.display.set_caption("Sulaymaans' Game")
        self.clock = pg.time.Clock()
        self.running = True
        # create playerbock, creates the all_sprites groupso that we can batch update and render, defines properties that can be seen in the game system
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map = Map(path.join(self.game_folder, 'level1.txt'))
    def new(self):
        self.load_data()
        print(self.map.data)
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_powerups = pg.sprite.Group()
        self.all_coins = pg.sprite.Group()
        # self.player = Player(self, 1, 1)
        # instantiated a mob
        # self.mob = Mob(self, 100,100)
        # makes new mobs and walls using a for loop
        # for i in range(randint(10,20)):
        #     m = Mob(self, i*randint(0, 200), i*randint(0, 200))
        #     Wall(self, i*TILESIZE, i*TILESIZE)


        #takes map.data and parses it using enumerate so that we can assign x and y values to
        #object instance
        for row, tiles in enumerate(self.map.data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile =="1":
                    Wall(self, col, row)
                if tile =="P":
                    self.player = Player(self, col, row)
                if tile =='M':
                    Mob(self, col, row)
                if tile == 'U':
                    Powerup(self, col, row)
                if tile =='C':
                    Coin(self, col, row)
    # using self.running as a boolean to continue running the game   
    def run(self):
        while self.running:
            # controlled by clock in line 22
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
    
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surface.blit(text_surface, text_rect)
    def draw(self):
        self.screen.fill(WHITE)
        self.draw_text(self.screen, str(pg.time.get_ticks()), 24, WHITE, WIDTH/30, HEIGHT/30)
        self.draw_text: (self.screen, "Coins collected: " + str(self.player.coins), 24, BLACK, WIDTH/2, HEIGHT/24)
        pg.display.flip()

# checks file name and creates a gae object
if __name__ == "__main__":
    g = Game()
    # create all game elements with the new method (not function)
    g.new()
    g.run()
