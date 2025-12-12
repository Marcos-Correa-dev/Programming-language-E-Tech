class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} faz som genérico.")

class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} da raça {self.raca} está latindo: au au")

    def mostrar_detalhes(self):
        print(f"Nome: {self.nome} | Especie: {self.especie} | Raça: {self.raca}")

class Gato(Animal):
    def __init__(self, nome, especie, cor_pelo, raca):

        super().__init__(nome, especie)

        self.cor_pelo = cor_pelo
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} da raça {self.raca} está miando: miau miau!")

    def mostrar_detalhes(self):
        print(f"Nome {self.nome} | Especie: {self.especie} | Raça: {self.raca} | Cor do pelo: {self.cor_pelo}")

# criação de objeto
doguinho = Cachorro("Ducky", "Canino", "Golden Retriever")

print(f"Nome herdado: {doguinho.nome}")

doguinho.fazer_som() # Ducky da raça Golden Retriever está latindo: au au

doguinho.mostrar_detalhes()

gato = Gato("Laura", "Felino", "Branco", "Siamês")

print(f"Nome herdado: {gato.nome}")

gato.fazer_som()

gato.mostrar_detalhes()