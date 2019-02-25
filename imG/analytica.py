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


def main():
    jpegs, pngs = imutils.find_local_images()
    print str(len(jpegs)) + " JPEGs Found"
    print str(len(pngs)) + " PNGs Found"
    edges = basic_edge_detector(jpegs)


if __name__ == '__main__':
    main()
