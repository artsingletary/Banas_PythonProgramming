import random
import sys
import os

long_string = "I'll catch you if you fall - The Floor"

# Print first four characters of the string 
print(long_string[0:4])

# Print last five characters of the string
print(long_string[-5:])

# Print everything up to the last five characters
print(long_string[:-5])

# Print first four characters of one string and concat with another string
print(long_string[:4] + " be there")

"""
rand_string = "    this is an important string    "

# Strip the black characters to the left
rand_string = rand_string.lstrip()

# Strip the black characters to the right
rand_string = rand_string.rstrip()

# Capitalize the first letter
print(rand_string.capitalize())

# Print in all caps
print(rand_string.upper())

# Print in all lower case
print(rand_string.lower())

# Convert a list into a string
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

# Convert a string into a list
a_list_2 = rand_string.split()
for i in a_list_2:
  print (i)

# Count number of occurrences of the word "is"
print("How many is : ", rand_string.count("is"))

# Replace a string within a string
print(rand_string.replace("an ", "a kind of "))

# Create an acronym
orig_string = input("Enter string to convert to acronym: ")
orig_string = orig_string.upper()
list_of_words = orig_string.split()
for word in list_of_words:
    print(word[0], end="")
print ()
"""

