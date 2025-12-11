# Comparação Lista vs Tupla - Mutabilidade

# Lista (Mutável)
print("\n# Lista (Mutável)")
lista = [1, 2, 3]
print("Lista original:", lista)
lista[0] = 10               # Modificando o primeiro elemento
print("Lista modificada:", lista)

# Tupla (Imutável)
print("\n# Tupla (Imutável)")
tupla = [1, 2, 3]
print("Tupla original:", tupla)
try:
    tupla[2] = 10           # Tentando modificar o primeiro elemento
    print("Isso não será executado")
except TypeError as e:
    print("Erro:", e)
    print("Tupla após tentativa:", tupla)  # A tupla permanece inalterada
