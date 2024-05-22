#Crie um algoritmo que leia o salário de um funcionmário e mostre seu novo salário , com 15% de aumento
salario = float(input('Informe o salário atual '))

aumento = 15/100
salarioAumento = salario + (salario * aumento)

print('Novo salário é de R${}'.format(salarioAumento))