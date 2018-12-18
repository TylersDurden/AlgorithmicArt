import sys, time, numpy as np, scipy.ndimage as ndi
import matplotlib.pyplot as plt, matplotlib.animation as animation


def render(matrices, isColor, speed):
    reel = []
    f = plt.figure()
    for frames in matrices:
        if isColor:
            reel.append([plt.imshow(frames)])
        else:
            reel.append([plt.imshow(frames, 'gray_r')])
    a = animation.ArtistAnimation(f, reel, interval=speed, blit=True, repeat_delay=500)
    plt.show()



