#crie um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Preço do produto: '))

desconto = 5/100
produtodesc = produto - (produto*desconto)

print('Preço do produto com 5% de desconto: R${}'.format(produtodesc))