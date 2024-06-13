triangulo = []

for tamanho in range (0,3):
    lados = float(input("Informe os comprimentos de retas: "))
    triangulo.append(lados)

if (triangulo[0] + triangulo[1] > triangulo[2]
        and triangulo[0] + triangulo[2] > triangulo[1]
        and triangulo[1] + triangulo[2] > triangulo[0]):
    print('Os segmentos informados, podem formar um triângulo')
    if triangulo[0] == triangulo[1]  == triangulo[2]:
        print('Esse triângulo é EQUILÁTERO')
    elif triangulo[0] != triangulo[1] != triangulo[2] != triangulo[0]:
        print('Esse triângulo é ESCALENO')
    else:
        print('Esse triângulo é ISÓSCELES')
else:
    print('Não é possível forma um triângulo')
