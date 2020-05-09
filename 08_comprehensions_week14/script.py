# list comprehension syntax
#[out for out in ... if ...]
# so the first out, is the output, and then we have the for loop to populate the list. At last we have an if-statement as our condition

# creates a list from 0 to 9
my_list = [var for var in range(10)]

# creates a list from 0 to 9 with a condition 
my_even_list = [var for var in range(10) if var % 2 == 0]

# create a list with an if else
if_else_list = [i if i%2 == 0 else 'odd number' for i in range(1,10)]

# create a list with en else if statement
else_if_list = [i if i%2 == 0 else 'odd small' if i < 5 else 'odd big' for i in range(1,10)]
# explanation: If the number is odd and smaller than 5 then return 'un-even small', else if the number is odd and bigger than 5, then we return 'un-even big'
# see basic_list_comp_exercise

# create a list from nested loop
nested_list = [(i,j) for i in range(1,3) for j in range(1,3)]

# set comprehension (same as list, but without duplicates and with curly braces)
set_comp = {i for i in range(10)}

# tuple comprehension
# the i for i in range ... is a generater expression. We need to type cast it to a tuple.
tuple_comp = tuple((i for i in range(10)))

# dictionary comprehension
random_dict = {1:'Number One', 2:'Number two'} # for demo purposes

dict_comp = {key:value for (key, value) in random_dict.items()}

dict = {number:number*2 for number in range(4)}
