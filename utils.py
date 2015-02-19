
import numpy
np = numpy

import theano


#TODO: add a list that contains names of all utils here (for reference)
#TODO: add docstrings
#TODO: add paths

#TODO? Can I just put everything I want to load in ip.py in here???
#TODO: define test matrices for checking things!

#TODO: onehot
# from http://www.iro.umontreal.ca/~memisevr/code/logreg.py
def onehot(x,numclasses=None):
    """ Convert integer encoding for class-labels (starting with 0 !)
        to one-hot encoding. 
      
        If numclasses (the number of classes) is not provided, it is assumed 
        to be equal to the largest class index occuring in the labels-array + 1.
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



def shared_normal(num_rows, num_cols, scale=1):
    '''Initialize a matrix shared variable with normally distributed
    elements.'''
    return theano.shared(numpy.random.normal(
        scale=scale, size=(num_rows, num_cols)).astype(theano.config.floatX))

def shared_zeros(*shape):
    '''Initialize a vector shared variable with zero elements.'''
    return theano.shared(numpy.zeros(shape, dtype=theano.config.floatX))



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


def sigmoidd(x):
    return 1. / (1 + np.exp(-x))


def softmaxx(vec):
    expd = np.exp(vec)
    summ = np.sum(expd)
    return expd/summ


def ssoftmaxx(vec):
    vec = vec**2
    summ = np.sum(vec)
    return np.log(vec/summ)

def nans(arr):
    return np.sum(np.isnan(arr))

#def init_with_pretrained(new_layer, old_layer):

# FIXME just returns utils
def filename():
    import os.path
    return os.path.basename(__file__)[:-3] # script's name (minus '.py')

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



# WIP I need to figure out the scope better
# the idea is to use a global variable to turn all print statements on or off.
printing_on = 1
def mprint(str):
    if printing_on:
        print(str)
    else:
        pass

def sprint(str):
    print '\n \n'
    print str
    print '\n \n'


# made for visualization with matplotlib, esp FFTs.
def logsquash(arr):
    return np.log(arr - np.min(arr) + 1)


import tables
def load_h5(filename):
    h5file = tables.openFile(filename, 'r')
    new_params = {}
    for p in h5file.listNodes(h5file.root):
        new_params[p.name] = p.read()
    h5file.close()
    return new_params


import matplotlib.pyplot as plt

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







"""
# check if filename exists, if it does, load and return
# otherwise, make object from object_maker, and save as filename, and return


def saveload(filename, object)_maker:
    import os
    if os.path.isfile(filename)
    return

if os.path.isfile(filename):
    return np.load(filename)
else:
    np.save(filename, object)
"""









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


