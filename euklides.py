#Największy wspólny dzielnik - modulo
def NWD(a,b):
    while b > 0:
        temp = b
        b = a % b
        a = temp

    return a

print(NWD(3,9))

#Największa wspólna wielokrotność
def NWW(a,b):
    return (a*b) // NWD(a,b)

print(NWD(27,9))