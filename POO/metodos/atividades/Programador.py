class Programador:
    def __init__(self, nome, linguagem):
        self.nome = nome
        self.linguagem = linguagem
        self.produtividade = 100

    def codificar(self, horas):
        REDUCAO_POR_HORA = 5
        reducao_total = horas * REDUCAO_POR_HORA
        self.produtividade -= reducao_total
        if self.produtividade < 0:
            self.produtividade = 0
        print(f"💻 {self.nome} codificou por {horas}h. Produtividade caiu em {reducao_total} pontos.")

    def tomar_cafe(self):
        AUMENTO = 15
        self.produtividade += AUMENTO
        if self.produtividade > 100:
            self.produtividade = 100
        print(f"☕ Produtividade de {self.nome} restaurada em {AUMENTO} pontos.")

    def verificar_produtividade(self):
        return self.produtividade


# TESTE:
alice = Programador("Alice", "Python")
print(f"Produtividade inicial: {alice.verificar_produtividade()}")
alice.codificar(5)  # Cai 25
print(f"Produtividade após codificar: {alice.verificar_produtividade()}")
alice.tomar_cafe()  # Sobe 15
print(f"Produtividade final: {alice.verificar_produtividade()}")