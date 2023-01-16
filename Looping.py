


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

for x in range(0,3)
  


"""
##############################################
# Print out numbers 2,4,6,8,10
##############################################
for i in [2,4,6,8,10]:
     print("i = ", i) 

##############################################
# Print out numbers from 0 to 10
##############################################
for i in range(10):
     print("i = ",i)

##############################################
# Print out numbers from 2 to 10
##############################################
for i in range(2,10):
     print("i = ",i)

##############################################
# Print out odd number from 1-20
##############################################
for i in range (1,21):
  if ((i % 2) != 0):
      print (i)

##############################################
# Print floating number with 2 decimals
##############################################
your_float = input("Enter a float: ")
your_float = float(your_float)
print ("Round to 2 decimals : {:.2f}".format(your_float))


##############################################
# Have the user enter their investment amount and expected interest rate
# Print out the earnings after each year for a 10 year period.
##############################################

total = input ('What is your investment amount ')
rate = input ('What is your interest rate ')

total = float(total)
rate = float(rate) * .01

for i in range (1,11):
  total = (total + (total * rate)) 
  print ("Total Year ", i, "- {:.2f}".format(total))

# Floats are only precise up to the first 16 digits
i = .11111111111111111111111111111111
j = .00000000000000010000000000000001

print ("Answer : {:.32}".format(i + j))

print("3 + 4 * 5 = {}".format (3 + 4 * 5))
print("(3 + 4) * 5 = {}".format ((3 + 4) * 5))


##############################################
# Generate a random integer between 1 and 50
##############################################
import random
rand_num = random.randrange(1,51)

i = 1

while (i != rand_num):
   i += 1
print ("The random value is : ", rand_num, i)

####################################################################################
# Loop 20 interations.  Just print out the odds.  Break out of the look when i is 15
####################################################################################

i = 1
while i <= 20:
     if (i % 2) == 0:
       i += 1
       continue

     if i == 15:
       break

     print ("Odd : ", i)
     i += 1
"""