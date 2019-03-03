#!/usr/bin/env python
import numpy as np, scipy.ndimage as ndi
import matplotlib.pyplot as plt
import sys, imutils, generaxia


def basic_edge_detector(jpegs):
    contours = dict()
    for jpeg in jpegs:
        try:
            random_imat = plt.imread(jpeg)
        except IOError:
            pass
        edges = np.zeros(random_imat.shape)
        if len(edges.shape) ==3:
            edges[:, :, 0] = ndi.laplace(random_imat[:, :, 1])
            edges[:, :, 1] = ndi.gaussian_filter(random_imat[:, :, 0], sigma=1)
            edges[:, :, 2] = ndi.gaussian_laplace(imutils.sharpen(random_imat[:, :, 2], 3), sigma=1)
            # imutils.filter_preview({'Original': random_imat, 'Edges': edges})
            contours[jpeg] = edges
    return contours


def choose_random_image(images):
    domain = np.random.random_integers(0,len(images),1)[0]
    return plt.imread(images[domain])


def main():
    jpegs, pngs = imutils.find_local_images()
    print str(len(jpegs)) + " JPEGs Found"
    print str(len(pngs)) + " PNGs Found"

    if '-edges' in sys.argv:
        edges = basic_edge_detector(jpegs)

    if '-test' in sys.argv:
        test_image = choose_random_image(jpegs)

        k1 = [[0,0,1],
              [0,1,0],
              [-1,0,1]]

        k2 = [[0, -1, 0],
              [-1, 2, -1],
              [0, -1, 0]]

        edge_test = np.zeros(test_image.shape)
        gol0 = ndi.gaussian_laplace(test_image[:,:,0], sigma=1)
        gol1 = ndi.laplace(ndi.convolve(test_image[:,:,1],k1))
        gol2 = ndi.gaussian_laplace(ndi.convolve(test_image[:,:,2],k2), sigma=1)
        edge_test[:,:,0] = ndi.convolve(test_image[:,:,0],[[0,0,0],[0,2,0],[0,0,0]])
        edge_test[:,:,1] = gol1
        edge_test[:,:,2] = gol2/255
        f, ax = plt.subplots(1,4, figsize=(10, 5), sharex=True)
        ax[0].imshow(test_image)
        ax[1].imshow(test_image-edge_test, 'gray')
        ax[2].imshow(gol1, 'gray')
        ax[3].imshow(gol0, 'gray')
        plt.show()


if __name__ == '__main__':
    main()
