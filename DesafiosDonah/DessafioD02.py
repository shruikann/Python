frase = str(input('Digite uma frase ')).upper().strip()
palavra = str(input('Digite uma palavra ')).upper().strip()
split_frase = frase.split()

print(palavra in split_frase)
print(split_frase)