def par(n):
    if n %2==0:
        return True
    else:
        return False
n=int(input("digite um valor"))
if par(n):
    print("VALOR PAR")
else:
    print("VALOR IMPAR")
