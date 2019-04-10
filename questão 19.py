def divisores(n):
    l=[]
    for i in range(2, n):
        if n % i == 0:
            l.append(i)
    return l
n=int(input("DIGIRE UM VALOR"))
print("DIVISORE DE {} SAO: {}".format(n,divisores(n)))