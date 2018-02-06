# Ian McLoughlin
# A program that displays Fibonacci numbers.
# Topic 1 Exercise

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 18+20
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# Fibonacci number 38 is 39088169

#-----------------------------------------------------------
#-----------------------------------------------------------

# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
# Topic 2 Exercise

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Higgins"
first = name[0]
print(first)

# H

last = name[-1]
print(last)
# s

firstno = ord(first)
print(firstno)
# 72

lastno = ord(last)
print(lastno)
# 115

x = firstno + lastno

ans = fib(x)
print("My surname is", name)
# My surname is Higgins

print("The first letter", first, "is number", firstno)
# The first letter H is number 72

print("The last letter", last, "is number", lastno)
# The last letter s is number 115

print("Fibonacci number", x, "is", ans)
# Fibonacci number 187 is 538522340430300790495419781092981030533


# H
# s
# 72
# 115
# My surname is Higgins
# The first letter H is number 72
# The last letter s is number 115
# Fibonacci number 187 is 538522340430300790495419781092981030533
