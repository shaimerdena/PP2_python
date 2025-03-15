import pygame

pygame.init()
screen = pygame.display.set_mode((800,300))
done = False

pygame.mixer.music.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\player_files\Moby-The Last Day (with Skylar Grey).mp3')
pygame.mixer.music.play(0)  
pygame.mixer.music.queue(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\player_files\topoffmusic).mp3')

while not done:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]: pygame.mixer.music.stop()

    pygame.display.flip() 
pygame.quit()