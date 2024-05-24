# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.

from math import hypot

cateto1 = float(input('Digite o primeiro cateto'))
cateto2 = float(input('Digite o segundo cateto'))

hipotenusa = hypot(cateto1, cateto2)

print('A hipotenusa do tringulo retangulo com catetos {} e {} é {:.2f}'.format(cateto1, cateto2, hipotenusa))
