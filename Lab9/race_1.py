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

# Coins sprite class
class Coins(pygame.sprite.Sprite):
    def __init__(self, name, score, image):
        super().__init__()
        self.name = name
        self.score = score
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        # Ensure coin doesn't spawn over an enemy
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            if not pygame.sprite.spritecollideany(self, enemies): 
                break

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

class Clever(Coins):
    def __init__(self):
        super().__init__('Clever', 5, r"C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab9\clever.png")

class NormalCoin(Coins):
    def __init__(self):
        super().__init__("Coin", 2, r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\race_files\coin.png')

P = PLayer()
Cl = Clever()
Co = NormalCoin()

# Group all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)
all_sprites.add(Cl)
all_sprites.add(Co)

coin_group = pygame.sprite.Group()
coin_group.add(Cl)
coin_group.add(Co)

count = 0

done = False
while not done:
    screen.fill((WHITE))
    screen.blit(bg, (0, 0))

    score = font_small.render(str(scores), True, BLACK)
    screen.blit(score, (SCREEN_WIDTH - 40, 10))

    if (scores - count) > 30:
        count = scores
        SPEED += 2    # Increase speed every 30 points

    for event in pygame.event.get():
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

    # Check collision with coins
    collected_coins = pygame.sprite.spritecollide(P, coin_group, True)
    for coin in collected_coins:
        if isinstance(coin, Clever):
            scores += 5  # Clever дает больше очков
        else:
            scores += 2  # Обычная монета

        # Создать новую монету
        if random.random() < 0.3:  # 30% шанс на Clever
            new_coin = Clever()
        else:
            new_coin = NormalCoin()

        coin_group.add(new_coin)
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