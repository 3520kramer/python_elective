import sys
def msg():
    # sys.argv takes commands from terminal and prints it as a list
    # index 0 is the name of the file
    # index 1 - n is the input from the terminal
    if sys.argv[1] == 'Oliver':
        print(sys.argv[1], 'You are in')
        print(sys.argv[2], 'WAUW')

    elif sys.argv[1] == 'NotOliver':
        print(sys.argv[1], 'You are not in')
    else:
        a = 'Nope'
        b = 'bro'
        print(f'{a} nono {b}')


msg()