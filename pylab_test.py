"""
This is an example of Roland's style of dynamic plotting with pylab.
This must be run from an interactive ipython session with the --pylab command.
"""

import pylab
import numpy as np
import matplotlib.mlab as mlab

pylab.figure()

for epoch in xrange(10):
    #pylab.clf()
    mean = 0
    variance = (epoch+1)**.5
    sigma = np.sqrt(variance)
    x = np.linspace(-3,3,100)
    pylab.plot(x,mlab.normpdf(x,mean,sigma))
    pylab.show(); pylab.draw()
    
pylab.savefig('ex1.png', bbox_inches='tight')


pylab.figure()

for i in range(20):
    pylab.subplot(10, 2, i+1)
    mean = 0
    variance = (epoch+1)**.5
    sigma = np.sqrt(variance)
    x = np.linspace(-3,3,100)
    pylab.plot(x,mlab.normpdf(x,mean,sigma))
    pylab.show()

pylab.savefig('ex2.png', bbox_inches='tight')


