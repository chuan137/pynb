import numpy as np
import matplotlib.pyplot as plt

def grid(a, b):
    from itertools import product
    return product(range(a), range(b))

def show_images(*ary, **kargs):
    col = len(ary)
    size = kargs.get('size', 4)
    colormap = kargs.get('cmap', 'RdBu_r')
    fig, axes = plt.subplots(nrows=1, ncols=col, figsize=(size*col, size))
    if col == 1:
        axes = [axes]
    for i, d in enumerate(ary):
        axes[i].imshow(d, cmap=colormap, interpolation="nearest")
        axes[i].get_xaxis().set_ticks([])
        axes[i].get_yaxis().set_ticks([])
    return fig, axes


