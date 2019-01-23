import matplotlib.pyplot as plt, scipy.ndimage as ndi
import sys, utility, time, numpy as np


def gravitational_field(strength, state):
    g0 = [[1,1,1],[1,1,1],[1,1,1]]

    fields = {1: g0}
    world = ndi.convolve(np.array(state), g0)
    plt.imshow(world, 'gray')
    plt.show()


def initialize(N_Particles, width, height, show):
    cosmos = []
    canvas = np.zeros((width, height))
    for pt in range(N_Particles):
        [x, y] = utility.spawn_random_point(canvas)
        canvas[y, x] = 1
        cosmos.append(canvas)
    plt.imshow(canvas, 'gray_r')
    plt.show()
    return canvas, cosmos


def main():
    width = 250
    height = 250
    if '-manual' in sys.argv:
        width = int(input('Enter Width: '))
        height = int(input('Enter Height: '))

    space = initialize(1000, width, height, True)
    gravitational_field(10,space)

if __name__ == '__main__':
    main()