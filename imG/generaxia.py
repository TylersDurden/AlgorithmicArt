import imutils, scipy.ndimage as ndi
import numpy as np


class generative:
    dimensions = []
    state = [[]]
    kernels = {}
    slices = {}

    def __init__(self, dims, state):
        self.dimensions = dims
        self.state = state
        self.slices = self.divisions(4)

    def examine_center(self):
        padx = np.array(self.state).shape[0]/5
        pady = np.array(self.state).shape[1]/5
        world = np.array(self.state)
        data = world[padx:world.shape[0]-padx, pady:world.shape[1]-pady]
        return data

    def divisions(self, ndiv):
        squares = {}
        qunatax = int(np.array(self.state).shape[0]/ndiv)
        quantay = int(np.array(self.state).shape[1] / ndiv)
        dx = np.linspace(0, np.array(self.state).shape[0], ndiv)
        dy = np.linspace(0, np.array(self.state).shape[1], ndiv)
        ii = 0
        for x in dx:
            for y in dy:
                row = int(x)
                col = int(y)
                try:

                    box = self.state[row - qunatax:row, col - quantay:col]
                    if np.array(box).shape[0]*np.array(box).shape[1] > 0:
                        squares[ii] = box
                        ii += 1
                except IndexError:
                    pass
        return squares

    def slice_eval(self):
        edges = {}
        ii = 0
        for space in self.slices.keys():
            state = np.array(self.slices[space])
            minima = state.min()
            maxima = state.max()
            averge = state.mean()
            edges[ii] = 10*ndi.gaussian_laplace(state, sigma=1)
            ii += 1
        imutils.filter_preview(edges)


def main():
    dims = [250, 250]
    state = imutils.draw_centered_circle(np.zeros(dims), 100, False)
    g = generative(dims, state)
    imutils.filter_preview(g.slices)
    g.slice_eval()

if __name__ == '__main__':
    main()
