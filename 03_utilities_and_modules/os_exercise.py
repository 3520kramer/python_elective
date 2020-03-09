import os

# find the current directory and print it
path = os.getcwd()
print('current directory:', os.getcwd())


# make a directory in current folder if it doesn't exist
name = 'os_exercise'
if os.path.isdir(name):
    pass
else:
    os.mkdir(name)

# change directory to the new folder and print it
os.chdir(path + '/' + name)
print('current directory:', os.getcwd())

# create 3 files with an input from the console 
for i in range(1,4):
    text = input('Please write some code ')
    file = open(f'exercise_{i}.py', 'w') # f means print format, so that i can put the value of the variable 'i' in the string
    file.write(text)
    file.close() # closes the file in the memory

for i in range(1,4):
    file = open(f'exercise_{i}.py')
    unique_words = len(set(file.read().split()))
    print(unique_words)
    #s = set(t)
    #unique_words = len(s)