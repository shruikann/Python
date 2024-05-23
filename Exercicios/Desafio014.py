#Crie um algoritmo que leia a temperatura em Celsius e converta para Fahrenheit

celsius = float(input('Digite a temperatura em Celsius: '))

converte = (celsius * 1.8) + 32

print('{}C em Fahrenheit é: {}F'.format(celsius, converte))