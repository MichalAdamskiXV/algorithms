# ----ALGORYTMY ITERACYJNE ---- #

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

print(NWW(27,9))


# ----ALGORYTMY REKURENCYJNE ---- #
def NWD_2(a, b):
    if b == 0:
        return a
    else:
        return NWD_2(b, a % b)

print(NWD_2(3, 27))

def NWW_2(a,b):
    return (a * b) // NWD_2(a, b)

print(NWW_2(27,9))
