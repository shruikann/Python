#criar uma tabuada em que o usuário informe onde quer começar e parar

tabuada = int(input('Informe a tabuada desejada'))
inicio = int(input('Informe por onde você quer começar: '))
final = int(input('Informe onde você quer terminar: '))
if inicio > final:
    temp = inicio
    inicio = final
    final = temp

for count in range(inicio, final+1):
    conta =tabuada * count
    print('{} x {} = {}'.format(tabuada, count, conta))