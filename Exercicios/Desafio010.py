#Crie um algoritmo que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

reais = float(input('Informe quanto você tem em reias: '))

dolar = 5.15
convert = reais / dolar
convert = round(convert, 2)

print('Você pode comprar US$ {}'.format(convert))
