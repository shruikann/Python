num_list = []

for tamanho in range(0,3):
    num = int(input('Digite um número inteiro '))
    #adicionando elementos a lista
    num_list.append(num)

#organiza a lista em forma crescente, (reverse=True) organiza a lista descendente
num_list.sort()
print('O menor número é {}'.format(num_list[0]))
print('O maior número é {}'.format(num_list[-1]))



