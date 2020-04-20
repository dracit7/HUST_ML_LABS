
import os
import numpy
import matplotlib.pyplot as plt

import knn
import utils

# Currently the main program is a simple script to
# run the knn algorithm on MNIST dataset.
if __name__ == "__main__":
  test_range = 10
  k_range = [20]
  img_dir = 'tmp/img'

  # Read the mnist dataset into memory.
  mnist = utils.mnist_reader(
    "data/train-images-idx3-ubyte",
    "data/train-labels-idx1-ubyte",
    "data/t10k-images-idx3-ubyte",
    "data/t10k-labels-idx1-ubyte"
  )
  print("Training set size: %d" % mnist.train_set_sz)
  print("Testing set size: %d" % mnist.test_set_sz)
  print("Image size: %d*%d" % (mnist.height, mnist.width))

  # Run KNN algo on MNIST dataset and collect
  # misclassification rate information.
  x = []
  y = []
  for k in k_range:
    correct_cnt = 0
    for i in range(test_range):

      # Dump tested images to test_dir if necessary.
      test_dir = ''
      if img_dir != '':
        test_dir = os.path.join(img_dir, 'test_%d' % i)
        if not os.path.isdir(test_dir):
          os.mkdir(test_dir)
        utils.save_img('%s/test.png' % test_dir, mnist.test_data_set[i])

      # Run the knn algorithm and compare the result.
      result = (knn.knn(
        k,
        mnist.test_data_set[i],
        mnist.train_data_set,
        mnist.train_label_set,
        test_dir
      )[0] == mnist.test_label_set[i])
      if result:
        correct_cnt += 1

    # Collect plotting information.
    x.append(k)
    y.append((test_range - correct_cnt) / test_range * 100)
    
  # plotting
  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.set_xlabel('k')
  ax.set_ylabel('misclassification rate (%)')
  ax.set_title('The misclassification rate of KNN algorithm on MNIST dataset')
  fig.savefig('tmp/img/rate.png')

