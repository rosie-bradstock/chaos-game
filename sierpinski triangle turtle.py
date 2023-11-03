import random, turtle

turtle = turtle.Pen()
turtle.speed(0)
turtle.penup()

#vertices of the triangle
triangle = [[100, 380], [-258, -160], [342, -160]]

#puts dots where all the vertices are
for i in range(3):
    turtle.goto((triangle[i][0], triangle[i][1]))
    turtle.dot(5)
    
#sets like srart position as the last vertex
previous_position = (triangle[2][0], triangle[2][1])

#repeats 10000 times
#selects a random vertex from the triangle (0-2)
#finds x and y coordinates halfway between old position and random vertex
#makes the new x y coordinate the new start position 
for i in range(10000):
        vertex = random.randint(0,2)
        new_position = int((previous_position[0]+triangle[vertex][0])/2), int((previous_position[1]+triangle[vertex][1])/2)
        turtle.goto(new_position)
        turtle.dot(5)
        previous_position = new_position
