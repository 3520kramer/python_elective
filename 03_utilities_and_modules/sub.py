import subprocess, os

# Controls commandline
subprocess.run('ls')

# a command with whitespace needs to be in a list to be executed
subprocess.run(['cd', '..'])

# creates a directory and change to it
#subprocess.run(['mkdir', 'clone_folder'])
#subprocess.run(['cd', 'clone_folder'])

# might be smarter to use os-module to create and change to a directory
os.mkdir('clone_folder')
os.chdir('clone_folder')

# clone a repo from git
subprocess.run(['git', 'clone', 'example_url'])

