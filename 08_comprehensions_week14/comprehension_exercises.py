'''
Create a dictionary containing a deck of cards.
The keys should be the elements from the colors set and the values should be the elements from the numbers list
'''

# i use set comprehension to create a set of characters which contains the colors/kulører of the cards
colors = {chr(out) for out in range(9824,9828)}

# i then use list comprehension to create the numbers and adds appends the special cards
numbers = [out for out in range(2,11)] + ['A','J','K','Q']

# i then use dictionary comprehension which creates a set of the numbers as the value, and sets the colors as key
card_deck = {out:set(numbers) for out in colors}

'''
Create a listcomp that produces a list of tuples containing all card in a deck.
'''
# For each color, i need to add all the numbers
my_list = []
for color in colors:
    for number in numbers:
        my_list.append((color,number)) 

# here using comprehension
list_of_cards = [(color, number) for color in colors for number in numbers]

'''
All the below exercieses, unless something else is stated, should be solved using:

a normal for loop
a list comprehension

You should also run the ‘timer’ and ‘memory usage’ decorators on your new functions. 
(these where the exercises last week)

Try to see if you in anyway can optimize you code. 
(It is a good idea to test your solutions with large numbers and see how they react)

'''

import my_decorators as decorator

# 1. Find all of the numbers from 1-1000 that are divisible by 7
@decorator.memory_profiler
@decorator.timer
def divisible_by_7_loop():
    looped_list = []
    for i in range(1000):
        if i % 7 == 0:
            looped_list.append(i)

@decorator.memory_profiler
@decorator.timer
def divisible_by_7_comp():
    comp_list = [i for i in range(1000) if i % 7 == 0]
'''comprehension is approximately 1 second faster when doing forloops of 100.000.000'''



# 2. Find all of the numbers from 1-1000 that have a 3 in them
looped_list = []
for i in range(1000):
    if '3' in str(i):
        looped_list.append(i)

@decorator.memory_profiler
@decorator.timer
def find_3_loop():
    for i in range(10000000):
        if '3' in str(i):
            looped_list.append(i)


@decorator.memory_profiler
@decorator.timer
def find_3_comp():
    comp_list = [i for i in range(10000000) if '3' in str(i)]
'''comprehension is approximately 0.2 second faster'''



# 3. Count the number of spaces in a string
my_string = 'A B C D E F G H I J K L M N'*10000000

@decorator.memory_profiler
@decorator.timer
def space_loop():
    loop_list = []
    for space in my_string:
        if space is " ":
            loop_list.append(space)
    print(len(loop_list))
             
@decorator.memory_profiler
@decorator.timer
def space_comp():
    comp_list = [space for space in my_string if space is " "]
    print(len(comp_list))
'''comprehension is approximately 4.5 second faster'''
import string



# 4. Remove all of the vowels in a string
vowels = "aeiouy"
words = "Hey! List comprehension is really fast!"*1000000

@decorator.memory_profiler
@decorator.timer
def vowel_loop():
    loop_list = []
    words_without_wowels = ""

    for char in words:
        if char not in vowels:
            words_without_wowels += char

@decorator.memory_profiler
@decorator.timer
def vowel_comp():
    comp_list = [char for char in words if char not in vowels]
    words_without_wowels = str().join(comp_list)
'''comprehension is approximately 2 seconds faster'''


# 5. In a string made up of randomly generated words, generate a list of all words that have less than 4 letters
import random
# creating a bunch of random "words" of 100000 letters and then multiplying it with 10000.
random_words = ''.join(random.choices(string.ascii_letters + " ", k=100000))*10000

@decorator.memory_profiler
@decorator.timer
def short_words_loop():
    looped_list = []
    for word in random_words.split():
        if len(word) < 4:
            looped_list.append(word)
    


@decorator.memory_profiler
@decorator.timer
def short_words_comp():
    comp_list = [word for word in random_words.split() if len(word) < 4]
    
'''comprehension and looping is almost identical (comp 0.1 faster) when doing forloops of 1.000.000'''


# 6. Use a dictionary comprehension to count the length of each word in a sentence.
sentence = ''.join(random.choices(string.ascii_letters + " ", k=1000000))
#sentence = "Look at that dictionary comprehension"

@decorator.memory_profiler
@decorator.timer
def dict_loop():
    dict_loop = dict()

    for word in sentence.split():
        dict_loop[word] = len(word)

@decorator.memory_profiler
@decorator.timer
def dict_comp():
    dict_comp = {word:len(word) for word in sentence.split()}

'''comprehension is approximately 0.2 seconds faster'''

# 7. Use a nested list comprehension to find all of the numbers from 1-1000 that are 
# divisible by any single digit besides 1 (2-9)
@decorator.memory_profiler
@decorator.timer
def nested_list_loop():
    nested_list_loop = []

    for i in range(1,1001):
        for j in range(2,10):
            if i % j == 0:
                nested_list_loop.append(i)

@decorator.memory_profiler
@decorator.timer
def nested_list_comp():
    nested_list_comp = [i for i in range(1,1001) for j in range(2,10) if i % j == 0]

'''comprehension is approximately 0.0002 seconds faster'''


# 8. For all the numbers 1-1000, use a nested list comprehension to find 
# the highest single digit any of the numbers is divisible by
@decorator.memory_profiler
@decorator.timer
def highest_loop():
    a_loop = []
    for i in range(1,1001):
        for j in range(9,0,-1):
            if i % j == 0:
                a_loop.append(j)
                break

# finds the highest number first by going through range backwards, but it doesn't solve the problem
doesnt_work_list_comp = [j for i in range(1,1001) for j in range(9,0,-1) if i % j == 0]

# solves the problem:
@decorator.memory_profiler
@decorator.timer
def highest_comp():
    list_comp = [max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in range(1,40)]

'''comprehension is approximately ??.?? seconds faster'''


# 9. Multiples of 3 and 5: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000
@decorator.memory_profiler
@decorator.timer
def sum_loop():
    sum_of_multiples = 0
    for i in range(1,10):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i

@decorator.memory_profiler
@decorator.timer
def sum_comp():
    comp_list = sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0])

'''comprehension is approximately ??.?? seconds faster'''
