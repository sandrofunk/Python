a = "João"
b = "Silva"

concatenar = a + " " + b

print(concatenar) #concatena as variáveis a e b
print(concatenar.lower()) #função lower retorna a string em minusculo
print(concatenar.upper()) #função upper retorna a string em maiusculo
print(concatenar.strip()) #remove espaços

###

frase = "Esse texto é um exemplo"
lista = frase.split() #função split converte string em lista
print(lista)

###

busca = frase.find("um") #comando busca a posição da string
print(busca)

###

altera = frase.replace("Esse texto", "Essa frase")
print(altera)