def tabuada(n):
    for i in range(1,11):
        tabuada=n*i
        print("{} x {} = {} ".format(n,i,tabuada))
n=int(input("DIGIT O NUMERO"))
print(tabuada(n))