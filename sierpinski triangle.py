import pygame, sys, random
from pygame.locals import *
pygame.init()
 
WHITE = (255, 255, 255)
BLACK = (0,0,0)
 
surface = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Chaos Game')

def mark_pixel(surface, pos):
    surface.set_at(pos, (BLACK))

triangle = [[500, 780], [258, 360], [742, 360]]

# The main function that controls the game
def main():
    first = True

    surface.fill(WHITE)

    # mark first three points
    if first == True:
        for i in range(3):
            mark_pixel(surface, (triangle[i][0], triangle[i][1]))
        first = False

    previous_position = (triangle[2][0], triangle[2][1])

    for i in range(100000):
        vertex = random.randint(0,2)

        new_position = int((previous_position[0]+triangle[vertex][0])/2), int((previous_position[1]+triangle[vertex][1])/2)

        mark_pixel(surface, new_position)
            
        previous_position = new_position
 
    # Render elements of the game
    pygame.display.update()

main()
