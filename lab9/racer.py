#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
# Count the number of coins (not dependent on its weight)
COIN_COUNT = 0
N = 5

#List with coin's pictures
coins_img = ["sources/Coin1.png", "sources/Coin2.png", "sources/Coin3.png"]

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("sources/AnimatedStreet.png")
pygame.mixer.music.load('sources/background.wav')
pygame.mixer.music.play(-1)

print
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        global SPEED
        super().__init__() 
        self.image = pygame.image.load("sources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        self.speed = SPEED
         # flag for increasing speed
        self.speed_increased = False

    def move(self):
        global SCORE
        self.change_speed()
        self.rect.move_ip(0,self.speed)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def change_speed(self):
        global COIN_COUNT, N
        #Every N coins speed will increase
        if COIN_COUNT % N == 0 and COIN_COUNT != 0 and not self.speed_increased:
            self.speed += 0.5
            self.speed_increased = True
            #print(COIN_COUNT, self.speed)
        elif COIN_COUNT % N != 0:
            self.speed_increased = False



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("sources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        global coins, all_sprites
        #every coin has its weight (golden +3 points, silver +2 points, bronze +1 point)
        self.weight = random.randint(1,3)
        self.image = pygame.image.load(coins_img[self.weight-1])
        self.rect = self.image.get_rect()
        #To ensure that coin doesn't have the same coordinates with enemies
        while pygame.sprite.spritecollideany(self, enemies):
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
            #To ensure that coin doesn't have the same coordinates with other coins
        while pygame.sprite.spritecollideany(self, coins):
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    #Check if a collision occurs between Enemy and Coin, if yes delete this coin
    def check_collisions(self):
        global all_sprites
        if pygame.sprite.spritecollideany(self, enemies):
            self.kill()

    #Check if a collision occurs between Player and Coin, if yes update coin_score and delete this coin
    def update(self):
        global COIN_SCORE, COIN_COUNT
        if pygame.sprite.collide_rect(self, P1):
            COIN_SCORE += self.weight
            COIN_COUNT += 1
            self.kill()    
        self.check_collisions()         

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 3000)

#Adding Coin event
ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_COIN,2000)

#Function to generate coins
#It depends on the number of coins so it won't be too many of them on the road
def coin_generator():
    global coins, all_sprites
    if len(coins) < 3:
        for i in range(random.randint(1,3)):
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)
    elif len(coins) == 3:
        coin = Coin()
        coins.add(coin)
        all_sprites.add(coin)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #     SPEED += 0.5
        if event.type == ADD_COIN:
            coin_generator()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_scores = font_small.render(str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_scores, (SCREEN_WIDTH - 35,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('sources/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()      

    coins.update()

    pygame.display.update()
    FramePerSec.tick(FPS)
