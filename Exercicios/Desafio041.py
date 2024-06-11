from datetime import date

atual = date.today().year

ano_nasc = int(input('Ano de nascimento: '))
idade = atual - ano_nasc

if idade <= 9:
    print('Competidor tem {} anos, sua categoria é MIRIM'.format(idade))

elif 9 < idade <= 14:
    print('Competidor tem {} anos, sua categoria é INFANTIL'.format(idade))

elif 14 < idade <= 19:
    print('Competidor tem {} anos, sua categoria é JÚNIOR'.format(idade))

elif 19 < idade <= 25:
    print('Competidor tem {} anos, sua categoria é SÊNIOR'.format(idade))

else:
    print('Competidor tem {} anos, sua categoria é MASTER'.format(idade))
