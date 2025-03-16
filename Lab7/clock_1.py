import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Micky Mouse Clock')
done = False

image = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\clock_files\clock.png')
min_right = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\clock_files\min_hand.png')
sec_left = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\clock_files\sec_hand.png')

def rotating(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center = pivot)
    return rotated_image, rotated_rect
    

while not done:
    screen.fill((0,0,0))

    screen.blit(image, (0,0))

    current_time = time.localtime()
    minute = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = (6 * minute) + 60   
    seconds_angle = (6 * seconds) - 60   

    rotated_minute_hand, minute_rect = rotating(min_right, minute_angle, (400,300))
    rotated_second_hand, second_rect = rotating(sec_left, seconds_angle, (400,300))

    screen.blit(rotated_minute_hand, minute_rect.topleft)
    screen.blit(rotated_second_hand, second_rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
pygame.quit()