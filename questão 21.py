def soma(n):
    s = 0
    for i in range(1, n + 1):
        s = s + 1 / i
    return s


while True:
    try:
        numero = int(input("Digite um número (Digite 0 para finalizar): "))
        if numero == 0: break
        print("A soma é %f" % soma(numero))
    except:
        print("Número inválido. Digite novamente!")

