import random
import sys
import os

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 
                'Bananas']
print('First Item', grocery_list[0])

# Change the value of the first item in the list
grocery_list[0] = "Green Juice"
print('First Item', grocery_list[0])

# Print index 1-3 but not including index 3
print(grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids', 
                'Cash']

# Store lists inside of a list
to_do_list = [other_events, grocery_list]
print(to_do_list)

# Print the second item in the second list
print((to_do_list[1][2]))