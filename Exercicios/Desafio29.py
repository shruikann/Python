velocidade = int(input('Informe a velocidade do carro '))

vel_limite = 80
multa = (velocidade - vel_limite) * 7

if velocidade > vel_limite:
    print('Você passou o limite de velocidade em {}km/h você foi multado em R${}'.format(velocidade - vel_limite, multa))

else:
    print('Boa viagem, dirija com segurança')




