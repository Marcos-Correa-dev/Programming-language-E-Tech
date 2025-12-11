# Há várias maneiras de iterar
# sobre dicionários,dependendo do que você deseja acessar
# (chaves, valores ou ambos)


# Ex: Iterando Sobre as Chaves do Dicionário

# Definindo um dicionário com informações de uma pessoa
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}

# Iterando sobre as chaves
for chave in pessoa: # Iterar diretamente sobre o dicionário itera sobre as chaves
    print("Chave:", chave)

# Saída Esperada:
# Chave: nome
# Chave: idade
# Chave: cidade


# ex 2 : Iterando Sobre os Valores do Dicionário

# Definindo um dicionário com informações de uma pessoa
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}

# Iterando sobre os valores
for valor in pessoa.values():
    print("Valor:", valor)

# Saída Esperada:
# Valor: Alice
# Valor: 30
# Valor: São Paulo


# Iterando Sobre os Pares Chave-Valor

# # Definindo um dicionário com informações de uma pessoa
# pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
#
# # Iterando sobre as chaves e valores
# for chave, valor in pessoa.items():
#     print(f"Chave: {chave}, Valor: {valor}")

# Saída Esperada:
# Chave: nome, Valor: Alice
# Chave: idade, Valor: 30
# Chave: cidade, Valor: São Paulo