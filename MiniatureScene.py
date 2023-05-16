#Make an image blurrier on the outsides than the insides so that it looks
#like a miniature replica

import numpy as np
import matplotlib.pyplot as plt
import sys

import timeit       # for benchmarking

def image_load(filename):
    """Load an image file into an ndarray."""
    return plt.imread(filename)

def image_save(filename, img):
    """Save an image img into a file with a given name filename."""
    plt.imsave(filename, img)
    

def fmt_save_filename(origfilename, modif):
    """Format an image file name."""
    return "{}_{}.png".format(origfilename.split(".")[-2], modif)



def img_blur(img, weights):
    """ A faster implementation for weighted blurring with numpy.
    img is the image ndarray
    weights is the n x n matrix used for the convolution, i.e. the weights.
    """
    
    (h, w, _) = img.shape
    hoffsets = np.arange(weights.shape[1], dtype=np.int32) - int(weights.shape[1] / 2)
    voffsets = np.arange(weights.shape[0], dtype=np.int32) - int(weights.shape[0] / 2)
    sums = np.zeros(img.shape, dtype=np.float64)
    total_weight = 0
    for i in voffsets:
        for j in hoffsets:
            # print(i + int(weights.shape[0] / 2), j + int(weights.shape[1] / 2))
            weight = weights[i + int(weights.shape[0] / 2), j + int(weights.shape[1] / 2)] 
            total_weight += weight
            # slice ranges for img and for the blurred image array, sums
            tsum = (max(0, i),min(h + i, h), max(0,j), min(w+j, w))
            ta = (max(0,-i), min(h, h-i), max(0, -j), min(w-j,w))
            (sr0, sr1, sc0, sc1) = tsum
            (ar0, ar1, ac0, ac1) = ta
            # update weighted sum with the current slice and current weight:
            sums[sr0:sr1, sc0:sc1] += img[ar0:ar1, ac0:ac1].astype(np.float64) * weight
    # scale each pixel value by 1/total_weight
    b = (sums / total_weight).astype(np.uint8)  # convert pixel values to uint8
    return b


def show_imgs(*imgs):
    """ Display a sequence of images using matplotlib."""
    ncols = len(imgs)
    nrows = 1

    if len(imgs) > 1:
        (fig, axes) = plt.subplots(nrows=nrows, ncols=ncols)    # axes is  nrows x ncols axis ndarray
    
        k = 0
        for (axis, img) in zip(axes.flat, imgs):
            img = axis.imshow(img, interpolation='none')    # create subplot image
            axis.set_title("Image {}".format(k))
            axis.set_axis_off()     
            k += 1
    else:
        plt.imshow(imgs[0])
    plt.show()




def test3():
    fn = "florida-keys-800-480.jpg"
    img1 = image_load(fn)
    # img0n = img_blur0_naive(img1)
    weightsize = [25,20,5,3,3,5,20,25]
    newarr = np.array_split(img1, 8)  
   
    imgbs=[]
    for x in range(len(weightsize)):
        imgbs+=([img_blur(newarr[x], np.ones((weightsize[x], weightsize[x])))])
    z=np.concatenate((imgbs[0],imgbs[1],imgbs[2],imgbs[3],imgbs[4],imgbs[5],imgbs[6],imgbs[7]))
    print(type(z))
    
    plt.imshow(z)
    plt.show()
    
    saved_filename = fmt_save_filename(fn, "blurredpicture")
    image_save(saved_filename, z)
    print("File {} blurred and saved to {}.".format(fn, saved_filename))
    #show_imgs(*imgbs)
    

test3()