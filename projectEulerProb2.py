# Robert Higgins G00364712
# 12th Feb 2018
# Euler Project Problem 2: Even Fibonacci Numbers

fibNo1 = 0
fibNoLast = 1
fibNoCurr = fibNo1 + fibNoLast
sumTotal = 0

while (fibNoCurr < 4000000):
    if (fibNoCurr % 2 == 0):
        sumTotal += fibNoCurr
        fibNo1 = fibNoLast
        fibNoLast = fibNoCurr
        fibNoCurr = fibNo1 + fibNoLast
    else:
        fibNo1 = fibNoLast
        fibNoLast = fibNoCurr
        fibNoCurr = fibNo1 + fibNoLast

print("Sum of even Fibonacci Numbers, less than 4,000,000 is :", sumTotal)