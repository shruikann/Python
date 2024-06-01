nome = str(input('Qual é o seu nome: '))
if nome == 'Deivison':
    print('Belo nome')
else:
    print('Seu nome não é Deivison')
print('Bom dia {}'.format(nome))

nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
media = (nota1 + nota2) / 2
print('Sua mpedia foi {:.1f}'.format(media))

if media >=6:
    print('Sua média foi boa')

else:
    print('Sua média não foi boa')
