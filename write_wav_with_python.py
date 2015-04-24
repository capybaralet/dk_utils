import numpy
np = numpy
from scipy.io import *

dat = loadmat('/u/kruegerd/compare_wavwrite_matlab_python.mat')

print type(dat)
print np.std(dat)

wavfile.write('/u/kruegerd/python_wavwrite_compare.wav', 16000, dat.astype('int16'))









