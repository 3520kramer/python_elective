"""
3. Machine -> printer
Create a Machine class that takes care of powering on and off a the machine.   
Create a printer class that is a subclass of the Machine super class.   
The printer should be able to print to console.  
The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and and load new paper in the tray if empty.  
"""

class Machine:

    def __init__(self):
        self.__power = True

    def __str__(self):
        return f'{self.__power}'

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, powering):
        if powering:
            self.__power = True
        else:
            self.__power = False


class Printer(Machine):
    def __init__(self):
        super().__init__()
        self.__papertray = Papertray()
    
    @property
    def papertray(self):
        return self.__papertray

    def print_pressed(self):
        if self.__papertray.papers_in_tray < 1:
            print('You need to load some paper, i\'m empty')
        else: 
            print('Printing Something')
            self.__papertray.use_paper()


class Papertray:
    def __init__(self):
        self.__papers_in_tray = 10

    @property
    def papers_in_tray(self):
        return self.__papers_in_tray

    @papers_in_tray.setter
    def papers_in_tray(self):
        pass

    
    def load_paper(self):
        self.__papers_in_tray += 10
    
    def use_paper(self):
        self.__papers_in_tray -= 1

    


m = Machine()
p = Printer()
