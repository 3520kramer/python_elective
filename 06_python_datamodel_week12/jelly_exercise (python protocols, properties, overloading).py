""" 
Imagine a game where different sizes of jelly beans  are floating around. 
When they bump into each other they melt together and one of them gain mass the other looses mass.

The old one does not dissapear but its mass becomes 0 (maybe a little gas like state or a ghost).

If your main Jelly Bean hits a ghost jelly bean, the ghost jelly bean should regain its original state, and the mass of that should be deducted from your main Jelly Bean (it will shrink in size).

Some Ghost Jellies are born ghosts. If you hit one of these, half of your mass will be stolen by that ghost.

The game is won when your jelly bean is the only one with a mass. 
The Game is lost if you do not have any more mass.

YOUR JOB IS NOT TO CREATE THIS GAME, but to create a class that can be used in this game by someone else.
Your job is also to write pythonic code, using python protocols, properties, overloading etc.

SO:

--Create a Jelly class.
--When initialized you will create a jelly bean with a mass.         
--You should be able to add 2 or more jelly beans together thus the mass of the one of them will increase. 
--The mass of the other one will be 0, and should not remember its former state. 

--The class should also be able to deduct 2 jelly beans. If a gas like jelly bean hit your jelly bean it should regain its former mass and yours should decrease.

--The object should be able to when asked tell its state.

X-tra assignemnets:
The "gas like Jelly Beans" will over time gain a little mass. 
Small jelly fragments are lying around and can be added with the plus operator to. 
The fragments are not objects of the Jelly Bean Class but of another more simple class called Jelly_fragment.
This class has a fixed mass of 1, and it should not be changed. 
If the Jelly Bean "Ghost" at some poit regain they old mass they are only allowed to keep "over time gained mass" corosponding to 2% of the original mass. If it succeceds it is discarded. 

Add the functionallity of being able to write this code in the client. 
    val = j2 in me
    Where me and j2 are jelly objects

You can already write j == j2 -> and get a return value of True or False. 
Create an implementation that when writing j == j2 checks if the mass of the 2 objects are alike.     
"""

# Create a Jelly class.
class Jelly:

    # When initialized you will create a jelly bean with a mass
    def __init__(self, *args):

        if len(args) == 0:
            self.__mass = 3
            self.__former_state = 3
        elif len(args) == 1:
            self.__mass = args[0]
            self.__former_state = args[0]

    # for debugging
    def __repr__(self):
        return str(self.__dict__)
    
    # The object should be able to when asked tell its state
    def __str__(self):
        return f'Mass: {self.__mass}'

    # Create an implementation that when writing j == j2 checks if the mass of the 2 objects are alike. 
    def __eq__(self, other):
        if self.mass == other.mass:
            return True
        else:
            return False

    # You should be able to add 2 or more jelly beans together thus the mass of the one of them will increase. 
    def __add__(self, other):
        self.__mass += other.mass

        # Small jelly fragments are lying around and can be added with the plus operator to. 
        if isinstance(other, Jelly_fragment):
            print("You've hit a jelly fragment")
        # if the mass of the other is 0 or less then that jelly is a ghost, and then the ghost will regain it's former state
        # if a jelly hits a ghost/gas jelly, then the jelly will lose mass, and the ghost/gas jelly will regain it's former state
        elif other.mass <= 0:
            other.mass = other.former_state
            self.mass -= other.mass

        # Or else, if the jelly hits another jelly, the mass of the other will be 0
        # The colliding jelly which will become a ghost should not remember its former state.
        else:
            other.mass = 0
            other.former_state = 0
        
        # For debugging
        #return f'{self} -- {other}'

    # The class should also be able to deduct 2 jelly beans. 
    # If a gas like jelly bean hit your jelly bean it should regain its former mass and yours should decrease.
    def __sub__(self, other):
        self.mass - other.mass

        if other.mass <= 0:
            other.mass = other.former_state

        return self.mass

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        self.__mass = mass
        
    @property
    def former_state(self):
        return self.__former_state

    @former_state.setter
    def former_state(self, former_state):
        self.__former_state = former_state


class Jelly_fragment:

    def __init__(self):
        self.__mass = 1
    
    @property
    def mass(self):
        return self.__mass
"""
    @mass.setter
    def mass(self, mass):
        self.__mass = mass
"""

jelly = Jelly()
ghostJelly = Jelly(2)

fragJelly = Jelly_fragment()

jelly1 = jelly
jelly2 = jelly

#print("something:", jelly1 == jelly2)
#print("eq", jelly == ghostJelly)

#print(isinstance(jelly, Jelly))