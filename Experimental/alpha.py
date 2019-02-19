import utility, numpy as np, matplotlib.pyplot as plt
import scipy.ndimage as ndi


def filter_test(image, debug, kernel):

    t0 = ndi.convolve(image, kernel)
    if debug:
        print 'Max: ' + str(image.max()) + '->' + str(np.array(t0).max())
        print 'Min: ' + str(image.min()) + '->' + str(np.array(t0).min())
        print 'Mean: ' + str(image.mean()) + '->' + str(np.array(t0).mean())
        print 'Dev :' + str(np.array(image).std()) + '->' + str(np.array(t0).std())
        plt.imshow(t0, 'gray')
        plt.show()
    return t0


def sample_state_gen(dims, kernel):
    width = dims[0]
    height = dims[1]
    circle_seed = utility.draw_centered_circle(np.zeros(dims), width / 3, False)
    box_seed = utility.draw_centered_box(np.zeros(dims), 50, 10, False)
    random_seed = utility.random_seed(width, height, 2)

    conv_circ = filter_test(circle_seed, False, kernel)
    conv_rand = filter_test(random_seed, False, kernel)
    cbox_seed = utility.draw_centered_box(filter_test(circle_seed, False, kernel), width / 5, conv_circ.mean() / 3, False)
    shapes = {'circle':circle_seed,
              'box':box_seed,
              'random':random_seed,
              'conv_circ':conv_circ,
              'conv_rand':conv_rand,
              'circbox': cbox_seed}
    return shapes


def create_miniverse(test_image):
    # Now generate some psuedo random cell decay to
    # eventually have life feed off of
    c1 = ndi.convolve(test_image, np.ones((3, 3)))
    conv_egg = 10*ndi.gaussian_laplace(test_image, sigma=1)

    # Seperate the unique nums
    cavg = conv_egg.mean()
    cmax = conv_egg.max()
    cmin = conv_egg.min()
    cstd = conv_egg.std()

    print 'avg: '+ str(cavg) + '/ max: '+ str(cmax) +\
          ' / min: ' + str(cmin) + ' / std_dev.' + str(cstd)
    print '------------------------------------------------------------------------------------'

    bins = {}
    for i in range(int(cmin), int(cmax)+1):
        bins[i] = 0
    counts = {}
    for cell in conv_egg.flatten():
        bins[int(cell)] += 1
        counts[bins[int(cell)]] = int(cell)
    print np.array(bins.values()).min()
    print np.array(bins.values()).max()
    print np.array(bins.values()).min()
    print np.array(bins.values()).std()
    print '------------------------------------------------------------------------------------'

    f, ax = plt.subplots(1,2)
    ax[0].bar(bins.keys(), bins.values())
    ax[1].imshow(conv_egg, 'gray')
    plt.show()
    return conv_egg


def main():
    e0 = [[1, 1, 1, 1, 1],
          [1, 2, 2, 2, 1],
          [1, 2, 0, 2, 1],
          [1, 2, 2, 2, 1],
          [1, 1, 1, 1, 1]]

    e1 = [[1, 1, 1, 0, 0],
          [1, 2, 2, 0, 0],
          [1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

    dims = [250, 250]
    shapes = sample_state_gen(dims, e0)
    # utility.filter_preview(shapes)

    # Generate Test Maps
    simple_test_image = shapes['conv_circ']
    complx_test_image = shapes['circbox']
    simple_life = create_miniverse(simple_test_image)
    complexity = create_miniverse(complx_test_image)


if __name__ == '__main__':
    main()

