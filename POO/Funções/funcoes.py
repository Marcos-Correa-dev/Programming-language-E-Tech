def saudacao():
    print("Olá, mundo")

saudacao()

# Passando valores por parametros

def saudacao(nome):
    print(f"Ola, {nome}")

saudacao("João")


# ELA RETORNAR UM VALOR USANDO UMA PALAVRA CHAMDA "retur"

def soma(a, b):
    return a + b

resultado = soma(5,4)
print(resultado)

# função permite retornar multiplos valores usando tupla

def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto

q, r = dividir(10,3)
print(f"quociente: {q} e resto: {r}")  # Output:  3,1

def soma(*dados):
    resultado = 0
    for num in dados:
        resultado += num
    return resultado

# exeplo de uso
print(soma(1,2,3,4)) # saida: 10
print(soma(10,20)) # saída: 30


# Imagine que você quer uma função para registrar
# os nomes de todos os convidados para um evento,
# mas você não sabe quantos convidados haverá.
# Neste caso, a função recebe qualquer
# número de nomes e os exibe.
# Utilize um if com interação com args e
# retorne esses nomes:
# ("Reunião de Equipe",
#   "Marcos", "Alice", "João", "Sofia”)

def lista_convidados(formatura, *args):
    print(f"Evento: {formatura}")

    if args:   # Verifica se a tupla args não está vázia
        print("Convidados:")
        for nome in args:
            print(f"- {nome}")
    else:
        print("Nenhum convidado registrado.")

lista_convidados("Reunião de equipe",
                 "Marcos", "Alice",
                 "João", "Sofia")


def criar_etiqueta_produto(nome_produto, *caracteristicas):

    print(f"\n--- PRODUTO: {nome_produto} ---")

    if caracteristicas:
        print("Características:")
        for item in caracteristicas:
            print(f"  • {item}")
    else:
        print("Nenhuma característica adicional registrada.")


criar_etiqueta_produto("Smartphone X10",
                       "128GB de Armazenamento")
