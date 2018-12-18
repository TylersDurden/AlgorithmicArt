import matplotlib.pyplot as plt, matplotlib.animation as ani
import sys, os, resource, numpy as np, scipy.ndimage as ndi


def check_mem_usage():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


def render(matrices, speedOfLife):
    f = plt.figure()
    reel = []
    for matrix in matrices:
        frame = plt.imshow(matrix,'gray_r')
        reel.append([frame])
    a = ani.ArtistAnimation(f, reel, interval=speedOfLife,blit=True,repeat_delay=1000)
    plt.show()
    ''' TODO: Add save2gif ability '''


def simulate(ngen, filter, seed):
    gen = 0
    generations = []

    while gen <= ngen:
        ii = 0
        world = ndi.convolve(seed,filter,origin=0)
        nextstate = seed.flatten()
        for cell in world.flatten():
            if cell == 42 or cell > 45:
                nextstate[ii] = 1
            if cell >= 32 and nextstate[ii] == 1:
                nextstate[ii] = 0
            if nextstate[ii] ==0 and cell == 22:
                nextstate[ii] = 1
            if nextstate[ii] == 1 and cell == 26:
                nextstate[ii]== 0
            if nextstate[ii] == 0 and cell == 1:
                nextstate[ii] = 1
            ii += 1

        seed = nextstate.reshape(seed.shape)
        generations.append(seed)
        gen += 1
    return generations


def crawler(density,ngenerations):
    # Create a random bit plane seed that is 100x100
    seed = np.array((np.random.randint(0, 128, 10000).reshape((100, 100)) > density), dtype=int)
    # Using a quirky little 7x7 kernel that tends to favor dense
    # edges or corners
    filter1 = [[2, 2, 2, 1, 2, 2, 2],
               [2, 1, 1, 1, 1, 1, 2],
               [2, 1, 0, 0, 0, 1, 1],
               [1, 1, 0, 1, 0, 1, 1],
               [2, 1, 0, 0, 0, 1, 1],
               [2, 1, 1, 1, 1, 1, 2],
               [2, 2, 2, 1, 2, 2, 2]]

    # Run the simulation using the seed and filter created above
    render(simulate(ngenerations, filter1, seed), 100)


def main():
    crawler(75, 95)
    crawler(82, 75)
    crawler(85, 150)
    crawler(95, 150)
    crawler(100, 150)


if __name__ == '__main__':
    main()
