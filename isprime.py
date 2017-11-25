def is_prime(a):
    x = True
    for i in range(2, a): #Tests if number to be checked is divisible by any numbers in the range 2 to itself.
       if a%i == 0:
           x = False
           break

    if x == True:
        print "Prime"
    else:
        print "Not prime"

num = int(raw_input("Enter number: "))
is_prime(num)
