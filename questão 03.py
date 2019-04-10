def primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))
if primo(numero) == True:
    print("O número %d é primo." % numero)
else:
    print("O número %d não é primo." % numero)
