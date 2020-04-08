s = 'Hello stirng from mod.py'
l = [1, 2, 3, 4]
t = (2, 3)
se = {1, 2, 3}
d = {'Name' : 'Claus'}

def func():
    return 'Hello from mod.py function'

class Car:
    pass

def main():
    print(func())

# Makes sure it only prints when executed in terminal, not when it's imported
if __name__ == '__main__':
    main()