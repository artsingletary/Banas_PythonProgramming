import random
import sys
import os

super_villains = {'Fiddler' : 'Isaac Bowin',
                 'Captain Cold' : 'Leonard Snart',
                 'Weather Wizard' : 'Mark Mardon',
                 'Mirror Master' : 'Sam Scudder',
                 'Pied Piper' : 'Thomas Peterson'
                 }

# Get the value for the key
print(super_villains['Captain Cold'])

# Delete a dictionary entry
del super_villains['Fiddler']

# Change a dictionary value
super_villains['Pied Piper'] = 'Hartley Rathaway'

# Get the number of key, value pairs we have
print (len(super_villains))

print(super_villains.get("Fiddler"))

# Get a list of dictionary keys 
print(super_villains.keys())

# Get a list of dictionary values
print(super_villains.values())


