import pygame

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption('Red Circle')
done = False
x = 350
y = 350
time = pygame.time.Clock()

while not done:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y-20>0: y-=20
    if pressed[pygame.K_DOWN] and y+20<700: y+=20
    if pressed[pygame.K_LEFT] and x-20>0: x-=20
    if pressed[pygame.K_RIGHT] and x+20<700: x+=20

    pygame.draw.circle(screen, (255,0,0), (x,y), 25)
    
    time.tick(60)        
    pygame.display.flip()

pygame.quit()
    