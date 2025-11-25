inteiro = 10    # int (número inteiro)
decimal = 10.5  # float (número decimal)
complexo = 3 + 4j       # complex (número complexo)

print(inteiro, decimal, complexo)
print(f"Tipos: {type(inteiro)}, {type(decimal)}, {type(complexo)}")

# Texto
Texto = "Olá, mundo!" #str (string/texto)
print(Texto)
print(f"Tipos: {type(Texto)}")

# booleanos

verdadeiro = True  # bool (booleano verdadeiro)
falso = False # bool (booleano falso)

print(verdadeiro, falso)
print(f"Tipos: {type(verdadeiro)}, {type(falso)}")

# Coleções

lista = [1, 2, 3]  # list (lista mutável)
tupla = (1, 2, 3)  # tupla (tupla imutável)
dicionario = {"nome": "Marcos"} # dict (dicionário)
conjunto = {1, 2, 3} # set (conjunto)
print(lista, tupla, dicionario, conjunto)
print(f"Tipos: {type(lista)}, {type(tupla)}, {type(dicionario)}, {type(conjunto)}")