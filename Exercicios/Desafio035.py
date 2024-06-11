triangulo = []

for tamanho in range(0, 3):
    lado = float(input('Digite o tamanho das retas '))
    triangulo.append(lado)

if (triangulo[0] + triangulo[1] > triangulo[2]
        and triangulo[0] + triangulo[2] > triangulo[1]
        and triangulo[1] + triangulo[2] > triangulo[0]):

    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')
