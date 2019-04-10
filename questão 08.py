def positivo(n):
    if n >0:
        return True
    else:
        return False
n=int(input("DIGITE UM VALOR"))
if positivo(n):
    print("VALOR POSITIVO")
else:
    print("Negativo")
