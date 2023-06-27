#simpler
'''
n1, n2 = input().split()
total = int(n1) + int(n2)
print(total)
'''

# try to re-write using sys library

import sys

# read input from the user
input = sys.stdin.readline()

# split the input data into two digits
digits = input_data.split()

# Ensure that two digits are provided
if len(digits) != 2:
  print('Please provide two digits.')
  sys.exit(1)

# Convert the digits to integers
try:
  digit1 = int(digits[0])
  digit2 = int(digits[1])
except ValueError:
  print('INvalid input.')
  sys.exit(1)

# Calculate the sum of the two digits
sum_digits = digit1 + digit2

# print the sum 
print('The sum is:', sum_digits)
