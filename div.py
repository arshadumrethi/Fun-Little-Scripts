def div(a, b, c):
    if a % 3 == 0 and a % 5 == 0:
        print "num1 is divisible by 3 & 5"
    else:
        print "num1 is not divisible"

    if b % 3 == 0 and b % 5 == 0:
        print "num2 is divisible by 3 & 5"
    else:
        print "num2 is not divisible"

    if c % 3 == 0 and c % 5 == 0:
        print "num3 is divisible by 3 & 5"
    else:
        print "num3 is not divisible"

num1 = int(raw_input("Enter the first number: "))
num2 = int(raw_input("Enter the second number: "))
num3 = int(raw_input("Enter the third number: "))

div(num1, num2, num3)
