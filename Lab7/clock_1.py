import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Micky Mouse Clock')
done = False
image = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\clock_files\clock.png')
min_right = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\clock_files\min_hand.png')
sec_left = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\clock_files\sec_hand.png')

while not done:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(image, (0,0))
    screen.blit(min_right, (0,0))
    screen.blit(sec_left, (0,0))

    pygame.display.flip()
pygame.quit()