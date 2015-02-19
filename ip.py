


def main():

    import sys

    fl = sys._getframe(1).f_locals

    fl['sys'] = sys

    fl['theano'] = __import__('theano')
    import theano.tensor as T
    fl['T'] = T
    from theano import function as F
    fl['F'] = F

    fl['pylearn2'] = __import__('pylearn2')
    from pylearn2.utils import serial
    fl['serial'] = serial

    fl['A'] = fl['numpy'].array

    import scipy
    fl['scipy'] = scipy
    from scipy.io import wavfile as wav
    fl['wav'] = wav

    fl['stft'] = __import__('stft')
    segmentaxis = __import__('segmentaxis')
    fl['segment_axis'] = segmentaxis.segment_axis

    fl['os'] = __import__('os')
    fl['time'] = __import__('time')

    utils = __import__('utils')
    dir_utils = dir(utils)
    for ut in dir_utils:
        if not ut.startswith('__'):
            fl[ut] = eval('utils.'+ut)


if __name__ == "__main__":
    main()
