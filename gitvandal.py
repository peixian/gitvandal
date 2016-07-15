from scipy import misc
import matplotlib.pyplot as plt
import sys
import numpy as np

#read the image
img = misc.imread("{}".format(sys.argv))
#ravel the numpy array
out_array = np.zeros([7,45])
#displace each val after sampling each value

#convert to github intensity (0-4) values

#feed into new array, pass into gitfiti
