import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
scores = 0

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Racer')
clock = pygame.time.Clock()

# Load background image and music
bg = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\race_files\AnimatedStreet.png')
bg_music = pygame.mixer.music.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\race_files\background.wav')
pygame.mixer.music.play(-1)

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts for text rendering
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game Over', True, BLACK)

# Enemy sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\race_files\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global scores
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            scores += 1  # Increase score when enemy leaves the screen
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

E = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E)

# Player sprite class
class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\race_files\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]: self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed[pygame.K_RIGHT]: self.rect.move_ip(5, 0)

# Coin sprite class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\race_files\coin.png')
        self.rect = self.image.get_rect()
        
        # Ensure coin doesn't spawn over an enemy
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            if not pygame.sprite.spritecollideany(self, enemies): 
                break

    def move(self):
        self.rect.move_ip(0, SPEED / 2)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

P = PLayer()
C = Coin()

coins = pygame.sprite.Group()
coins.add(C)

# Group all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)
all_sprites.add(C)

# Event to increase speed over time
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 2000)

done = False
while not done:
    screen.fill((WHITE))
    screen.blit(bg, (0, 0))

    score = font_small.render(str(scores), True, BLACK)
    screen.blit(score, (SCREEN_WIDTH - 40, 10))

    for event in pygame.event.get():
        if event.type == inc_speed:
            SPEED += 0.5  # Increase speed every 2 seconds
        if event.type == QUIT:
            done = True
            pygame.quit()
            sys.exit()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Check collision with enemy
    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\race_files\crash.wav').play()

        screen.fill(RED)
        total_score = font_small.render(f'Total score: {scores}', True, BLACK)
        screen.blit(total_score, (120, 200))
        screen.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    # Check collision with coin
    if pygame.sprite.spritecollide(P, coins, True):
        scores += 5  # Increase score for collecting coins
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Check if player goes off-screen
    if P.rect.left < 0 or P.rect.right > SCREEN_WIDTH:
        pygame.mixer.music.stop()

        screen.fill(RED)
        total_score = font_small.render(f'Total score: {scores}', True, BLACK)
        screen.blit(total_score, (120, 200))
        screen.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    clock.tick(60)
    pygame.display.update()
pygame.quit()