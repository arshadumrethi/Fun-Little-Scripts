######################################################
#3.A
startnum = 1

sequence = str(startnum)
nextnumber = startnum

for i in range(1, 7):
    nextnumber += i
    sequence = sequence + ", " + str(nextnumber)

print sequence

########################################################
#3.B
startnum = 1

sequence = str(startnum)
nextnumber = startnum

for i in range(1, 14):
    nextnumber += i
    sequence = sequence + ", " + str(nextnumber)

print sequence

######################################################
#3.C
def fib(n):
    a, b = 0, 1
    while b < n:
        print b,
        a,b = b, a + b

fib(100)
##########################################################
