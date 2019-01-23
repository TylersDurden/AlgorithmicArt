import numpy as np, matplotlib.pyplot as plt
import os, imutils, time, scipy.ndimage as ndi


def merge_list(listA, listB):
    for element in listA:
        listB.append(element)
    return listB


def find_images():
    t0 = time.time()
    cmd0 = 'p=$PWD; cd /media; find -name *.png | cut -b 2- >> $p/imgs.txt; cd $p'
    cmd1 = 'p=$PWD; cd /home; find -name *.png | cut -b 2- >> $p/imgs.txt; cd $p'
    cmd2 = 'p=$PWD; cd /media; find -name *.jpg | cut -b 2- >> $p/imgs.txt; cd $p'
    cmd3 = 'p=$PWD; cd /home; find -name *.jpg | cut -b 2- >> $p/imgs.txt; cd $p'
    os.system(cmd0)
    images = imutils.swap('imgs.txt', True)
    os.system(cmd1)
    images = merge_list(imutils.swap('imgs.txt', True), images)
    os.system(cmd2)
    jpegs = merge_list(imutils.swap('imgs.txt', True), [])
    os.system(cmd2)
    jpegs = merge_list(imutils.swap('imgs.txt', True), jpegs)
    os.system(cmd3)
    jpegs = merge_list(imutils.swap('imgs.txt', True), jpegs)
    t1 = time.time()
    print str(len(images)) + " PNG Images and " + str(len(jpegs)) + \
                             " JPEGs Found in " + str(t1 - t0) + ' seconds'
    return images, jpegs


def sort_image_sizes(images):
    sizes = []
    for image in images:
        sizes.append(image.shape)


def error_diffusion(image):
    dith = np.zeros(image.shape)
    # TODO!!
    return dith


def bullseye(i1,i2,i3):
    RAW_IMAGE_DATA = np.array(i1).data
    '''
    Find the gradient, then find the regions that have regions of
    linear ramps and edges, and apply dots (dithering) accordingly
    [Vignetting maybe?]
    '''


def normalized_image_reduction(test_image, show):
    f0 = [[0, 0, 1], [0, 1, 0], [0, 0, 1]]
    avg_image = test_image[:, :, 0] / 3 + test_image[:, :, 1] / 3 + test_image[:, :, 2] / 3
    # Also return normalized channels
    c0 = test_image[:, :, 0] / 3
    c1 = test_image[:, :, 1] / 3
    c2 = test_image[:, :, 2] / 3
    Norm = (c0 + c1 + c2) * 255
    extra_detailed = ndi.convolve(Norm, f0)
    # Show the transformations
    if show:
        f, ax = plt.subplots(1, 4, figsize=(12,4),sharex=True, sharey=True)
        ax[0].imshow(avg_image)
        ax[1].imshow(Norm)
        ax[2].imshow(Norm - avg_image)
        ax[3].imshow(extra_detailed)
        plt.show()
    return avg_image, extra_detailed, Norm


def main():

    test_image = [[]]
    pngs, jpgs = find_images()

    DEBUG = True
    if DEBUG:
        # TODO: samples = sort_image_sizes(images=sample_imgs)
        img_root = '2f6d656469612f74796c65727364757264656e2f436f6f7065727344422f496d616765732f'
        sample_imgs = imutils.load_local_images(img_root)
        print str(len(sample_imgs)) + " Local Sample Images Loaded"
        test_image = plt.imread(str(img_root.decode('hex')) + 'SPACE.jpg')

    detailed_image, extra_detailed, NormalizedConv = normalized_image_reduction(test_image
                                                                                ,show=True)
    # TODO: error_diffusion(detailed_image)

    bullseye(detailed_image, extra_detailed, NormalizedConv)


if __name__ == '__main__':
    main()
