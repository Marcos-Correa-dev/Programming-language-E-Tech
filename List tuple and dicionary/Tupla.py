# Tuplas são coleções ordenadas de elementos.
#
# São imutáveis (não podem ser alteradas após a criação).
#
# Úteis quando você deseja que os dados sejam protegidos contra modificações acidentais.


tupla_numeros = (1, 2, 3, 4, 5)

# Tupla com tipos mistos
tupla_mista = (1, "Olá", 3.14, True)

# Acessando Elementos

# Supondo que 'tupla_numeros' é (1, 2, 3, 4, 5)
print(tupla_numeros[0]) # Acessa o primeiro elemento: 1
print(tupla_numeros[-1]) # Acessa o último elemento: 5


# Funções Importantes para Tuplas

# count(): Retorna o número de ocorrências de um valor específico.
# Supondo que 'tupla_numeros' é (1, 2, 3, 4, 5)
ocorrencias = tupla_numeros.count(3)
print(ocorrencias) # Output: 1

# index(): Retorna o índice da primeira ocorrência de um valor.
# Supondo que 'tupla_numeros' é (1, 2, 3, 4, 5)
posicao = tupla_numeros.index(4)
print(posicao) # Output: 3