#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

alunos = ['Erick', 'Guerta', 'Donah', 'Yuri']

escolha = random.choice(alunos)
if alunos[1] == escolha :
    print('Guerta recebeu um namoradinho')
else:
    print('{} recebeu uma namoradinha'.format(escolha))

