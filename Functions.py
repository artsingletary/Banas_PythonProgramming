import random
import sys
import os

def addNumber(fNum, lNum):
     sumNum = fNum + lNum
     # What goes on inside a function stays there unless it is returned
     return sumNum
 
print(addNumber(1,4))

print('What is your name')
name = sys.stdin.readline()
print('Hello', name)