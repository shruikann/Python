# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro foi alugado: '))
distancia = int(input('Quantos quilometros o carro andou: '))

preco = dias * 60 + distancia * 0.15

print('O Valor a ser pago é de : R${}'.format(preco))