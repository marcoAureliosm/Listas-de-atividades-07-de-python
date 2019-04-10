def fatorial(n):
    fat=1
    for i in range(1,n+1):
        fat=fat*i
    return fat
num = int(input("Digite um número: "))
print("O fatorial de {} é: {}" .format(num, fatorial(num)))
