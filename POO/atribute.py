class Carro:
    # Atributo da Classe
    roda = 4

    def __init__(self, marca, modelo):
        self.marca = marca # atributo de instância
        self.modelo = modelo # Atributo de instância

#Criando nossos OBJETOS
carro_a = Carro("Ford", "FordKa")
carro_b = Carro("BMW", "X1")

# Estamos Acessando pelo Objeto(Instância)
print(f"O {carro_a.modelo} tem {carro_a.roda} rodas.")
# Saída: O Ford tem 4 rodas.

print(f"Todo Carro deve ter {Carro.roda} rodas.")
# Saída: Todo Carro deve ter 4 Rodas.

Carro.roda = 6
print(f"Novo valor em carro_a: {carro_a.roda}")

