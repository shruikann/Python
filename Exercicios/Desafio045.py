from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
jogador = int(input('O que você irá jogar, escolha uma das opções: '))

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    else:
        print('COMPUTADOR GANHOU')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('JOGADOR GANHOU')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    else:
        print('EMPATE')

