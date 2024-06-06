info_loan = {}

#input das informações
house_value = float(input('Informe o valor da casa: '))
payment = float(input('Informe a sua renda: '))
loan_isntall = int(input('Informe o número de parcelas: '))
value = 'Valor'
pay = 'Salário'
installment = 'Parcelas'

#construção do dicionário
info_loan[value] = house_value
info_loan[pay] = payment
info_loan[installment] = loan_isntall

#operaçoes com dicionário
value_install = info_loan[value] / info_loan[installment]
value_pay = info_loan[pay] * 30/100

if value_install > value_pay:
    print('Não aprovado, valor da parcela escede 30% do salário')
    print('Valor parcela: R${:.2f}'.format(value_install))
    print('Salario parcela: R${:.2f}'.format(value_pay))
else:
    print('Aprovado, parabéns')
    print('Valor parcela: R${:.2f}'.format(value_install))
    print('Salario parcela: R${:.2f}'.format(value_pay))

print(info_loan)