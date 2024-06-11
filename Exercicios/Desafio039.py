from datetime import date

atual = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você precisa se alistar, já')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você ainda não pode se alistar, faltam {} anos'.format(saldo))
    print('SSeu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Você deveria ter se alistado a {} anos atrás'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
