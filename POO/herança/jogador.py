class Jogador:
    def __init__(self, nome, idade, time):
        self.nome = nome
        self.idade = idade
        self.time = time

    def acao_principal(self):
        print(f"{self.nome} realiza uma ação genérica no jogo.")

    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Time: {self.time}")


class Atacante(Jogador):
    def __init__(self, nome, idade, time, gols):
        super().__init__(nome, idade, time)
        self.gols = gols  # gols marcados na temporada

    # Polimorfismo: sobrescrita
    def acao_principal(self):
        print(f"{self.nome} avança para o ataque e chuta a gol!")

    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Posição: Atacante | Idade: {self.idade} | "
              f"Time: {self.time} | Gols na temporada: {self.gols}")


class Zagueiro(Jogador):
    def __init__(self, nome, idade, time, desarmes):
        super().__init__(nome, idade, time)
        self.desarmes = desarmes  # desarmes feitos na temporada

    def acao_principal(self):  # ação
        print(f"{self.nome} faz um desarme preciso e salva a defesa!")

    def mostrar_dados(self): #ação
        print(f"Nome: {self.nome} | Posição: Zagueiro | Idade: {self.idade} | "
              f"Time: {self.time} | Desarmes na temporada: {self.desarmes}")


atacante = Atacante("Pedro", 26, "Flamengo", 22)
zagueiro = Zagueiro("Gustavo Gómez", 30, "Palmeiras", 95)

print("--- Testando Jogadores de Futebol ---")

atacante.mostrar_dados()
atacante.acao_principal()

print()

zagueiro.mostrar_dados()
zagueiro.acao_principal()
