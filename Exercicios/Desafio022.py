nome = str(input('Digite seu nome completo ')).strip()#retira os espaços no começo e no fim da palavra

print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúscula é: {}'.format(nome.lower()))

#contar numero de letras sem espaços
conta_nome = len(nome) - nome.count(' ')
print('Seu nome tem o total de {} letras'.format(conta_nome))

#contar letras do primeiro nome
split_word = nome.split()
first_word = len(split_word[0])
print('Seu primeiro nome tem {} letras'.format(first_word))












