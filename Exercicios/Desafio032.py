from datetime import date

ano = int(input('Digite o ano que você quer analisar, coloque 0 para analisar o ano atual: '))
#ano bissexto são anos multiplos de 4, porém não multiplos de 100, mas multiplos de 400 são anos bissextos
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano de {} é bissexto'.format(ano))

else:
    print('O ano de {} não é bissexto'.format(ano))
