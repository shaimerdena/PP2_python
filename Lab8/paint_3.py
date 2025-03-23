import pygame, sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    caption = pygame.display.set_caption(('Painter'))
    clock = pygame.time.Clock()

    radius = 15
    x, y = 0, 0
    points = []

    # Predefined some colors
    ORANGE = (100,65,0)
    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255,255,0)
    PURPLE = (160,32,240)
    PINK = (255, 192, 203)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #surfase
    canvas = pygame.Surface((800, 600))
    canvas.fill(WHITE)
    mode = BLUE

    #color palette
    list_of_colors = [BLACK, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
    color_rects = [(30 + i * 30, 20, 20, 20) for i in range(len(list_of_colors))]

    #eraser
    eraser = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\paint_files\eraser.png')
    eraser_rect = eraser.get_rect(center = (265,19))

    #starting position for rectangle and circle
    start_pos = (0,0)
    rect_position = pygame.Rect((0,0,0,0))

    drawing = False

    done = False

    drawing_rect = False

    while not done:
        screen.blit(canvas, (0,0))

        pygame.draw.rect(screen, WHITE, pygame.Rect(0,0,800,60))
        pygame.draw.line(screen, BLACK, (0, 60), (800, 60), 1)
        colors(screen, list_of_colors)
        screen.blit(eraser, (265,19))

        rect_rect = pygame.Rect(305, 23, 17, 17)
        pygame.draw.rect(screen, BLACK, rect_rect, 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                color_selected = False  # Track if a color was selected
                start_pos = event.pos

                # Check if a color button was clicked
                for i, rect in enumerate(color_rects):
                    if pygame.Rect(rect).collidepoint(x, y):
                        mode = list_of_colors[i]  # Change the drawing color
                        color_selected = True  # Prevent drawing from activating
                        break

                # Check if the eraser was clicked
                if eraser_rect.collidepoint(x, y):
                    mode = WHITE
                    color_selected = True  # Prevent accidental drawing

                if rect_rect.collidepoint(x, y):
                    drawing_rect = True

                # Start drawing only if the user didn't click a color or the eraser
                if not color_selected:
                    drawing = True
                    last_pos = event.pos

            # Рисуем линию, если зажата кнопка и двигается мышка
            if event.type == pygame.MOUSEMOTION and drawing:
                if drawing and last_pos:
                    pygame.draw.line(canvas, mode, last_pos, event.pos, radius)
                last_pos = event.pos
                if drawing_rect:
                    end_pos = event.pos
                    rect_position.x = min(start_pos[0], end_pos[0])
                    rect_position.y = min(start_pos[1], end_pos[1])
                    rect_position.width = abs(start_pos[0] - end_pos[0])
                    rect_position.height = abs(start_pos[1] - end_pos[1])


            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_rect:
                    pygame.draw.rect(canvas, BLACK, rect_position, 2)  # Draw rectangle on canvas
                    drawing_rect = False
                drawing = False
        
        clock.tick(100)
        pygame.display.flip()

def colors(screen, list_of_colors):
    pos = 30
    for i in range(len(list_of_colors)):
        pygame.draw.circle(screen, list_of_colors[i], (pos, 30), 10)
        pos += 30

main()