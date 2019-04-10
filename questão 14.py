def tipo_triangulo(a, b, c):
    if (a <= b + c):
        print('formar um triangulo')

        if (a == b == c):
            print('triangulo eqüilátero')

        elif (a == b != c) or (a == c != b) or (b == c != a):
            print('triangulo Isosceles')

        elif (a != b != c):
            print('Triangulo escaleno')
        else:
            print('Não é um triangulo')


a = int(input('Digite o valor de um dos lados do triangulo'))
b = int(input('Digite o valor de um dos lados do triangulo'))
c = int(input('Digite o valor de um dos lados do triangulo'))

tipo_triangulo(a, b, c)
