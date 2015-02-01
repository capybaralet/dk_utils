import os
import time
import numpy
np = numpy

"""

TODO: add hostname, date (so it can be used without overwritting)


"""




"""
TODO (above)
"""



os.system('nvidia-smi > /u/kruegerd/dk_utils/nvi.txt')
fil = open('/u/kruegerd/dk_utils/nvi.txt', 'r')
lines = fil.readlines()



#monitor_file = open("monitoring.txt", "w")



gpu_lines = [8]
i = 8

while True:
    i += 4
    line = lines[i]
    if line[2] != 'N':
        break
    else:
        gpu_lines.append(i)


print 'monitoring ', len(gpu_lines), ' GPUs....'

gpu_monitors = [[]]*len(gpu_lines)

for i in range(60*60*24*7): # by default, run for ~1 week unless interrupted
    for j in range(10):
        for i,nline in enumerate(gpu_lines):
            line = lines[nline]
            gpu_monitors[i] += [int(line[33:40])] # current memory usage of this GPU
        time.sleep(.1)
        os.system('nvidia-smi > /u/kruegerd/dk_utils/nvi.txt')
        fil = open('/u/kruegerd/dk_utils/nvi.txt', 'r')
        lines = fil.readlines()
    # for now, we just use a npy array to store results...
    # that's not gonna really work, though (as it gets bigger, the write time gets huge...)
    #monitor_file.write()
    np.save('/u/kruegerd/dk_utils/nvi_monitoring.npy', np.array(gpu_monitors))
    #monitor_file.close()

