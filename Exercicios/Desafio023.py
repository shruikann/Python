num = int(input('Digite um numero: '))

#convert_num = str(num)
#split_num = convert_num.split()

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Unidades: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print(('Milhar: {}'.format(milhar)))

