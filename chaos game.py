# import relevent modules
import pygame, random, math, os
from pygame.locals import *

# define relevent constants
WHITE = (255, 255, 255)
BLACK = (0,0,0)
WIDTH = 1000

# initialise pygame
pygame.init()
surface = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption('Chaos Game')

# picks a colour for a pixel depending on its position
# aim to be a gradient of three colours with these colours strongest around the outside of a fractal

def get_colour(pos):
    colour1 = int(255 - ((pos[1]) / 4)) + 50
    if colour1 > 255:
        colour1 = 255
    colour1 = int(colour1 * 0.8)
    colour2 = int(math.sqrt(pos[0]**2+pos[1]**2) / 4)
    if colour2 > 255:
        colour2 = 255
    colour2 = int(colour2 * 0.8)
    colour3 = int(math.sqrt((1000-pos[0])**2+pos[1]**2) / 4)
    if colour3 > 255:
        colour3 = 255
    colour3 = int(colour3 * 0.8)

    return colour1, colour2, colour3

# calculates the "kiss" - the point on the line between the previous and new verticies (eg. 0.5 = halfway between these points)

def get_kiss(vertices):

# this formula did not work - credit to Tom Bates (Bridges 2019 Conference Proceedings)

##    alpha = math.pi/vertices
##    beta = 2*alpha*(math.ceil(vertices/4))
##    epsilon = beta-math.pi/2
##
##    kiss = round(1 - (math.sin(alpha) / ((math.sin(alpha) + math.cos(epsilon)))),4)

# needed to be divided by a different number for a triangle in order to work, else is 1/phi for pentagon? Adapted this to work for any shape

    if vertices == 3:
        magic = 1
    else:
        magic = 2
        
    kiss = round(1/(2 * abs(math.cos(2*math.pi/vertices)) + magic),4)

    return kiss

# generates an array containing the coords of the vertices of the shape, scaled and translated to fit the screen

def generate_shape(vertices):

    # fill the screen in a solid colour
    surface.fill(WHITE)

    # define relevent constants
    shape = []
    radius = WIDTH/2
    angle = (2 * math.pi)/vertices

    # calculates the coords using an imaginary circle, and points evenly spaced around its circumference
    for i in range(vertices):
        x_coord = radius*math.sin(angle*i)
        y_coord = radius*math.cos(angle*i)

        x_coord = round((x_coord + radius)*(vertices*0.3))
        y_coord = round((y_coord + radius)*(vertices*0.3))
            
        shape.append((x_coord, y_coord))

    return shape

# the subroutine to put the points within the fractal

def fractal(iterations, vertices, process, colour, restricted):
    
    # generates the vertices of the shape
    shape = generate_shape(vertices)
    previous_position = shape[0]

    # finds the kiss value
    kiss = get_kiss(vertices)

    # decides whether the shape needs to be scaled further to fit the screen
    if restricted or vertices == 4:
        kiss = 0.5
        for i in range(len(shape)):
            shape[i] = (shape[i][0] * (vertices*0.13) , shape[i][1] * (vertices*0.13))

    # sets up some variables
    previous_vertex = 0
    vertex = 0
    
    for i in range(iterations):

        # does not allow a previous point to be picked again as a new vertex (creates a new fractal for a pentagon, may not work for others)         
        if restricted:
            while vertex == previous_vertex:
                vertex = random.randint(0,vertices-1)
            previous_vertex = vertex
        else:
            vertex = random.randint(0,vertices-1)

        # finds the new point as a factor of the distance between the new and old vertex
        new_position = int((previous_position[0]+shape[vertex][0])*kiss), int((previous_position[1]+shape[vertex][1])*kiss)

        # colours the pixel if it needs to be coloured
        if colour:
            surface.set_at(new_position, get_colour(new_position))
        else:
            surface.set_at(new_position, BLACK)
        previous_position = new_position

        # dictates whether you can watch the fractal being created
        if process:
            pygame.display.update()
    
    if process == False:
        pygame.display.update()

save_path = 'E:\Computing\Other Projects\Fractal Images'

# puts everything together to generate the fractal
def generate_random_fractal():
    vertices = random.choice((3,4,5,6,7,8,9))
    restricted = random.choice((True, False))
    coloured = random.choice((True, False))
    fractal_name = f"{vertices} sided fractal, {coloured} coloured, {restricted} restricted.png"
    print(fractal_name)
    file_name = os.path.join(save_path, fractal_name)
    fractal(10**6, vertices, False, coloured, restricted)
    pygame.image.save(surface,file_name)


generate_random_fractal()


        
