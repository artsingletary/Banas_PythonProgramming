import random
import sys
import os

print("hello world")

# Comment

'''
Multiline Comment
'''

name = "Art"
print(name)

print ("5 + 2 =", 5+2)
print ("5 - 2 =", 5-2)
print ("5 * 2 =", 5*2)
print ("5 / 2 =", 5/2)
print ("5 % 2 =", 5%2)
print ("5 ** 2 =", 5**2)
print ("5 // 2 =", 5//2)

quote = "\"Always remember you are unique\""

multi_line_quote = '''  
just 
like everyone 
else'''

new_string = quote + multi_line_quote

print(new_string)

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print("\n" * 5  )
print("end")