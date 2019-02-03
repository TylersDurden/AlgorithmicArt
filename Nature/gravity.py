import matplotlib.pyplot as plt, matplotlib.animation as ani, scipy.ndimage as ndi
import sys, utility, time, numpy as np


def gravitational_field(strength, state):
    g0 = np.array([[1,1,1],[1,1,1],[1,1,1]])
    g1 = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
    g2 = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])

    fields = {1: ndi.convolve(np.array(state), g0),
              2: ndi.convolve(np.array(state), g1),
              3: ndi.convolve(np.array(state), g2)}

    # utility.filter_preview(fields)
    data = []
    for i in range(strength):
        world = state.flatten()
        ii = 0
        for cell in fields[1].flatten():
            if cell > 1:
                world[ii] = 1
            ii += 1
        state = world.reshape(state.shape)
        data.append(state)
        ii = 0
        for c2 in fields[2].flatten():
            if c2 > 1:
                world[ii] = 1
            ii += 1
        ii = 0
        state = world.reshape(state.shape)
        data.append(state)
        for c3 in fields[3].flatten():
            if c3 > 1:
                world[ii] = 1
            ii += 1
        state = world.reshape(state.shape)
        data.append(state)
    return data


def initialize(n_particles, width, height, show):
    cosmos = []
    canvas = np.zeros((width, height))
    for pt in range(n_particles):
        [x, y] = utility.spawn_random_point(canvas)
        canvas[y, x] = 1
        cosmos.append(canvas)
    if show:
        plt.imshow(canvas, 'gray_r')
        plt.show()
    return canvas, cosmos


def main():
    width = 250
    height = 250
    if '-manual' in sys.argv:
        width = int(input('Enter Width: '))
        height = int(input('Enter Height: '))

    space, history = initialize(1500, width, height, False)
    data = gravitational_field(200,space)
    utility.bw_render(data,40,False,'')


if __name__ == '__main__':
    main()