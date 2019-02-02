import matplotlib.pyplot as plt, matplotlib.animation as animation
import utility, numpy as np, time


class Medium:

    n_particles = 0
    size = 0
    state = [[]]

    def __init__(self, N, shape):
        self.n_particles = N
        self.size = shape
        self.state = self.seed_state()

    def seed_state(self):
        state = np.zeros((self.size, self.size))
        for pt in range(self.n_particles):
            point = utility.spawn_random_point(np.array(state))
            state[point[0], point[1]] = 1
        return state

    def wiggle(self, strength, trails):
        t0 = time.time()
        movements = list(np.random.randint(1, 10, self.n_particles*strength))
        motion = []
        f = plt.figure()
        for jiggle in range(strength):
            ii = 0
            state = self.state
            motion.append([plt.imshow(self.state, 'gray_r')])
            for cell in self.state.flatten():
                try:
                    pos = utility.ind2sub(ii, self.state.shape)
                    directions = {1: [pos[0] - 1, pos[1] - 1],
                                  2: [pos[0], pos[1] - 1],
                                  3: [pos[0] + 1, pos[1] - 1],
                                  4: [pos[0] - 1, pos[1]],
                                  5: pos,
                                  6: [pos[0] + 1, pos[1]],
                                  7: [pos[0] - 1, pos[1] + 1],
                                  8: [pos[0], pos[1] + 1],
                                  9: [pos[0] + 1, pos[1] + 1]}
                    if cell > 0:
                        if not trails:
                            state[pos[1], pos[0]] = 0
                        next_pos = directions[movements.pop()]
                        state[next_pos[1], next_pos[0]] = 1
                except IndexError:
                    break
                ii += 1
            self.state = state
        a = animation.ArtistAnimation(f, motion, 40, blit=True, repeat_delay=900)
        print "Simulation Finished in " + str(time.time()-t0)+'s\n'
        print "Rendering " + str(len(motion)) + " Frames "
        plt.show()


def main():
    gas = Medium(800, 100)
    gas.wiggle(40, False)


if __name__ == '__main__':
    main()
