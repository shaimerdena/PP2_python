import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
done = True

surface = pygame.Surface((100,100))
surface.fill((255,0,0))
image = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab7\tutorial\551253201520.jpg')

while done:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.blit(image,(0, 0))   #displaying the image
        
    pygame.display.flip()
pygame.quit()