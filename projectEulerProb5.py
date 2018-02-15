# Robert Higgins G00364712
# 12th Feb 2018
# Euler Project Problem 5: Smallest multiple of numbers from 1 - 20

prod = 1
num = 1

while num <= 20:
    if prod % num != 0:
        prod = num*prod
    num +=1

print("LCM of all numbers from 1 - 20, inclusive, is:", prod)
    