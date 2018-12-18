import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as animation
import scipy.ndimage as ndi, time


def render(matrices, speedOfLife):
    f = plt.figure()
    reel = []
    for matrix in matrices:
        frame = plt.imshow(matrix,'gray_r')
        reel.append([frame])
    a = animation.ArtistAnimation(f, reel, interval=speedOfLife,blit=True,repeat_delay=1000)
    plt.show()


cross = [[0,0,0,0,1,1,1,0,0,1,1],
           [0,0,0,0,1,1,1,0,0,1,1],
           [0,0,0,0,1,1,1,0,0,0,1],
           [0,1,0,0,1,1,1,0,0,0,0],
           [0,1,1,1,1,1,1,1,1,1,1],
           [0,1,0,1,0,1,1,1,1,1,1],
           [0,0,0,0,1,1,1,0,0,0,0],
           [0,0,0,0,1,1,1,0,0,0,0],
           [0,0,0,0,1,1,1,0,0,0,0],
           [0,0,0,0,1,1,1,0,0,1,1],
           [0,0,0,0,1,1,1,0,0,0,1]]

A = [[1,1,1,0,0,0,0,1,1,1],
     [1,1,0,0,0,0,0,0,1,1],
     [1,0,0,0,1,1,0,0,0,1],
     [0,0,0,1,1,1,1,0,0,0],
     [0,0,1,1,1,1,1,1,0,0],
     [0,0,1,1,1,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,1,1,1,0,0,0],
     [0,0,0,1,1,1,1,0,0,0]]


B = [[1,0,0,0,0,0,0,0,1,1],
     [1,0,0,1,1,1,0,0,0,1],
     [1,0,0,1,1,1,1,0,0,1],
     [1,0,0,1,1,1,1,0,0,1],
     [1,0,0,1,1,1,0,0,0,1],
     [1,0,0,0,0,0,0,0,1,1],
     [1,0,0,0,0,0,0,0,1,1],
     [1,0,0,1,1,1,0,0,0,1],
     [1,0,0,1,1,1,1,0,0,1],
     [1,0,0,1,1,1,0,0,0,1],
     [1,0,0,0,0,0,0,0,1,1]]


def simulation_one(ngen,seed):
    gen = 0
    generations = []

    neighbors = [[1,1,1],
                 [1,0,1],
                 [1,1,1]]
    while gen <= ngen:
        density = ndi.convolve(seed, neighbors)
        nextstate = seed.flatten()
        II = 0
        for cell in density.flatten():
            if nextstate[II] == 1:
                if 4 > cell > 2:
                    nextstate[II] = 1
                else:
                    nextstate[II] = 0
            else:
                if cell > 2:
                    nextstate[II] = 1
                else:
                    nextstate[II] = 0
            II += 1

        seed = nextstate.reshape((seed.shape[0], seed.shape[1]))
        generations.append(seed)
        gen += 1
    render(generations,500)
    return generations


def simulation_two(ngen, seed):
    gen = 0
    generations = []
    conv = [[3,3,3,3,3],
            [3,2,2,2,3],
            [3,2,1,2,3],
            [3,2,2,2,3],
            [3,3,3,3,3]]
    phase = np.zeros((seed.shape)).flatten()
    start = time.time()
    while gen <= ngen:
        world = ndi.convolve(seed, conv)
        next = seed.flatten()
        II = 0
        for cell in world.flatten():
            if next[II] == 1:
                if cell > world.mean():
                    next[II] = 1
                    phase[II] += 1
                else:
                    next[II] = 0
                    #phase[II] += 1
            elif next[II] > world.mean():
                next[II] = 1
                #phase[II] += 1
            # Source of decay
            if phase[II] > 60 and next[II] == 1:
                next[II] = 0
                phase[II] -= 1
            # Pops particles from ether
            if phase[II] > 30 and next[II] == 0:
                next[II] = 1
            # source of growth
            if cell > 5:
                phase[II] += 1
            if cell < world.mean():
                phase[II] -= 1
            if phase[II] < 0:
                next[II] = 1

            II += 1
        seed = next.reshape((seed.shape[0],seed.shape[1]))
        generations.append(seed)
        gen += 1
    print " READY TO SHOW [render time " + str(time.time() - start) + "s]"
    return generations


def main():

    # inkBlotter = simulation_one(100, np.array(A))
    # mazerunner = simulation_one(200, np.array(B))
    # mazerunner2 = simulation_one(100, np.array(cross))

    render(simulation_two(100, np.random.randint(0,2,10000).reshape((100,100))),200)


if __name__ == '__main__':
    main()