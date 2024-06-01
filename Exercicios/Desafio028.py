from random import randint
print('Vou pensar em um número entre 1 e 5, tente adivinhar')
comp_num = randint(1,5)

palpite = int(input('Digite um numero de 1 á 5: '))

while palpite > 5 or palpite < 0:
    print('Digite um número válido: ')
    palpite = int(input('Digite um numero de 1 á 5: '))

if palpite == comp_num:
    print('Você acertou o número')

else:
    print('Você errou, o número sorteado foi {}'.format(comp_num))



