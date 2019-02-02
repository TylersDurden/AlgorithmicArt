import matplotlib.pyplot as plt, matplotlib.animation as animation
import numpy as np, scipy.ndimage as ndi
import imutils


class Drawing:

    width = 0
    height = 0
    state = [[]]

    features = {}

    def __init__(self, manual, shape):
        if manual:
            self.width = shape[0]
            self.height = shape[1]
        else:
            self.width = int(input('Enter a width: '))
            self.height = int(input('Enter a height: '))
        self.state = np.zeros((self.width, self.height))

    def spotty_region(self, x1, x2, y1, y2, N, state):
        dx = x2 - x1
        dy = y2 - y1
        A = np.zeros((dx, dy))
        for i in range(N):
            pt = imutils.spawn_random_point(A)
            A[pt[0],pt[1]] = 1
        state[x1:x2,y1:y2] = A
        return state


def main():
    d = Drawing(manual=True, shape=[250, 250])
    # Random Dot Patterns [ Not very good shading ]
    area_one = d.spotty_region(10, 50, 10, 50, 400, d.state)


if __name__ == '__main__':
    main()
