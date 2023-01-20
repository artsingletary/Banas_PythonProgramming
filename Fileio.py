import random
import sys
import os

test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("this is a test\n", 'UTF-8'))
test_file.close()