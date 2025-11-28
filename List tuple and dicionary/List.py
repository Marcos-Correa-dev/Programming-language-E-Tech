# criando uma lista de números

numeros = [1,2,3,4,5]
print(numeros)

mistos = [1, "olá", 3.14, True]
print(mistos)

lista_vazia = list()
print(lista_vazia)

# Criando uma lista a partir de uma sequência
lista_numeros = list([1,2,3,4,5])
print(lista_numeros)

# Criando uma lista a partir de uma string (a string será dividida em caracteres)

lista_caracteres = list("Python")
print(lista_caracteres)

#  Criando uma lista a partir de uma regra

lista_regra = list(range(5))
print(lista_regra)



# append() adiciona um elemento no final da lista.

# Supondo que 'numeros' é [1,2,3,4,5]
numeros.append(6)
print(numeros)


#  remove() :  remove a ocorrência de um valor específico.

numeros.remove(3)
print(numeros)


# pop()

# remove e retorne o elemento em um posição especifica.

ultimo = numeros.pop()
print(ultimo)
print(numeros)