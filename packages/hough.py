import numpy as np
from .helpers import grid
import cv2

def hough_kernel(rmin=5, rmax=20, x=64, y=64, rs=2, rt=4, gw=0, gsig=6, gh=1.5):
    """generate ring pattern
    @input rmin, rmax
        minimum or maximum ring size
    @input x, y
        size of output image
    @input rs
        step in ring size
    @input rt
        ring thickness
    @input gw, gsig, gh
        gaussian width, sigma and height for fuzzy HT
    """
    ring_sizes = range(rmin, rmax+1, rs)
    img = np.zeros((len(ring_sizes), x , y))
    for i, r in enumerate(ring_sizes):
        cv2.circle(img[i], (x/2, y/2), r, color=255, thickness=rt)
    if gw > 0:
        fimg = np.copy(img)
        kern = np.zeros(2*gw+1)
        for p in range(gw+1):
            kern[gw+p] = gh * np.exp(-p**2 / gsig**2)
            kern[gw-p] = kern[gw+p]
        for x, y in grid(*img.shape[1:]):
            fimg[:,x,y] = np.convolve(img[:,x,y], kern, mode='same')
        img = fimg
    return img

