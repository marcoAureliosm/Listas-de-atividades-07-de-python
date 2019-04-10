def media(n,n1,n2,n3):
    if n =="A":
        media=(n1+n2+n3)/3
        return media
    elif n == "P":
        media= (n1*5)+(n2*3)+(n3*2)/10
        return media
n =str(input("Digite qual função deseja usar [A]-Aritmetica [P]-Ponderada"))
while n != "A" and n != "P":
    print("Valor invalido")
    n = str(input("Digite qual função deseja usar [A]-Aritmetica [P]-Ponderada"))
nota1=int(input("Digite sua 1ª nota"))
nota2=int(input("Digite sua 2ª nota"))
nota3=int(input("Digite sua 3ª nota"))
print("SUA MEDIA É: ",media(n,nota1,nota2,nota3))