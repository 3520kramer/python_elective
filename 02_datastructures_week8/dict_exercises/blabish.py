
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Blabish exercise.

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # opens the file
  file = open(filename)

  # reads the file and splits it by whitespace to a list
  text = file.read().lower().split()

  # creates an empty dictionary to map the words
  dictionary = {}

  # creates a counter to keep track of where to slice the list
  counter = 0

  # sets the first key to an empty string, with the value as a list of the 10 first words in the file
  dictionary[''] = text[counter:counter+10]
  
  # to be able to add a new word to the dictionary through the text, we must add one to the counter in each iteration 
  for word in text:
    counter+=1
    dictionary[word] = text[counter:counter+10]

  return dictionary


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # sets the word to searc for to the argument passed in the parameter
  search_word = word
  
  # iterates 200 times to create 200 words
  for i in range(200):
    # Chooses a random word from the list associated with the search word and saves the new word
    search_word = random.choice(mimic_dict[search_word])

    # prints the random word, and uses a whitespace at the end of the print statement instead of a newline
    print(search_word, end=" ")

    # if the length of the list associated with the new search word is empty then we set the search word to be the argument passed
    if len(mimic_dict[search_word]) is 0:
      search_word = word


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print ('usage: python mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


main()
