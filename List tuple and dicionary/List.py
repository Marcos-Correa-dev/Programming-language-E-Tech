# Listas são coleções ordenadas de elementos.
#
# São mutáveis (podem ser alteradas).
#
# Podem conter elementos de tipos diferentes, incluindo outras listas.


# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Lista mista com diferentes tipos de dados
mista = [1, "Olá", 3.14, True]
print(mista)


# ///====


# Declarando Listas com list()

# Criando uma lista vazia
lista_vazia = list()
print(lista_vazia) # Output: []

# Criando uma lista a partir de uma sequência
lista_numeros = list([1, 2, 3, 4, 5])
print(lista_numeros) # Output: [1, 2, 3, 4, 5]

# Criando uma lista a partir de uma string (a string será dividida em caracteres)
lista_caracteres = list("Python")
print(lista_caracteres) # Output: ['P', 'y', 't', 'h', 'o', 'n']

# Criando uma lista a partir de um range
lista_range = list(range(5))
print(lista_range) # Output: [0, 1, 2, 3, 4]


# Acessando Elementos
#
# Python

# Supondo que 'numeros' é [1, 2, 3, 4, 5]
print(numeros[0]) # Acessa o primeiro elemento: 1
print(numeros[-1]) # Acessa o último elemento: 5



numeros.append(6)
print(numeros) # Output: [1, 2, 3, 4, 5, 6]

# remove() Exemplo

# Supondo que 'numeros' é [1, 2, 3, 4, 5, 6]
numeros.remove(3)
print(numeros) # Output: [1, 2, 4, 5, 6]

# pop() Exemplo


# Supondo que 'numeros' é [1, 2, 4, 5, 6]
ultimo = numeros.pop()
print(ultimo) # Output: 6
print(numeros) # Output: [1, 2, 4, 5]


# index() Exemplo


# [1, 2, 4, 5]
posicao = numeros.index(4)
print(posicao) # Output: 2