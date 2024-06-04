salario = float(input('Digite o salário atual para calcularmos seu aumento'))

if salario <= 1250:
    sal_aumento = salario + (salario * 15/100)
    print('Seu salário era R${:.2f}, agora é de R${:.2f}'.format(salario, sal_aumento))

else:
    sal_aumento = salario + (salario * 10/100)
    print('Seu salário era R${:.2f}, agora é de R${:.2f}'.format(salario, sal_aumento))