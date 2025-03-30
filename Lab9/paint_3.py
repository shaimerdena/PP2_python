import pygame, sys
import math

# Main function to run the painter program
def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))  # Set screen size
    caption = pygame.display.set_caption(('Painter'))  # Set window title
    clock = pygame.time.Clock()

    radius = 15  # Brush size
    x, y = 0, 0  # Mouse position variables

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
    triangle_pos1 = (0,0)
    triangle_pos2 = (0,0)
    triangle_top = (0,0)
    rhombus_center = (0,0)

    # Flags for different drawing modes
    drawing = False  # Freehand drawing mode
    drawing_rect = False  # Rectangle drawing mode
    drawing_circle = False  # Circle drawing mode
    drawing_square = False  # Square drawing mode
    drawing_right_tri = False  # Right triangle drawing mode
    drawing_equilateral_tri = False # Equilateral triangle drawing mode
    drawing_rhombus = False  # Rhombus drawing mode

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
                elif event.key == pygame.K_s:  # Press 'S' to start drawing a square
                    drawing_square = True
                elif event.key == pygame.K_t:  # Press 'T' to start drawing a right triangle
                    drawing_right_tri = True
                elif event.key == pygame.K_e:  # Press 'E' to start drawing an equilateral triangle
                    drawing_equilateral_tri = True
                elif event.key == pygame.K_h:  # Press 'E' to start drawing a rhombus
                    drawing_rhombus = True

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
                        circle_center = event.pos    # Circle center point
                    elif drawing_rect:
                        rect_position.topleft = event.pos
                    elif drawing_square:
                        rect_position.topleft = event.pos   # Top-left corner for square
                    elif drawing_right_tri:         
                        triangle_pos1 = event.pos  # First point for right triangle
                    elif drawing_equilateral_tri:
                        triangle_top = event.pos  # Top vertex for equilateral triangle
                    elif drawing_rhombus:
                        rhombus_center = event.pos  # Center point for rhombus
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
                if drawing_square:
                    end_pos = event.pos
                    rect_position.width = abs(start_pos[0] - end_pos[0])
                    rect_position.height = rect_position.width    # Ensure square proportions
                if drawing_right_tri:
                    triangle_pos2 = event.pos    #end point is a 2nd vertex of a triangle
                if drawing_equilateral_tri:
                    end_pos = event.pos
                    height = abs(end_pos[1] - triangle_top[1])
                    length = height//math.sqrt(3)      #computing vertexes' coordinates using height of a triangle
                if drawing_rhombus:
                    end_pos = event.pos   
                    x, y = rhombus_center
                    dx = end_pos[0] - x
                    dy = end_pos[1] - y
                    points = [(x, y - dy), (x + dx, y), (x, y + dy), (x - dx, y)]   #oomputing coordinates of vertexes

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_rect:
                    pygame.draw.rect(canvas, BLACK, rect_position, 2)  # Draw rectangle
                    drawing_rect = False
                if drawing_circle:
                    pygame.draw.circle(canvas, BLACK, circle_center, circle_radius, 2)  # Draw circle
                    drawing_circle = False
                if drawing_square:
                    pygame.draw.rect(canvas, BLACK, rect_position, 2)  # Draw square
                    drawing_square = False
                if drawing_right_tri:
                    x1, y1 = triangle_pos1
                    x2, y2 = triangle_pos2
                    triangle_pos3 = (x1, y2)        # Ensure a right triangle
                    pygame.draw.polygon(canvas, BLACK, [triangle_pos1, triangle_pos2, triangle_pos3], 2)
                    drawing_right_tri = False
                if drawing_equilateral_tri:
                    tri_pos1 = triangle_top[0]+length, end_pos[1]   
                    tri_pos2 = triangle_top[0]-length, end_pos[1]
                    pygame.draw.polygon(canvas, BLACK, [triangle_top, tri_pos1, tri_pos2], 2)
                    drawing_equilateral_tri = False
                if drawing_rhombus:
                    pygame.draw.polygon(canvas, BLACK, points, 2)
                    drawing_rhombus = False
                drawing = False  # Stop freehand drawing
        
        clock.tick(60)
        pygame.display.flip()

# Function to display the color selection palette
def colors(screen, list_of_colors):
    pos = 30
    for i in range(len(list_of_colors)):
        pygame.draw.circle(screen, list_of_colors[i], (pos, 30), 10)
        pos += 30

main()