import random
import sys
import os

# Print numbers 0 through 9 on one line
for x in range(0, 10):
  print(x,' ',end="")
  
# Print a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']
       
for y in grocery_list:
  print(y)        

# Define a list to cycle through 
for x in [2,4,6,8,10]:
  print(x)

# List inside a list
num_list = [[1,2,3], [10,20,30], [100,200,330]]

for x in range(0,3):
    for y in range(0,3):
        print (num_list[x][y])

# While loops are used when you have no idea how many times you are going to need to loop.  Here we generate
# a random number from 0-99. Need to import the random module to get this code to work
random_num = random.randrange(0,100)
while (random_num != 15):
    print(random_num, ' ', end="")
    random_num = random.randrange(0,100)
    
# Create a more traditional while loop using an interator
i = 0;
  
while (i <= 20):
     if (i%2 == 0):
         print(i)
     elif (i == 9):
         break
     else:
         i += 1
         continue
     i += 1