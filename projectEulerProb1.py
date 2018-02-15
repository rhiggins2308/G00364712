# Robert Higgins G00364712
# 12 Feb 2018
# Project Euler Problem 1: Multiple of 3 and 5 below 1000

counter = 0
sumTotal = 0

while counter < 1000:
    if (counter % 3 == 0) or (counter % 5 == 0):
        sumTotal += counter
        counter +=1
    else:
        counter += 1

print("Sum of all multiples of 3 or 5, less than 1,000 is: ", sumTotal)
