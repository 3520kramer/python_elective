"""
The underscore methods (__add__ etc.) you can see in the documentation using help(list) 
should be implemented in your LinkedList (or at least as many as possible)
"""

# help(list)

class Node:
    def __init__(self, data):
        self.data = data # the data of the node
        self.next = None # a pointer to the next node in the linkedlist

    def __repr__(self):
        #return str(self.__dict__)
        return f'{self.data}'

    """def __str__(self):
        return f'{self.data}'"""

class LinkedList:
    def __init__(self):
        self.head = None # head points to the first node of the linkedlist
    

    def __repr__(self):
        return f'Data: {", Data: ".join(map(str,self))}' # f-format to make a repr of the object


    def __str__(self):
        return f'{", ".join(map(str,self))}' # uses f-format to make a str representtion of the object


    # function that makes the object iterable 
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current # same as return but the rest of the function is stille executed
            current = current.next


    # returns the length of the linkedlist
    def __len__(self):
        length = 0
        for node in self: # We are able to iterate over the linked list by having implemented the __iter__ function
            length += 1
        return length

    # Makes it possible to add to linkedlists together by using '+'-operator
    # returns a sublist with the concatenated linked list
    def __add__(self, other):

        concatenated_linked_list = LinkedList()
        for node in self:
            concatenated_linked_list.append(node)
        
        for node in other:
            concatenated_linked_list.append(node)

        return concatenated_linked_list

        # This simply appends the notes from the other linkedlist to the original list and returns it
        """
        for node in other:
            self.append(node)

                return self
        """

    def __mul__(self, times_multiplied):
        multiplied_linked_list = LinkedList()

        for i in range(times_multiplied):
            multiplied_linked_list += self
        
        return multiplied_linked_list

    # Makes it possible to use slice. It's used later in __getitem__()
    def __sliceitem__(self, the_slice):
        
        sliced_list = LinkedList()

        if the_slice.step == None:
            step = 1
        else: 
            step = the_slice.step

        if the_slice.start == None:
            if step > 0:
                start = 0
            else:
                start = len(self)-1
        else:
            start = the_slice.start

        if the_slice.stop == None:
            if step > 0:
                stop = self.length
            else:
                stop = -1
        else:
            stop = the_slice.stop

        # By using range with it's built in ability to take start, stop and step as arguments
        # We use it's able to take these arguments, to insert our own 
        # We can then slice the list by appending the nodes to a new list
        for item in range(start,stop,step):
            sliced_list.append(self[item])
        
        print(sliced_list)

        return sliced_list

    # Makes it possible to retrieve an item at a specific index by using list[0] syntax
    # Makes it possible to slice the list by using syntax [start:stop:step]
    def __getitem__(self, index):
        # If you enter a slice instead of a index, we return the returnvalue of the sliceitem method
        if type(index) == slice:
            return self.__sliceitem__(index)
        # If you enter a index and it's below zero.
        # The iteration over the list will start backwards,
        # therefore the iteration_index is set to the negative value of the lists length
        else:
            if index < 0:
                iter_index = -(len(self))
            # if the index is above 0 and below the lists length, the iterations starts from the first position.
            # Therefore the iteration starts from 0 by setting the iter_index to 0
            else:
                iter_index = 0
                for item in self:
                    if iter_index == index:
                        return item
                    iter_index += 1
            
                # If the index is above the lenght of the list, negative values included,
                # we raise an indexError
                raise IndexError('index out of range')
        


    # Makes it possible to update a node at a specific index
    def __setitem__(self, index, element):
        if index > len(self)-1: # if the index is higher than the lists length-1 (zero-based), then we raise an error
            raise AttributeError('No such index in list, use .append() to append the element to list instead')
        else:
            temp = self.head
            for iter_index in range(index+1):
                if iter_index == index:
                    temp.data = element
                else:
                    temp = temp.next


    # Makes it possible to delete items from list by using del()
    def __delitem__(self, index):
        if index > len(self):
            raise IndexError('index out of range')
        elif index > 0:
            iter_index = 0
            self[index-1].next = self[index+1]
        elif index == 0:
            self.head = self[1]

    # Appends the element to the end of the list
    def append(self, element):
        #node = Node(element)
        #print("NODE:", node)
        #print("ELEMENT:", element)
        if self.head == None:
            self.head = Node(element)
        else:
            self[len(self)-1].next = Node(element)

            



llist = LinkedList()
llist2 = LinkedList()

data1 = 'data1'
data2 = 'data2'
data3 = 'data3'
data4 = 'data4'
data5 = 'data5'

llist.append(data1)
llist.append(data2)
llist.append(data3)

llist2.append(data4)
llist2.append(data5)

