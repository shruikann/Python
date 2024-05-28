frase = 'Curso em Vídeo Python'
#fatiar string quando, começando do inciio da string até o final, pulando de 2 em 2
print(frase[::2])
print(frase.upper())
print(frase.count('e'))
print(len(frase))
print(frase.replace('Vídeo', 'Foto')) #[e uma variável temporária, não altera a string se outra variavel não fpi atribuida
print('Foto' in frase) #verifica se existe a palavra dentro da string e retorna true ou false
print(frase.find('Curso'))#verifica se existe a palavra e retorna a posição em que ela começa
print(frase.split())
