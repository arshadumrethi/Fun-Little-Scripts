num = int(raw_input("Enter number: "))

#Easiest Way
import math
math.factorial(num)

#Alternate Way if you have to write the function yourself.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial(num)
