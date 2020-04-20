
import os
import gzip

from numpy import *

class mnist_reader:

  ## Read the mnist image data to memory
  def __init__(self, train_f, train_label_f, test_f, test_label_f):

    # Read the training set
    with gzip.open(train_f, "rb") as f:

      # Read the file header
      f.read(4) # Skip the magic number
      self.train_set_sz = int.from_bytes(f.read(4), byteorder='big')
      self.height = int.from_bytes(f.read(4), byteorder='big')
      self.width = int.from_bytes(f.read(4), byteorder='big')

      # Read the data
      self.train_data_set = array([ \
        [ 0 for x in range(self.height * self.width)] \
            for y in range(self.train_set_sz)])
      for i in range(0, self.train_set_sz):
        self.train_data_set[i] = fromstring(f.read(self.height*self.width), uint8)

    # Read the testing set
    with gzip.open(test_f, "rb") as f:

      # Read the file header
      f.read(4) # Skip the magic number
      self.test_set_sz = int.from_bytes(f.read(4), byteorder='big')
      assert(self.height == int.from_bytes(f.read(4), byteorder='big'))
      assert(self.width == int.from_bytes(f.read(4), byteorder='big'))

      # Read the data
      self.test_data_set = array([ \
        [ 0 for x in range(self.height * self.width)] \
            for y in range(self.test_set_sz)])
      for i in range(0, self.test_set_sz):
        self.test_data_set[i] = fromstring(f.read(self.height*self.width), uint8)

    # Read the testing label set
    with gzip.open(train_label_f, "rb") as f:

      # Read the file header
      f.read(4) # Skip the magic number
      assert(self.train_set_sz == int.from_bytes(f.read(4), byteorder='big'))

      # Read the data
      self.train_label_set = \
        ['0' for x in range(0, self.train_set_sz)]
      self.train_label_set = fromstring(f.read(self.train_set_sz), uint8)

    # Read the testing label set
    with gzip.open(test_label_f, "rb") as f:

      # Read the file header
      f.read(4) # Skip the magic number
      assert(self.test_set_sz == int.from_bytes(f.read(4), byteorder='big'))

      # Read the data
      self.test_label_set = \
        ['0' for x in range(0, self.test_set_sz)]
      self.test_label_set = fromstring(f.read(self.test_set_sz), uint8)

