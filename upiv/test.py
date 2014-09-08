#!/usr/bin/env python
import cv2
import numpy as np

img = cv2.imread('p88.bmp')
imgshape = (200,200,3)

simg = np.zeros(imgshape,dtype='uint8')
pimg = np.zeros(imgshape,dtype='uint8')

for r in range(imgshape[0]):
    for c in range(imgshape[1]):
        simg[r,c] = img[400+r,400+c]

lb = 31.5 
hb = lb+6
#hb = 50.5

for r in range(imgshape[0]):
    for c in range(imgshape[1]):
        if simg[r,c,0] < lb:
            pimg[r,c] = [0,0,0]
        elif simg[r,c,0] < hb:
            pimg[r,c] = simg[r,c]
        else:
            pimg[r,c] = [255,255,255]


cv2.imwrite('sample.bmp', simg)
cv2.imwrite('processed.bmp', pimg)
