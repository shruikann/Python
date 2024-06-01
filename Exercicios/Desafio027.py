nome = input('Digite seu nome completo').strip()

name_split = nome.split()

print('Seu primeiro nome é: {}'.format(name_split[0]))
print('Seu último nome é : {}'.format(name_split[-1]))#acessa o ultimo elemento da lista
