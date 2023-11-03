import matplotlib.pyplot as plt
import random

triangle = [[0, 280], [-242, -140], [242, -140]]

def plot_point(x,y):
    plt.scatter(x,y)

for i in range(3):
    plot_point(triangle[i][0], triangle[i][1])

previous_position = (triangle[2][0], triangle[2][1])

for i in range(1000):
    vertex = random.randint(0,2)

    new_position = int((previous_position[0]+triangle[vertex][0])/2), int((previous_position[1]+triangle[vertex][1])/2)

    plot_point(*new_position)
        
    previous_position = new_position

plt.show()
