# # Tuplas são coleções ordenadas de elementos.
# #
# # São imutáveis (não podem ser alteradas após a criação).
# #
# # Úteis quando você deseja que os dados sejam protegidos contra modificações acidentais.
#
#
# tupla_numeros = (1, 2, 3, 4, 5)
#
# # Tupla com tipos mistos
# tupla_mista = (1, "Olá", 3.14, True)
#
# # Acessando Elementos
#
# # Supondo que 'tupla_numeros' é (1, 2, 3, 4, 5)
# print(tupla_numeros[0]) # Acessa o primeiro elemento: 1
# print(tupla_numeros[-1]) # Acessa o último elemento: 5
#
#
# # Funções Importantes para Tuplas
#
# # count(): Retorna o número de ocorrências de um valor específico.
# # Supondo que 'tupla_numeros' é (1, 2, 3, 4, 5)
# ocorrencias = tupla_numeros.count(3)
# print(ocorrencias) # Output: 1
#
# # index(): Retorna o índice da primeira ocorrência de um valor.
# # Supondo que 'tupla_numeros' é (1, 2, 3, 4, 5)
# posicao = tupla_numeros.index(4)
# print(posicao) # Output: 3


# coordenadas = (10.5, 20.3)
# print("Tupla original:", coordenadas)
#
# # Tente a modificação (isso deve gerar um erro)
# try:
#     coordenadas.append(30)
# except AttributeError as e:
#     print("Erro esperado:", e)


#  Dada a tupla registro_aulas, encontre e imprima:
# O número de vezes que a string "Python" aparece
# na tupla, usando o método count().
# O índice da primeira ocorrência da string "SQL",
# usando o método index()

# registro_aulas = ("Python", "SQL", "Java", "Python", "Web", "SQL")
#
# # 1. Conte as ocorrências de "Python"
# contagem_python = registro_aulas.count()# Chame o método count() aqui
# print("Ocorrências de 'Python':", contagem_python)
#
# # 2. Encontre o índice de "SQL"
# indice_sql = registro_aulas.index()# Chame o método index() aqui
# print("Índice da primeira 'SQL':", indice_sql)




# Um sistema de cadastro armazena cada registro como uma Tupla dentro de uma Lista.
#
# Crie uma lista chamada registros com as duas tuplas fornecidas.
#
# Use a indexação para imprimir o nome ("Pedro") do segundo registro.
#
# Use o método append() para adicionar um terceiro registro (uma nova tupla:
#  ("Carla", 22, "Recife")) à lista registros.
# Imprima a lista final de registros.

registro1 = ("Ana", 28, "São Paulo")
registro2 = ("Pedro", 35, "Rio de Janeiro")

# 1. Crie a lista de registros
registros = [registro1, registro2]
print(f"1. Lista Incial:", registros)

# 2. Imprima o nome "Pedro" usando indexação
# print(registros[1][0])
# print("2.  Nome do segundo registro:", re)
npme_pedro = registros[1][0]
print(f"2. Nome do segundo registro",npme_pedro)

# 3. Crie e adicione o terceiro registro usando append()
registro3 = ("Carla", 22, "Recife")
registros.append(registro3)

# 4. Imprima a lista final
print(f"Lista final de registros:", registros)
