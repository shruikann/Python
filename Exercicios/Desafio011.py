#Crie um algoritmmo em que o usuario informa a altura e o comprimento de uma parede, calcule sua area e informe quantos litros de tinta serão utilizdos para pintar essa parede

altura = float(input('Altura da parede '))
comprimento = float(input('Comprimento da parede '))

area = comprimento * altura
tinta = area / 2

print('Área da parede: {}, serão necessários {} litros de tinta para pintar essa parede'.format(area, tinta))