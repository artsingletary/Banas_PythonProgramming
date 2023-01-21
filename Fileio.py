import random
import sys
import os

# Create and open a file for writing.  Use "ab+" to read and append to a file.
test_file = open("test.txt", "wb")
# Show the mode that was used
print(test_file.mode)
# Print the name of the file
print(test_file.name)
# Write to the file
test_file.write(bytes("this is a test\n", 'UTF-8'))
# Close the file
test_file.close()

"""

# Open a file for reading and writing 
test_file = open("test.txt", "r+") 
text_in_file = test_file.read()
print (text_in_file)
test_file.close()

# Remove a file
os.remove("test.txt")
"""