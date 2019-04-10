def peso_ideal(sexo,altura):
    if sexo == 1 :
        peso=(72.7*altura)-58
        print("Seu peso ideal é",peso)
    elif sexo == 2:
        peso=(62.1*altura)-44.7
        print("Seu peso ideal é",peso)
n=int(input("QUAL O SEU SEXO [1]-HOMEM [2]-MULHER"))
while n != 1 and n != 2:
    print ("VALOR INVALIDO")
    n = int(input("QUAL O SEU SEXO [1]-HOMEM [2]-MULHER"))
altura=float(input("Digite sua altura"))
peso_ideal(n,altura)

