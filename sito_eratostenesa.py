# Algorytm to wyznaczania liczb pierwszych w danym przedziale
def sito_eratostenesa(n):
    sito = [0]*(n+1)
    sito[0] = 1
    sito[1] = 1

    i = 2
    while i*i <= n:
        if sito[i] == 0:
            for j in range(i*i, n+1, i):
                sito[j] = 1
        i += 1

    return sito

n = 10

sito = sito_eratostenesa(10)
for i in range(n+1):
    if sito[i] == 0:
        print(i)

