def fat(x):
    f = 1
    for i in range(1, x + 1):
        f = f * i
    print("\n", f)
    return f


def soma(n):
    s = 1
    for i in range(1, n + 1):
        s = s + 1 / fat(i)
    return s


numero = int(input("Digite um número: "))
print("A soma é ", soma(numero))