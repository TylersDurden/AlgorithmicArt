import numpy as np, scipy.ndimage as ndi
import matplotlib.pyplot as plt
import utility, time


class Evolve:
    lifetime = 0
    state = [[]]
    kernel = [[]]
    k_threshold = 0
    score = 0

    def __init__(self, n_generation, seed, filter):
        self.lifetime = n_generation
        self.state = seed
        self.kernel = filter
        # self.set_target()

    def evolve(self):
        history = []
        for i in range(self.lifetime):
            history.append(np.array(self.state))
            self.run()
        return history

    def set_target(self, manual, val):
        if manual:
            self.k_threshold = int(input('Enter the threshold to use:'))
            print np.array(self.kernel)
        else:
            self.k_threshold = val

    def run(self):
        world = ndi.convolve(self.state, self.kernel)
        nextstate = np.array(self.state).flatten()
        ii = 0
        for cell in world.flatten():
            if cell >= self.k_threshold and nextstate[ii]==0:
                nextstate[ii] = 1
            ii += 1
        self.state = nextstate.reshape(np.array(self.state).shape)


def create_seed_image(density, dimensions):
    state = np.zeros(dimensions)
    pts = {}
    for i in range(density):
        pt = utility.spawn_random_point(state)
        state[pt[0],pt[1]] = 1
        pts[i] = pt
    return state, pts


def simulate(density, dims, thresh, t0):
    test_img, seed_pts = create_seed_image(density, dims)
    evo = Evolve(200, test_img, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    evo.set_target(False, thresh)
    history = evo.evolve()
    print '\033[33m\033[1m FINISHED SIMULATION \033[0m\033[1m[' + \
          str(time.time() - t0) + 's Elapsed]\033[0m'
    return history


def main():
    t0 = time.time()
    ''' 4 is highly complex  but fast '''
    history_5 = simulate(density=15000,dims=[350, 350], thresh=4, t0=t0)
    utility.bw_render(history_5, 100, True, 'unrestrained_decay.mp4')




if __name__ == '__main__':
    main()
