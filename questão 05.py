def idade(ano):
    dia=(ano*365)
    meses=dia*12
    print("Sua idade em dias é: ", dia)
    print("Sua idade em meses é: ", meses)

ano=int(input("Você tem quantos anos?: "))

idade(ano)