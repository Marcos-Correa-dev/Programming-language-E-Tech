# Dicionários são coleções desordenadas de pares chave-valor.
#
# Cada chave é única.
#
# Muito úteis para armazenar dados que precisam ser acessados por uma chave identificadora.

# ***Criando um Dicionário e Acessando Valores

# Dicionário com informações de uma pessoa
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}

# Acessando Valores
print(pessoa["nome"]) # Acessa o valor associado à chave "nome": Alice

# Outras Formas de Criação

# Criando um dicionário vazio
dicionario_vazio = dict()
print(dicionario_vazio) # Output: {}

# Criando um dicionário com pares chave-valor
dicionario_pessoa = dict(nome="Alice", idade=30, cidade="São Paulo")
print(dicionario_pessoa) # Output: {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}

# Funções Importantes para Dicionários

# Supondo que 'pessoa' é {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}

# keys(): Retorna uma lista (ou view) das chaves no dicionário.
chaves = pessoa.keys()
print(chaves) # Output: dict_keys(['nome', 'idade', 'cidade'])

# values(): Retorna uma lista (ou view) dos valores no dicionário.
valores = pessoa.values()
print(valores) # Output: dict_values(['Alice', 30, 'São Paulo'])

# items(): Retorna uma lista (ou view) de pares chave-valor (tuplas).
itens = pessoa.items()
print(itens) # Output: dict_items([('nome', 'Alice'), ('idade', 30), ('cidade', 'São Paulo')])


# get() e Modificação

# get(): Retorna o valor associado a uma chave, mas evita um erro se a chave não existir, retornando um valor padrão (ou None)[cite: 42].
# Supondo que 'pessoa' é {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
idade = pessoa.get("idade")
print(idade) # Output: 30

# Tentando acessar uma chave inexistente sem causar um erro
estado = pessoa.get("estado", "Desconhecido")
print(estado) # Output: Desconhecido

# update(): Atualiza o dicionário com pares chave-valor de outro dicionário ou de um iterável de pares.
pessoa.update({"idade": 31, "estado": "SP"})
print(pessoa) # Output: {'nome': 'Alice', 'idade': 31, 'cidade': 'São Paulo', 'estado': 'SP'}

# pop(): Remove a chave especificada e retorna o valor correspondente.
idade_removida = pessoa.pop("idade")
print(idade_removida) # Output: 31
print(pessoa) # Output: {'nome': 'Alice', 'cidade': 'São Paulo', 'estado': 'SP'}