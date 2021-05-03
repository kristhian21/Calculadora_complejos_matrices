import math


def raizB(numero):
    cont = 0

    x = numero / 2

    while cont < 1000:
        if x * x == numero:
            return x
        else:
            x = (x + (numero / x)) / 2
        cont += 1

    return x


n = int(input())
print(math.sqrt(n))
print()
print(raizB(n))
