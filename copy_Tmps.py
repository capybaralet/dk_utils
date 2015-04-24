"""
Running this file will:
1. read ~/exp_log.txt
2. copy new experiment results from local machines' /Tmp dir to /data/lisatmp
    for now, we assume that the results consist of a learning curve and best model
3. update the log to reflect that this has happened.

Meanwhile, we will:
1. Save all results locally in /Tmp (to avoid overloaded lisatmp)
2. Record all experiments in the log, with timestamps.
3. Make corresponding subdirs in lisatmp.

utils contains a function log_me(filename) that takes care of step 2 above. 
step 3 will be in the exp script.

The semantics of the log will be:
1. two lines per experiment:
    hostname
    experiment name
2. blank line seperating old (at top) from new (at bottom).

>> How to deal with multiple files editing the log?
    not gonna worry about it for now... can do something like add a message at the top of the log when editting...


CRAP!
I just realized that we're going to have to relog the experiment everytime we save, 
AND avoid appending the name if it's already there...
AND avoiding fallacious records from aborted experiments...

"""

import os

# NOT REALLY IN WORKING CONDITION
#
# what about something that just does it on this machine??
#
# BUT, I should still use the log_me() function with my experiments (AND ADD TIMESTAMPS TO IT!)
#
if __name__ == "__main__":
    fil = open('/u/kruegerd/exp_log.txt', 'r')
    lines = fil.readlines()
    reached_new_experiments = False
    for line in lines:
        if reached_new_experiments:
            if line.startswith('filepath='):
                filepath = line[9:]
                # copy this experiment's data to lisatmp
                os.system('scp kruegerd@' + hostname + ':/Tmp/kruegerd/' +\
                  filepath + '_learning_curve.npy' +  '/data/lisatmp/kruegerd/' + filepath + '_learning_curve.npy')
                os.system('scp kruegerd@' + hostname + ':/Tmp/kruegerd/' +\
                  filepath + '_best.npy' +  '/data/lisatmp/kruegerd/' + filepath + '_best.npy')
                # TODO: move this experiment's record in the log to the old section.
            else:
                hostname = line[:-1]
        if line == '\n':
            reached_new_experiments = True



