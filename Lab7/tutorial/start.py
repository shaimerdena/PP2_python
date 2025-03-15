import pygame

pygame.init()    # initializes all the modules required for PyGame
screen = pygame.display.set_mode((600, 500))  # will launch a window of the desired size:  set_mode(width, height)
done = False
is_blue = True
x = 250
y = 200


while not done:
    screen.fill((0,0,0))        #Clear the screen each frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #when you click on the close button in the corner of the window.
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y=-10
        if pressed[pygame.K_DOWN]: y+=10
        if pressed[pygame.K_LEFT]: x-=10
        if pressed[pygame.K_RIGHT]: x+=10

        if is_blue: color = (0, 128, 255)
        else: color = (255, 0, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 100, 100))     #Rect(coordinates, dimensions)

        pygame.display.flip()            #this call is required in order for any updates that you make to the game screen to become visible.
pygame.quit()