import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import util
import sys


def mazy_echoes(cloud, cloud_data, generations):
    g0 = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    g1 = np.array([[1,1,0,0,1,1],
          [1,1,0,0,1,1],
          [1,1,0,0,1,1],
          [0,0,0,0,0,0],
          [1,1,0,0,1,1],
          [1,1,0,0,1,1]])

    simulation = []

    for generation in range(generations):
        w0 = ndi.convolve(cloud, g0, origin=0)
        w1 = ndi.convolve(cloud, g1, origin=0)
        beat = w1 - w0
        cloud = cloud.flatten()
        ii = 0
        minima = np.array(beat).min()
        maxima = np.array(beat).max()
        average = np.array(beat).mean()
        for cell in beat.flatten():
            if cell <= average and cell > minima:
                cloud[ii] += 1
            if cell >= average and cell < maxima:
                cloud[ii] -= 1
            if cell == average or cell == minima or cell == maxima:
                cloud[ii] = 1
            ii += 1
        cloud = cloud.reshape(beat.shape)
        simulation.append(cloud)
    return simulation


def clustering(cloud, cloud_data, generations):
    g0 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    g1 = np.array([[1,1,0,0,1,1],
                  [1,1,0,0,1,1],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [1,1,0,0,1,1],
                  [1,1,0,0,1,1]])

    simulation = []

    for generation in range(generations):
        w0 = ndi.convolve(cloud, g0, origin=0)
        w1 = ndi.convolve(cloud, g1, origin=0)
        beat = w1 - w0
        cloud = cloud.flatten()
        ii = 0
        minima = np.array(beat).min()
        maxima = np.array(beat).max()
        average = np.array(beat).mean()
        for cell in beat.flatten():
            if cell <= average and cell > minima:
                cloud[ii] -= 1
            if cell >= average and cell < maxima:
                cloud[ii] += 1
            if cell == average or cell == minima or cell == maxima:
                cloud[ii] = -1
            ii += 1
        cloud = cloud.reshape(beat.shape)
        simulation.append(cloud)
    return simulation


def resonanct_dissolve(cloud,generations):
    g0 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    g1 = np.array([[1, 1, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1]])

    simulation = []

    for generation in range(generations):
        w0 = ndi.convolve(cloud, g0, origin=0)
        w1 = ndi.convolve(cloud, g1, origin=0)
        beat = w1 - w0
        cloud = cloud.flatten()
        ii = 0
        minima = np.array(beat).min()
        maxima = np.array(beat).max()
        average = np.array(beat).mean()
        for cell in beat.flatten():
            if cell <= average and cell > minima:
                cloud[ii] -= 1
            if cell >= average and cell < maxima:
                cloud[ii] += 1
            if cell == maxima:
                cloud[ii] /= 2
            ii += 1
        cloud = cloud.reshape(beat.shape)
        simulation.append(cloud)
    return simulation


def main():
    light_square, square_group = util.create_point_cloud(250, 100, 250, False)
    galactic, pt_cloud = util.create_round_point_cloud(550, 300, 100, False)

    # Do one simulation
    if 'melt' in sys.argv:
        melting = clustering(galactic, pt_cloud, 80)
    if 'trip' in sys.argv:
        ripples = mazy_echoes(galactic,pt_cloud, 100)
    if 'ice' in sys.argv:
        wiggles = resonanct_dissolve(galactic, 100)

    # util.bw_render(melting, 225, False, '')
    util.bw_render(wiggles, 225, True, 'big_bang_3.mp4')


if __name__ == '__main__':
    main()
