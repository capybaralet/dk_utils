from numpy import *
import numpy as N
import pylab as P


def estimated_autocorrelation(x):
    n = len(x)
    variance = x.var()
    x = x-x.mean()
    r = N.correlate(x, x, mode = 'full')[-n:]
    #assert N.allclose(r, N.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
    result = r/(variance*(N.arange(n, 0, -1)))
    return result

#P.plot(time,estimated_autocorrelation(x))
#P.xlabel('time (s)')
#P.ylabel('autocorrelation')
#P.show()


noise = np.random.randn(1000)
b = np.hstack((A([1]), np.random.uniform(-1,1,5)))
filtered_noise = lfilter(b, 1, noise)
print estimated_autocorrelation(noise)
print estimated_autocorrelation(filtered_noise)

