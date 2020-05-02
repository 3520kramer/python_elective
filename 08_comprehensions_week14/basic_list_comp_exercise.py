
# 1.
# Create a list of capital letters from the english alphabet.
# not really a list comprehension:
import string
list_of_letters = [letter for letter in string.ascii_uppercase]
# the proper way:
list_of_letters = [chr(i) for i in range(65,91)]

# 2.
# Do the same, but exclude the 4 with the Unicode code point of 70, 75, 80 and 85.
list_of_some_letters = [chr(i) for i in range(65,91) if i not in [70, 75, 80, 85]]

# 3.
# Create a list of capital letters, but exclude every second between F & O
list_of_a_few_letters = [chr(i) for i in range(65,91) if i not in range(70,81,2)]

# 4.
# Create something that prints
# ['un-even and small', 2, 'un-even and small', 4, 'un-even and large', 6, 'un-even and large', 8, 'un-even and large']
mixed_list = [i if i%2 == 0 else 'un-even small' if i < 5 else 'un-even big' for i in range(1,10)]

# mixed_list should be seen as an else if statement: 
# if the number is odd return 'un-even small', else if the number is odd and bigger than 5, then we return 'un-even big'

# if a is false, and b is true, then c needs to be true or else d is what gets returned
demo_else_if_list = [output if 'a' else 'b' if 'c' else 'd' for output in range(10)]

# 5.
# From 2 lists, using a list comprehension, create a list containing:
# [('Black', 's'), ('Black', 'm'), ('Black', 'l'), ('Black', 'xl'), ('White', 's'), ('White', 'm'), ('White', 'l'), ('White', 'xl')]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
nested_list = [(i,j) for i in colors for j in sizes]

# 6.
# If the tuple pair is in the list 'sold_out', it should not be added to the comprehension generated list.
sold_out = [('Black', 'm'), ('White', 's')]

new_nested_list = [(i,j) for i in colors for j in sizes if (i,j) not in sold_out]