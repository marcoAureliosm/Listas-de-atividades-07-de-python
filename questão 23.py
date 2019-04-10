def soma(n):
    s = 0
    j=2
    k=4
    l=2
    for i in range(1,n+1):
        s = s + (j/k)+(((n*n)+1)/(n+3))
        k+=1
        j=j+i+l
        l+=l
    return s

while True:
    try:
        numero = int(input("Digite um número (Digite 0 para finalizar): "))
        if numero == 0: break
        print("A soma é %f" % soma(numero))
    except:
        print("Número inválido. Digite novamente!")