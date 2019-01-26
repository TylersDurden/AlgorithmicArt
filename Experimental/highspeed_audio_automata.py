import numpy as np, scipy.ndimage as ndi
import matplotlib.pyplot as plt


def instant_annealer(state, depth, isRendering):
    f0 = [[1,1,1],[1,0,1],[1,1,1]]

    f1 = [[1,1,0,1,1],
          [1,0,0,0,1],
          [0,0,1,0,0],
          [1,0,0,0,1],
          [1,1,0,1,1]]
    dims = state.shape
    data = []
    for frame in range(depth):
        conv = ndi.convolve(state,f1)
        state = state.flatten()
        ii = 0
        for cell in conv.flatten():
            if cell > 3:
                state[ii] = 0
            state = state.reshape(dims)
            if isRendering:
                data.append([plt.imshow(data.append(state), 'gray')])
            else:
                data.append(state)
    return data