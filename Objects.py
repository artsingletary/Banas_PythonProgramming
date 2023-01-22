import random
import sys
import os

class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0
    
    #Constructor used to setup or initialize an object
    def __init__(self, name, height, weight, sound ):
         self.__name = name
         self.__height = height
         self.__weight = weight
         self.__sound = sound
    
    # Define setters and getters
    def set_name(self, name):
        self.__name = name
        
    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight
        
    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)
        
    def get_weight(self):
        return str(self.__weight)

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name, 
                                                                     self.__height,
                                                                     self.__weight, 
                                                                     self.__sound)

#Create the object cat
cat = Animal('Whiskers', 33, 10, 'Meow' )
print(cat.toString())


class Dog(Animal):
    __owner = ""
    # Give dog its own constructor
    def __init__(self, name, height, weight, sound, owner):  
       self.__owner = owner 
       # Have Dog inherit attributes from the super class Animal
       super(Dog, self).__init__(name, height, weight, sound)

       def set_owner(self, owner):
           self.__owner = owner
           
       def get_owner(self):
           return self.owner 
  
       def get_type(self):
           print ("Dog") 
           
       def toString(self):
           return "{} is {} cm tall and {} kilograms and say {} his owner is {}".format(self.__name, 
                                                                                        self.__height,
                                                                                        self.__weight, 
                                                                                        self.__sound,
                                                                                        self.__owner)
       def multiple_sounds(self, how_many=None):
           if how_many is None:
               print(self.get_sound()) 
           else: 
               print(self.get_sound() * how_many) 

#Create a dog object
Millie = Dog("Millie", 53, 27, "WooWooWoo", "Art")
print(Millie.toString())