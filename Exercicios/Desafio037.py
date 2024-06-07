num = int(input('Digite a medida a ser convertida: '))


converte = int(input('Digite o número da opção escolhida: '))
print('BINÁRIO: 1 ')
print('OCTAL: 2')
print('HEXADECIMAL: 3')

while converte < 1 or converte > 3:
    print('Opção inválida, escolha entre 1, 2 ou 3 ')
    converte = int(input('Digite o número da opção escolhida: '))

if converte == 1:
    bin_conv = bin(num)[2:]
    print('{} convertido para binário é: {}'.format(num, bin_conv))

elif converte == 2:
    oct_conv = oct(num)[2:]
    print('{} convertido para octal é: {}'.format(num, oct_conv))

else:
    hex_conv = hex(num)[2:]
    print('{} convertido em hexadecimal é: {}'.format(num,hex_conv))
