from Ising import Ising 
from random import choice, random, randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math



def get_ratio(current_pixel, new_pixel_value):
    neighbours = image.get_neighbours(current_pixel[0], current_pixel[1])

    curr_pixel_value = image.get_pixel_value(current_pixel[0], current_pixel[1])

    t = 0
    for neighbour_value in neighbours:
        t = t + new_pixel_value*neighbour_value - curr_pixel_value*neighbour_value 

    return math.pow(math.e, beta*t)

#implements metropolis
def metropolis(current_pixel, Q):
    #proposed j
    new_pixel_value = choice(Q)
    new_image = image

    ratio = get_ratio(current_pixel, new_pixel_value)

    a = min(1, ratio)

    prob = random()
    if(prob < a):   #accept
        new_image.set_pixel_value(current_pixel[0], current_pixel[1], new_pixel_value)

        #update MC
        chain.append(new_pixel_value)
    else:
        #update MC
        chain.append(image.get_pixel_value(current_pixel[0],current_pixel[1]))


    return new_image


def func(self):
    for x in range(N-1):
        for y in range(N-1):
            #X0
            current_pixel = (x,y)
            new_im = metropolis(current_pixel, Q)
    im = plt.imshow(new_im.get_lattice(), cmap='Greys', animated=True)
    return im
##################################################

#the MC consists of pixel values ??
chain = []
Q = [-1, 1]

fig = plt.figure()

N = 50
beta = 10

image = Ising(N, beta)


ani = animation.FuncAnimation(fig, func, frames = 100, interval = 50)
plt.show()


