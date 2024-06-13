
massa = float(input('Informe sua massa: '))
altura = float(input('Informe sua altura:'))

imc = massa/(altura * altura)

if imc <18.5 :
    print('Abaixo do peso, IMC de {:.1f}'.format(imc))
elif imc <25 :
    print('Peso ideal, IMC de {:.1f}'.format(imc))
elif imc <30 :
    print('Sobrepeso, IMC de {:.1f}'.format(imc))
elif imc <=40 :
    print('Obesidade, IMC de {:.1f}'.format(imc))
else:
    print('Obesidade mórbida, IMC de {:.1f}'.format(imc))