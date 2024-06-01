distancia = int(input('Digite a distância da sua viagem: '))
passagem = 0
if distancia <= 200:
    passagem = distancia * 0.5
    print('Sua passagem irá custar R${}'.format(passagem))

else:
    passagem = distancia * 0.45
    print('Sua passagem irá custar R${}'.format(passagem))
