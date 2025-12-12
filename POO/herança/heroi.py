class Personagem:   # SuperClasse (Classe Mãe)
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

class Heroi(Personagem):  # Subclasse (classe filho)
    def __init__(self, nome, vida, habilidade):
        super().__init__(nome, vida)
        self.habilidade = habilidade

class Vilao(Personagem):
    def __init__(self, nome, vida, poder):
        super().__init__(nome, vida)
        self.poder = poder

def atacar(personagem):
    print(f"{personagem.nome} está atacando")


heroi1 = Heroi("Superman", 98, "Voo")
vilao1 = Vilao("Lex Luthor", 80, "Inteligencia")


atacar(heroi1)
atacar(vilao1)