import matplotlib.pyplot as plt
import numpy

def save_img(fname, arr):
  plt.imsave(fname, numpy.array(arr).reshape((28, 28)))