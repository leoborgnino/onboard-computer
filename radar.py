"""
 Show how to do a radar sweep.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""
# Import a library of functions called 'pygame'
import pygame
import math

# Initialize the game engine
pygame.init()

# Colors
BLACK = (0, 0, 0)
GREEN_BACK = (0,20,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.141592653

# Set the height and width of the screen
size = [450, 450]
screen = pygame.display.set_mode(size)

my_clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

angle     = PI/2
decrement = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set the screen background
    screen.fill(GREEN_BACK)

    # Dimensions of radar sweep
    # Start with the top left at 20,20
    # Width/height of 250
    box_dimensions = [0, 0, 450, 450]
    box_dimensions_over_two = [75, 75, 300, 300]
    box_dimensions_over_three = [150, 150, 150, 150]

    # Draw the outline of a circle to 'sweep' the line around
    pygame.draw.ellipse(screen, GREEN, box_dimensions, 1)
    pygame.draw.ellipse(screen, GREEN, box_dimensions_over_two, 1)
    pygame.draw.ellipse(screen, GREEN, box_dimensions_over_three, 1)

    # Draw a black box around the circle
    # pygame.draw.rect(screen, BLACK, box_dimensions, 2)
    pygame.draw.line(screen, GREEN, [225, 0], [225, 450], 1)
    pygame.draw.line(screen, GREEN, [0, 225], [450, 225], 1)


    # Calculate the x,y for the end point of our 'sweep' based on
    # the current angle
    x = 225 * math.sin(angle) + 225
    y = 225 * math.cos(angle) + 225

    # Draw the line from the center at 145, 145 to the calculated
    # end spot
    pygame.draw.line(screen, RED, [225, 225], [x, y], 2)

    # Increase the angle by 0.03 radians
    if angle > 3*PI/2:
        decrement = 1
    elif angle < PI/2:
        decrement = 0

    angle = angle + ((-1) ** decrement) * .03

    # Flip the display, wait out the clock tick
    pygame.display.flip()
    my_clock.tick(60)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
