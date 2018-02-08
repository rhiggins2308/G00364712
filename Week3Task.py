# Robert Higgins 08/02/2018
# G00364712
# Collatz Conjecture https://en.wikipedia.org/wiki/Collatz_conjecture

nStr = input("Enter a positive integer:")
n = int(nStr)

while n > 1:
    if n % 2 == 0:
        n = n/2
        print(int(n))
    else:
        n = (3*n) + 1
        print(int(n))

# Output below for user input 23
# Enter a positive integer:23
# 70
# 35
# 106
# 53
# 160
# 80
# 40
# 20
# 10
# 5
# 16
# 8
# 4
# 2
# 1