import pygame, sys

# Main function to run the painter program
def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))  # Set screen size
    caption = pygame.display.set_caption(('Painter'))  # Set window title
    clock = pygame.time.Clock()

    radius = 15  # Brush size
    x, y = 0, 0  # Mouse position variables
    points = []

    # Predefined colors
    ORANGE = (100,65,0)
    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255,255,0)
    PURPLE = (160,32,240)
    PINK = (255, 192, 203)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Create a drawing surface
    canvas = pygame.Surface((800, 600))
    canvas.fill(WHITE)  # Set canvas background color
    mode = BLUE  # Default drawing color

    # Define color palette
    list_of_colors = [BLACK, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
    color_rects = [(30 + i * 30, 20, 20, 20) for i in range(len(list_of_colors))]

    # Load eraser image
    eraser = pygame.image.load(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab8\paint_files\eraser.png')
    eraser_rect = eraser.get_rect(center = (265,19))

    # Variables for drawing shapes
    start_pos = (0,0)
    rect_position = pygame.Rect((0,0,0,0))
    circle_center = (0,0)
    circle_radius = 0

    drawing = False  # Flag for freehand drawing
    drawing_rect = False  # Flag for rectangle drawing
    drawing_circle = False  # Flag for circle drawing

    while True:
        screen.blit(canvas, (0,0))  # Draw canvas onto the screen

        # Draw UI elements
        pygame.draw.rect(screen, WHITE, pygame.Rect(0,0,800,60))  # White background for the toolbar
        pygame.draw.line(screen, BLACK, (0, 60), (800, 60), 1)  # Separator line
        colors(screen, list_of_colors)  # Draw color selection circles
        screen.blit(eraser, (265,19))  # Display eraser icon

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_c:  # Press 'C' to start drawing a circle
                    drawing_circle = True
                elif event.key == pygame.K_r:  # Press 'R' to start drawing a rectangle
                    drawing_rect = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                color_selected = False  # Track if a color was selected
                start_pos = event.pos

                # Check if a color button was clicked
                for i, rect in enumerate(color_rects):
                    if pygame.Rect(rect).collidepoint(x, y):
                        mode = list_of_colors[i]  # Change drawing color
                        color_selected = True  # Prevent accidental drawing
                        break

                # Check if the eraser was clicked
                if eraser_rect.collidepoint(x, y):
                    mode = WHITE  # Set eraser mode
                    color_selected = True  # Prevent accidental drawing

                # Start drawing only if a color or the eraser was not selected
                if not color_selected:
                    if drawing_circle:
                        circle_center = event.pos
                    elif drawing_rect:
                        rect_position.topleft = event.pos
                    else:
                        drawing = True
                        last_pos = event.pos

            if event.type == pygame.MOUSEMOTION:
                if drawing and last_pos:
                    pygame.draw.line(canvas, mode, last_pos, event.pos, radius)  # Draw lines
                    last_pos = event.pos
                if drawing_rect:
                    end_pos = event.pos
                    rect_position.width = abs(start_pos[0] - end_pos[0])
                    rect_position.height = abs(start_pos[1] - end_pos[1])
                if drawing_circle:
                    end_pos = event.pos
                    circle_radius = int(((end_pos[0] - circle_center[0])**2 + (end_pos[1] - circle_center[1])**2)**0.5)  # Calculate circle radius

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_rect:
                    pygame.draw.rect(canvas, BLACK, rect_position, 2)  # Draw rectangle
                    drawing_rect = False
                if drawing_circle:
                    pygame.draw.circle(canvas, BLACK, circle_center, circle_radius, 2)  # Draw circle
                    drawing_circle = False
                drawing = False  # Stop freehand drawing
        
        clock.tick(100)
        pygame.display.flip()

# Function to display the color selection palette
def colors(screen, list_of_colors):
    pos = 30
    for i in range(len(list_of_colors)):
        pygame.draw.circle(screen, list_of_colors[i], (pos, 30), 10)
        pos += 30

main()