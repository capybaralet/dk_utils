#TODO: add a list that contains names of all utils here (for reference)
#TODO: add docstrings
#TODO: add paths
#TODO: define test matrices for checking things!

import sys
import os
import time
import cPickle as pickle
import subprocess

import numpy
np = numpy
import numpy.random
from numpy import array as A
import scipy
from scipy.io import wavfile as wav

import matplotlib.pyplot as plt
import pylab
from pylab import *

import theano
import theano.tensor as T
from theano import function as F
from theano.tensor.shared_randomstreams import RandomStreams
from pylearn2.utils import serial


# This is how I was doing it before...
#
#    fl = sys._getframe(1).f_locals
#    fl['sys'] = sys

#_______________________________________________________________________________
# PLOTS

# made for visualization with matplotlib, esp FFTs.
def logsquash(arr):
    return np.log(arr - np.min(arr) + 1)

def mimshow(img, range=None, squash=False):
    # TODO: remove figure!
    #plt.figure()
    if squash:
        img = logsquash(img)
    if range is not None:
        vmin = range[0]
        vmax = range[1]
        plt.imshow(img, interpolation='none', cmap="Greys", vmin=vmin, vmax=vmax)
    else:
        plt.imshow(img, interpolation='none', cmap="Greys")

def mimsave(path, img, range=None, squash=False):
    plt.figure()
    mimshow(img, range, squash)
    plt.savefig(path)
    plt.close()


def mplots(list_of_vecs, maxnplots=25, background_vecs=None):
    plt.figure()
    nrows = min(int(len(list_of_vecs) ** .5), maxnplots)
    print "nrows=", nrows
    for i in range(nrows**2):
        plt.subplot(nrows, nrows, i+1)
        plt.plot(list_of_vecs[i])
        if background_vecs is not None:
            for vec in background_vecs:
                plt.plot(vec)

# modified from http://stackoverflow.com/questions/2459295/invertible-stft-and-istft-in-python
def stft(x, amp_phase=0, fs=1, framesz=320., hop=160.):
    """
     x - signal
     fs - sample rate
     framesz - frame size
     hop - hop size (frame size = overlap + hop size)
    """
    framesamp = int(framesz*fs)
    hopsamp = int(hop*fs)
    w = scipy.hamming(framesamp)
    X = scipy.array([scipy.fft(w*x[i:i+framesamp]) 
                     for i in range(0, len(x)-framesamp, hopsamp)])
    Xamp = np.abs(X)
    Xphase = np.angle(X)
    if amp_phase:
        return X, Xamp, Xphase
    else:
        return X


# from https://github.com/vdumoulin/sheldon
from numpy.lib.stride_tricks import as_strided
def segment_axis(a, length, overlap=0, axis=None, end='cut', endvalue=0):
    """Generate a new array that chops the given array along the given axis
    into overlapping frames.

    Parameters
    ----------
    a : array-like
        The array to segment
    length : int
        The length of each frame
    overlap : int, optional
        The number of array elements by which the frames should overlap
    axis : int, optional
        The axis to operate on; if None, act on the flattened array
    end : {'cut', 'wrap', 'end'}, optional
        What to do with the last frame, if the array is not evenly
        divisible into pieces. 

            - 'cut'   Simply discard the extra values
            - 'wrap'  Copy values from the beginning of the array
            - 'pad'   Pad with a constant value

    endvalue : object
        The value to use for end='pad'


    Examples
    --------
    >>> segment_axis(arange(10), 4, 2)
    array([[0, 1, 2, 3],
           [2, 3, 4, 5],
           [4, 5, 6, 7],
           [6, 7, 8, 9]])

    Notes
    -----
    The array is not copied unless necessary (either because it is
    unevenly strided and being flattened or because end is set to
    'pad' or 'wrap').

    use as_strided

    """

    if axis is None:
        a = np.ravel(a) # may copy
        axis = 0

    l = a.shape[axis]

    if overlap>=length:
        raise ValueError, "frames cannot overlap by more than 100%"
    if overlap<0 or length<=0:
        raise ValueError, "overlap must be nonnegative and length must be "\
                          "positive"

    if l<length or (l-length)%(length-overlap):
        if l>length:
            roundup = length + \
                      (1+(l-length)//(length-overlap))*(length-overlap)
            rounddown = length + \
                        ((l-length)//(length-overlap))*(length-overlap)
        else:
            roundup = length
            rounddown = 0
        assert rounddown<l<roundup
        assert roundup==rounddown+(length-overlap) or \
               (roundup==length and rounddown==0)
        a = a.swapaxes(-1,axis)

        if end=='cut':
            a = a[...,:rounddown]
        elif end in ['pad','wrap']: # copying will be necessary
            s = list(a.shape)
            s[-1]=roundup
            b = np.empty(s,dtype=a.dtype)
            b[...,:l] = a
            if end=='pad':
                b[...,l:] = endvalue
            elif end=='wrap':
                b[...,l:] = a[...,:roundup-l]
            a = b

        a = a.swapaxes(-1,axis)


    l = a.shape[axis]
    if l==0:
        raise ValueError, "Not enough data points to segment array in 'cut' "\
                          "mode; try 'pad' or 'wrap'"
    assert l>=length
    assert (l-length)%(length-overlap) == 0
    n = 1+(l-length)//(length-overlap)
    s = a.strides[axis]
    newshape = a.shape[:axis] + (n,length) + a.shape[axis+1:]
    newstrides = a.strides[:axis] + ((length-overlap)*s, s) + \
                 a.strides[axis+1:]

    try:
        return as_strided(a, strides=newstrides, shape=newshape)
    except TypeError:
        warnings.warn("Problem with ndarray creation forces copy.")
        a = a.copy()
        # Shape doesn't change but strides does
        newstrides = a.strides[:axis] + ((length-overlap)*s, s) + \
                     a.strides[axis+1:]
        return as_strided(a, strides=newstrides, shape=newshape)


# from http://www.iro.umontreal.ca/~memisevr/code/logreg.py
def onehot(x,numclasses=None):
    """ Convert integer encoding for class-labels (starting with 0 !)
        to one-hot encoding.
        The output is an array who's shape is the shape of the input array plus
        an extra dimension, containing the 'one-hot'-encoded labels.
    """
    if x.shape==():
        x = x[None]
    if numclasses is None:
        numclasses = x.max() + 1
    result = numpy.zeros(list(x.shape) + [numclasses], dtype="int")
    z = numpy.zeros(x.shape)
    for c in range(numclasses):
        z *= 0
        z[numpy.where(x==c)] = 1
        result[...,c] += z
    return result

# from http://glowingpython.blogspot.ca/2011/07/prime-factor-decomposition-of-number.html
from math import floor
def factor(n):
 result = []
 for i in range(2,n+1): # test all integers between 2 and n
  s = 0;
  while n/float(i) == floor(n/float(i)): # is n/i an integer?
   n = n/float(i)
   s += 1
  if s > 0:
   for k in range(s):
    result.append(i) # i is a pf s times
   if n == 1:
    return result

def shared_normal(num_rows, num_cols, scale=1):
    return theano.shared(numpy.random.normal(
        scale=scale, size=(num_rows, num_cols)).astype(theano.config.floatX))

def shared_zeros(*shape):
    return theano.shared(numpy.zeros(shape, dtype=theano.config.floatX))

def sigmoidd(x):
    return 1. / (1 + np.exp(-x))

def softmaxx(vec):
    expd = np.exp(vec)
    summ = np.sum(expd)
    return expd/summ

# "spherical softmax"
def ssoftmaxx(vec):
    vec = vec**2
    summ = np.sum(vec)
    return np.log(vec/summ)

def numnans(arr):
    return np.sum(np.isnan(arr))

def time_dhm(seconds):
    m = seconds / 60
    h = m / 60
    m = m % 60
    d = h / 24
    h = h % 24
    return str(d)+' days, '+str(h)+' hours, '+str(m)+' minutes'


def isin_name(var, substr):
    if substr in var.name:
        return True
    else:
        return False

def isin(str, substr):
    if substr in str:
        return True
    else:
        return False


def shortest(arr):
    return min(arr.shape)

def nprint(str):
    print '\n \n'
    print str
    print '\n \n'


# should make another copy for arrays!
def trim(list):
    """trim a list of lists down to the shortest length among them"""
    minlen = np.inf
    for i in list:
        if len(i) < minlen:
            minlen = len(i)
    mylist = []
    for i in list:
        mylist.append(i[:minlen])
    return mylist


def incorporate(list, list_or_element):
    """ If its a list, we want to add the elements,
        If its not, we want to add it"""
    if isinstance(list_or_element, list):
        list.extend(list_or_element)
    else:
        list.append(list_or_element)




#_______________________________________________________________________________
# WIPs


# WIP I need to figure out the scope better
# the idea is to use a global variable to turn all print statements on or off.
printing_on = 1
def mprint(str):
    if printing_on:
        print(str)
    else:
        pass

"""
# check if filename exists, if it does, load and return
# otherwise, make object from object_maker, and save as filename, and return


def saveload(filename, object_maker):
    import os
    if os.path.isfile(filename)
    return

if os.path.isfile(filename):
    return np.load(filename)
else:
    np.save(filename, object)
"""

""" WIP
def frame_size(shapes, strides):
    # both inputs are lists, in order from top to bottom
    fss = [1]
    fs = 1
    le = len(shapes)
    for i in range(le-1):
        fs += shapes[i]
        #fss.append(fs)
        fs += (shapes[i+1]-1)*strides[i]
"""


