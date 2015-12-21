import numpy as np
from random import choice, random

class Ising():

    def __init__(self, N, beta):
        self.N = N
        self.beta = beta

        self.create_lattice()

    def create_lattice(self):
        lattice = np.zeros((self.N,self.N))

        _values = [1, -1]

        for i in range(self.N):
            for j in range(self.N):
                lattice[i,j] = choice(_values)

        self.lattice = lattice


    def get_lattice(self):
        return self.lattice

    def get_pixel_value(self,x,y):
        return self.lattice[x,y]

    def set_pixel_value(self, x, y, val):
        self.lattice[x,y] = val

    def get_neighbours(self, x, y):
        directions = [(0,-1), (0,1), (-1,0), (1,0)]

        neighbours = []
        new_x = 0
        new_y = 0
        for dir in directions:
            new_x = x + dir[0]
            new_y = y + dir[1]

            neighbours.append(self.get_pixel_value(new_x,new_y))

        return neighbours






