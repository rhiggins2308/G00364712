# Robert Higgins G00364712
# 12th Feb 2018
# Euler Project Problem 5: Smallest multiple of numbers from 1 - 20

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

prod = 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for n in range(len(nums)):
    prod = lcm(prod, nums[n])

print("LCM is: ", prod)