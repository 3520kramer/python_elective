# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Words exercise

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# function that creates a dictionary with the word as key, 
# and a count of how many times the word is in the text as value
def create_dictionary(file):
  # opens the files and reads the content in lowercase and splitted on whitespace, into the variable text as a list
  file = open(file)
  text = file.read().lower().split()
  
  # creates the dictionary
  word_dict = dict()

  # for each word that is in the text, it needs to be either created, if it is not in the list,
  # but if it is, we need to add one to the counter of that word
  for word in text:
    if word in word_dict:
      word_dict[word] += 1
    else:
      word_dict[word] = 1
  
  # close the file and return the dictionary
  file.close()
  return word_dict

# a function that prints all the words with the count but not sorted
def print_words(file): 
  word_dict = create_dictionary(file)
  
  for i in sorted(word_dict):
    print(i, word_dict[i])
  
# a helper function to the sorted method. This is used as key to sort by
def sort_by_value(value):
  return value[1]

# this prints the word which are represented most times in the text first
def print_top(file):
  word_dict = create_dictionary(file)

  # For loop which sorts the items of the dict (which is the iterable). 
  # I sort it by the helper function, and we reverse it as we want the biggest value first. 
  # Then i only use the top 20 for a more clean presentation
  for i in sorted(word_dict.items(), key=sort_by_value, reverse=True)[:20]:
    print(i[0], i[1])
    
  

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: python words.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

main()
