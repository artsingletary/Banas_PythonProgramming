import random
import sys
import os

long_string = "     i'll catch you if you fall - The Floor"

# Print first four characters of the string 
print(long_string[0:4])

# Print last five characters of the string
print(long_string[-5:])

# Print everything up to the last five characters
print(long_string[:-5])

# Print first four characters of one string and concat with another string
print(long_string[:4] + " be there")

print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14) ) 

# Capitalize the first letter of a string
print(long_string.capitalize())

# Return the index value.  The find string is case sensitive so it has to be exact.
print(long_string.find("Floor"))

# Check to see if a string is all characters 
print('test'.isalpha())

# Check to see if a string is all numbers
print("12345".isalnum())

# Get the length of a string
print(len(long_string))

# Replace a word with another word
print(long_string.replace("Floor","Door"))

# Strip out any white space at the front or back of the string
print(long_string.strip())

# Split a string into a list
quote_list = long_string.split(" ")
print(quote_list)
