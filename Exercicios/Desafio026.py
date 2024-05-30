frase = str(input('Digite uma frase ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primmeira letra A aparece na posição {}'.format(frase.find('A')))
#começa a busca pela direita
print('A últimma letra A aparece na posição {}'.format(frase.rfind('A')))