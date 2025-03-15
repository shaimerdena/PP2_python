import pygame

pygame.init()
screen = pygame.display.set_mode((500,200))
pygame.display.set_caption('Music Player')
done = False
list_of_songs = [r'Lab7\player_files\Daddy Issues.mp3', r'Lab7\player_files\The Last Day.mp3', r'Lab7\player_files\Leave the lights on.mp3', r'Lab7\player_files\Я знаю какая ты.mp3', r'Lab7\player_files\Money pull up.mp3']

#buttons
play = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\player_files\play-button.png')
play_rect = play.get_rect(topleft = (225, 125))
current_image = play
pause = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\player_files\pause.png')
pause_rect = play_rect
next = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\player_files\next.png')
next_rect = next.get_rect(topleft = (325, 125))
back = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\player_files\back.png')
back_rect = back.get_rect(topleft = (125, 125))

#playing
current_song = 0
pygame.mixer.music.load(list_of_songs[0])
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()

#text
font = pygame.font.SysFont('Montserrat', 48)
current_text = list_of_songs[current_song][18:-4]
text = font.render(current_text, True, (0,0,0))

playing = False

while not done:
    screen.fill((204,255,153))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):    #pausing and resuming the song
                if current_image == play:
                    current_image = pause
                    pygame.mixer.music.unpause()
                    playing = True
                else:
                    current_image = play
                    pygame.mixer.music.pause()
                    playin = False
            elif next_rect.collidepoint(event.pos):    #next song
                current_song = (current_song + 1) % len(list_of_songs)
                current_text = list_of_songs[current_song][18:-4]
                text = font.render(current_text, True, (0,0,0))
                pygame.mixer.music.load(list_of_songs[current_song])
                pygame.mixer.music.play()
                current_image = pause
                playing = True
            elif back_rect.collidepoint(event.pos):    #previous song
                current_song = (current_song - 1) % len(list_of_songs)
                current_text = list_of_songs[current_song][18:-4]
                text = font.render(current_text, True, (0,0,0))
                pygame.mixer.music.load(list_of_songs[current_song])
                pygame.mixer.music.play()
                current_image = pause
                playing = True

    #buttons
    screen.blit(current_image, play_rect.topleft)
    screen.blit(next, next_rect.topleft)
    screen.blit(back, back_rect.topleft)

    pygame.draw.rect(screen, (0,153,0), pygame.Rect(0, 0, 800, 100))

    #text
    screen.blit(text, (125, 30))

    pygame.display.flip()
pygame.quit()