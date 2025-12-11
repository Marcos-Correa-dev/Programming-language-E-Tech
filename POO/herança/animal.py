class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.saudavel = True

    def fazer_som(self):
        print(f"{self.nome} faz um som genérico.")


class Cachorro(Animal):  # Cachorro HERDA de Animal

    # 1. Construtor (Adiciona o novo atributo 'raca')
    def __init__(self, nome, especie, raca):
        # 2. Chama o construtor da classe MÃE (Animal)
        # O super() inicializa 'nome' e 'especie' para nós.
        super().__init__(nome, especie)
        # 3. Inicializa o novo atributo exclusivo da Subclasse
        self.raca = raca

    # 4. Sobrescreve o metodo (Polimorfismo Básico)
    def fazer_som(self):
        print(f"{self.nome} da raça {self.raca} está latindo: Au Au!")

    # 5. Metodo exclusivo
    def mostrar_detalhes(self):
        print(f"Nome: {self.nome} | Espécie: {self.especie} | Raça: {self.raca}")


class Gato(Animal):
    def __init__(self, nome, especie, cor_pelo):
        # 1. Chama o construtor da Superclasse (Animal)
        super().__init__(nome, especie)

        # 2. Inicializa o atributo exclusivo da Subclasse
        self.cor_pelo = cor_pelo



# Criação do Objeto Cachorro
doguinho = Cachorro("Buddy", "Canino", "Golden Retriever")

print("--- Testando Herança de Atributos e Métodos ---")

# Acessando Atributos herdados:
print(f"Nome herdado: {doguinho.nome}")
print(f"Status de saúde herdado: {doguinho.saudavel}") # Atributo inicializado no __init__ de Animal

# Chamando o Método Sobrescrito (Polimorfismo):
doguinho.fazer_som() # Saída: Buddy da raça Golden Retriever está latindo: Au Au!

# Chamando o Método exclusivo:
doguinho.mostrar_detalhes()

gato_mimi = Gato("Mimi", "Felino", "Branco")
print(f"Nome do gato: {gato_mimi.nome} | Cor do Pelo: {gato_mimi.cor_pelo} | Saúde Herdada: {gato_mimi.saudavel}")