produto = float(input('Informe o valor do produto: '))

print('Escolha a forma de pagamento')

print('1 => à vista dinheiro/chque: 10% de desconto')
print('2 => à vista no cartão: 5% de desconto')
print('3 => em até 2x no cartao: preço normal')
print('4 => 3x ou mais no cartão: 20% de juros')

condicao = int(input('Forma de pagamento: '))

if condicao == 1:
    preco = produto - (produto * 10/100)
    print('O produto custava R${:.2f}, com o desconto de 10% custará R${:.2f}'.format(produto, preco))

elif condicao == 2:
    preco = produto - (produto * 5/100)
    print('O produto custava R${:.2f}, com o desconto de 5% custará R${:.2f}'.format(produto, preco))

elif condicao == 3:
    print('Esta condição de pagamento não oferece desconto')

elif condicao == 4:
    preco = produto + (produto * 20/100)
    print('O produto custava R${:.2f}, com os juros de 20% custará R${:.2f}'.format(produto, preco))

else:
    print('Opção inaválida de pagamento. Tente novamente.')
