import utility, numpy as np, scipy.ndimage as ndi


class Kernels:

    f0 = [[1,1,1],
          [1,1,1],
          [1,1,1]]

    f1 = [[1,1,1],
          [1,0,1],
          [1,1,1]]

    f2 = [[1,1,1],
          [0,0,0],
          [1,1,1]]

    f3 = [[1,0,1],
          [1,0,1],
          [1,0,1]]

    c1 = [[1,1,0],
          [1,0,0],
          [0,0,0]]

    c2 = [[0,1,1],
          [0,0,1],
          [0,0,0]]

    c3 = [[0,0,0],
          [0,0,1],
          [0,1,1]]

    c4 = [[0,0,0],
          [1,0,0],
          [1,1,0]]

    i0 = [[0,1,0],
          [1,0,1],
          [0,1,0]]

    i1 = [[0,1,0],
          [1,1,1],
          [0,1,0]]

    b0 = [[0,0,0,0,0],
          [0,1,1,1,0],
          [0,1,1,1,0],
          [0,1,1,1,0],
          [0,0,0,0,0]]

    shape = []

    filters = {}

    def __init__(self, dims):
        self.shape = dims
        self.initialize()

    def initialize(self):
        self.filters = {'f0':self.f0,
                        'f1':self.f1,
                        'bh':self.f2,
                        'bv':self.f3,
                        'c1':self.c1,
                        'c2':self.c2,
                        'c3':self.c3,
                        'c4':self.c4,
                        'i0':self.i0,
                        'i1':self.i1,
                        'b0':self.b0}

    def filter_check(self, seed):
        test = list()
        test.append(seed)
        test.append(ndi.convolve(seed, self.filters['c1']))
        test.append(ndi.convolve(seed, self.filters['c2']))
        test.append(ndi.convolve(seed, self.filters['c3']))
        test.append(ndi.convolve(seed, self.filters['c4']))
        test.append(ndi.convolve(seed, self.filters['f0']))
        test.append(ndi.convolve(seed, self.filters['f1']))
        test.append(ndi.convolve(seed, self.filters['bh']))
        test.append(ndi.convolve(seed, self.filters['bv']))
        test.append(ndi.convolve(seed, self.filters['i0']))
        test.append(ndi.convolve(seed, self.filters['i1']))
        test.append(ndi.convolve(seed, self.filters['b0']))
        # Show the Image Kernels used
        utility.filter_preview(self.filters)
        # Show a rendering of the seed image being run
        # through each of the filters
        utility.render(test, 200, False, True)
        return test


class Automata:
    dims = []
    state = [[]]
    lens = [[]]
    avg_global = 0
    lifetime = 0

    def __init__(self, ngen, state, kernel):
        self.state = state
        self.dims = state.shape
        self.lifetime = ngen
        self.lens = kernel
        self.avg_global = np.array(kernel).mean() + 1

    def run(self, rules):
        gen = 0
        generations = list()
        while gen < self.lifetime:
            world = ndi.convolve(self.state, self.lens)
            self.state = self.state.flatten()
            i = 0
            for cell in world.flatten():
                # AVERAGER #
                if 'avg' in rules:
                    if cell >= 2*self.avg_global and self.state[i] == 0:
                        self.state[i] = 1
                    if cell < 4 and self.state[i]==1:
                        self.state[i] = 0
                    if self.state[i] == 0 and cell >= 4:
                        self.state[i] = 1
                i += 1
            self.state = self.state.reshape(self.dims)
            generations.append(self.state)
            gen += 1
        return generations

def main():

    seed = utility.random_seed(100, 100, 1)

    iKernels = Kernels(seed.shape)
    iKernels.filter_check(seed)

    meany = Automata(530, seed, iKernels.filters['b0'])
    simulation0 = meany.run({'avg': True})

    utility.render(simulation0, 20, False, True)

if __name__ == '__main__':
    main()
