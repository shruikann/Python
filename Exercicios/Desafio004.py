info = input('Digite algo ')

print('O tipo primitivo desse valor é', type(info))
print('É só espaços?', info.isspace())
print('É um número', info.isnumeric())
print('É só letras', info.isalpha())
print('É alfanumerico', info.isalnum())
print('Está em maiúsculas', info.isupper())
print('Está em minúscula', info.islower())
print('Está capitalizada', info.istitle())

