def somatorio (n):
    soma=0

    for i in range(1,n+1):
        soma=soma+i
    return soma
n=int(input("digite um valor"))
print("SOMATORIA DO VALOR DIGITADO",somatorio(n))
