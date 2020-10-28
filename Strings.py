# Operações com Strings
# Neste programa apresento como funciona 
# a declaração e a execução das strings

a = "Paulo"
b = "Silva"

concatenar = a + " " + b # concatena as variáveis a e b
print(concatenar)


tamanho = len(concatenar) # a função len conta a qtde de caracteres
print(tamanho)

print(a[2]) # imprimi a posição que se encontra
print(concatenar[0:11])

print(concatenar.lower()) # imprimi em minusculo
print(concatenar.upper()) # imprimi em maiusculo

concatenar = concatenar.lower() # transforma para minusculo
print(concatenar) 