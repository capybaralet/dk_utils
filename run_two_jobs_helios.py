
#
# each job waits a random amount of time
# then looks to see if job1 has started (logged in a txt file in $RAM_DISK_USER)
# if yes, then starts job2.
# 
# 
#
#
# MORE ON USING CLUSTERS:
# scp to head node (or $SCRATCH) to copy things to cluster
# $RAM_DISK(_USER) is best place for temporary things...
#
# jobs are automatically logged in $SCRATCH/LOGS/command/ (err \ out)
# 
# may need to update bashrc config for clusters...
#
# TO SEE JOBS:
# showq (Helios)
# qstat (-u capybara) (Briaree/Hades)
#
# mjobctl -c -w username : delete all jobs
#
# tail -f out (for live monitoring)
#
# jobdispatch --gpu --duree=10m --mem=2G --env=THEANO_FLAGS=floatX=float32,device=gpu,force_device=True --repeat_jobs=2 python ~/repos/theano/misc/check_blas.py
#
#
# cluster_comparison: https://docs.google.com/spreadsheet/ccc?key=0Aos5g8e-dv5pdExVeEp1RnRTckRIem9ac1VyaGk4WEE&authkey=CNr65MAL&hl=en&authkey=CNr65MAL#gid=0
#
#
#
#
# Use Dustin's system with seperate branches in seperate directories, and setting paths to them for different projects (or I guess I could just work locally...)
#
# Clean up and organize everything
#
# 
#
#

