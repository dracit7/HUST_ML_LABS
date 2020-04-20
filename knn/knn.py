import utils

from operator import itemgetter
from numpy import *

def knn(k, test_set, train_set, train_labels, imgdir=''):

  # Get the sorted vector of distances between test cases and
  # all points in the train set.
  distances = ((
    (tile(test_set, [len(train_set), 1]) - train_set)
    ** 2).sum(axis=1) ** 0.5).argsort()
  
  # Count the number of images in each class using knn algo.
  classes = dict(zip(
    train_labels, [0 for i in range(len(train_labels))]))
  for i in range(k):
    if imgdir != '':
      utils.save_img(
        '%s/%d_nearest.png' % (imgdir, i),
        train_set[distances[i]])
    classes[train_labels[distances[i]]] += 1
  
  # Return the class with the biggest size.
  return sorted(
    classes.items(),
    key=itemgetter(1), # Use the number of members as key
    reverse=True # Pick the biggest class
  )[0]