#Crie um algoritmmo que mostre a tabuada de um numero digitado

tabuada = int(input('Digite a tabuada desejada'))

for count in range(10):
    print('{} x {} = {}'.format(tabuada, count+1, tabuada*(count+1)))