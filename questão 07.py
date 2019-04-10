def categoria(idade):
    if idade >= 5 and idade <=7:
        return "A"
    elif idade >8 and idade <=10:
        return "B"
    elif idade >= 11 and idade <= 13:
        return "jA"
    elif idade >=14 and idade <=17:
        return "jB"
    elif idade >=18:
        return "AB"
n=int(input("DIGITE A SUA IDADE"))
if categoria(n) =="A":
    print("INFANTIL A")
elif categoria(n) == "B":
    print("INFANTIL B")
elif categoria(n) == "jA":
    print("JUVENIL A")
elif categoria(n) == "jB":
    print("JUVENIL B")
elif categoria(n) == "AB":
    print("ADULTO")