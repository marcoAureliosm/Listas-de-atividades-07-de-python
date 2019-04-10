def perfeito(n):
    divisores=0
    soma=0
    for i in range(1,n):
        if n % i==0:
            divisores=i
            soma=soma+divisores

    if soma==n:
        return soma
    else:
        return soma

n=int(input("DIGITE O SEU VALOR"))
if perfeito(n):
    print("NUMERO PERFEITO: ",n)
else:
    print("Esse numero não é perfeito: ",n)