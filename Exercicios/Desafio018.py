#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você quer o seno, cosseno e tangente: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo é {}° e seu seno é {:.2f}. seu cossseno é {:.2f} e sua tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))