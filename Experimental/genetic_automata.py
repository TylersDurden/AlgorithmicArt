import numpy as np, scipy.ndimage as ndi
import utility, time


class KernelGen:
    N = 0
    kernel = [[]]

    def __init__(self, size, range):
        self.N = size
        self.kernel = self.generate(range)

    def generate(self, dr):
        return np.random.random_integers(0,0+dr,self.N*self.N).reshape((self.N, self.N))

    def random_refresh(self, dr):
        return self.generate(dr)


class StateSpace:

    width = 0
    height = 0
    state = [[]]

    def __init__(self, dims, bitdepth, is_random):
        self.width = dims[0]
        self.height = dims[1]
        if is_random:
            self.state = utility.random_seed(self.width,
                                             self.height,
                                             bitdepth)
        else:
            self.state = np.zeros(dims)


class Simulator:
    bit_depth = 0
    n_steps = 0
    generations = 0
    history = []

    kernel_params = {}

    def __init__(self, length, n_trials, dims,
                 bitdepth, israndom, hyperparams):
        self.n_steps = length
        self.generations = n_trials
        self.bit_depth = bitdepth
        self.kernel_params = hyperparams
        test_kernels = self.generate_random_kernels()
        self.simulate(dims,bitdepth,israndom, test_kernels)

    def simulate(self, dims,bitdepth,is_random, test_kernels):
        print '\033[1m\033[33m[Simulation Started]\033[0m'
        t0 = time.time()
        k_thresh = self.kernel_params['k_thresh']
        for trial in range(self.generations):
            k = test_kernels.pop()
            state_space = StateSpace(dims, bitdepth, is_random).state
            for step in range(self.n_steps):
                self.history.append(state_space)
                nextstate = np.array(state_space).flatten()
                ii = 0
                for cell in ndi.convolve(state_space, k).flatten():
                    if cell >= k_thresh and nextstate[ii] == 1:
                        nextstate[ii] = 0
                    elif cell == k_thresh and nextstate[ii] == 0:
                        nextstate[ii] = 1
                state_space = np.array(nextstate).reshape(np.array(state_space).shape)
                self.history.append(state_space)
        print '\033[1m\033[33mSimulation FINISHED [' + str(time.time()-t0)+'s Elapsed]\033[0m'
        print 'Rendering ' + str(len(self.history)) + " Frames"
        utility.render(self.history, 5, False, True)

    def generate_random_kernels(self):
        test_kernels = []
        for i in range(self.generations):
            test_kernels.append(KernelGen(3, self.generations).kernel)
        return test_kernels


def main():
    Simulator(length=100, n_trials=10, dims=[250, 250],
              bitdepth=2, israndom=True, hyperparams={'k_thresh': 2})

    

if __name__ == '__main__':
    main()
