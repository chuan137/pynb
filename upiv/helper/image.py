import numpy

def crop(srcimg, cropx, cropy, sizex, sizey=0):
    if sizey == 0:
        sizey = sizex
    img = numpy.copy(srcimg[cropy:sizey+cropy, cropx:sizex+cropx])
    return img

def filter_hist(img, c0, c1):
    shape = img.shape
    output = numpy.zeros((shape[0],shape[1],3), dtype='uint8')
    for y in range(shape[0]):
        for x in range(shape[1]):
            if img[y,x] < c0 or img[y,x] >= c1:
                output[y,x] = [0,0,0]
            else:
                output[y,x] = [img[y,x], img[y,x], img[y,x]]
    return output
