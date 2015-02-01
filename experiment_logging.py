"""
This is a general purpose add-on for logging experiments

Place it at the beggining of any script that runs experiments to automatically 
log ALL experiments with that script.

Saves models locally (in /Tmp) and everything else in /data/lisa/exp.

"""



import os
import shutil
import socket
import time

username = 'kruegerd'

# make directories for saving model and analysis plots
# we save everything in the exp folder, except the pkls of the model (which are saved locally)
filename = os.path.basename(__file__)[:-3] # this script's name (minus '.py')
# where the pkls are saved
exp_dir = '/Tmp/' + username + '/exp/' + filename + '/'
if not os.path.exists(exp_dir): os.makedirs(exp_dir)
# where the plots are saved
plots_dir = '/data/lisa/exp/' + username + '/' + filename + '/'
if not os.path.exists(plots_dir): os.makedirs(plots_dir)
# where the script is saved
exp_scripts_dir = plots_dir + 'exp_scripts/'
if not os.path.exists(exp_scripts_dir): os.makedirs(exp_scripts_dir)

# record experiments by start-time and hostname in txt file:
exp_record_path = plots_dir + '/exps.txt'
if not os.path.exists(exp_record_path): open(exp_record_path, 'a').close()
fil = open(exp_record_path,'a+')
exp_num = len(fil.readlines()) + 1
date = time.strftime("%d/%m/%Y")
hostname = socket.gethostname()
exp_info = date + '__' + time.strftime("%H:%M:%S") + '   hostname= '+hostname+'\n'
fil.write(exp_info)
fil.close()
# copy this version of the script into exp_scripts_dir
shutil.copyfile(os.path.realpath(__file__), exp_scripts_dir + filename + '__#' + str(exp_num) + '.py')

# add exp_num to create paths for this run of the script
model_path = exp_dir + 'model#' + str(exp_num)
plots_path = plots_dir + 'model#' + str(exp_num)
