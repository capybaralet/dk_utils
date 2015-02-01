# a better way than with os:
from subprocess import PIPE, Popen
proc = Popen(['git', 'log'], stdout=PIPE)
lines = proc.stdout.readlines()


import os
os.system("git log > gitlog.txt")
text_file = open("gitlog.txt", "r")
lines = text_file.readlines()
# create list of commits
commits = []
for line in lines:
    if line.startswith('commit'):
        commits.append(line[7:-1])



# find last commit with my_filename in it:
def find_last_commit_with_filename(my_filename):
    for n, commit in enumerate(commits):
        os.system("git ls-tree -r " + commit + " --name-only > list_of_files.txt")
        text_file = open("list_of_files.txt", "r")
        filenames = text_file.readlines()
        for filename in filenames:
            if filename == my_filename + '\n':
                print n, commit
                return


