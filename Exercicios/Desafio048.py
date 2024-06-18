soma = 0
cont_num = 0
for mult in range(1, 501, 2):
    if mult % 3 == 0:
        cont_num = cont_num + 1
        soma = soma + mult

print(soma)
print(cont_num)
