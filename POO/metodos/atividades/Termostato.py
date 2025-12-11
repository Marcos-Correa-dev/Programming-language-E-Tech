class Termostato:
    def __init__(self, temperatura=20):
        # Atributo da Instância
        self.temperatura = temperatura

    # Metódo adiciona graus à temperatura
    def aumentar(self, graus):
        self.temperatura += graus
        print(f"Temperatura aumentada para: {self.temperatura}")

    def diminuir(self, graus):
        self.temperatura -= graus
        print(f"Temperatura diminuida para {self.temperatura}")

# TESTE
meu_termostato = Termostato()
print(f"inicial!: {meu_termostato.temperatura}")
meu_termostato.aumentar(3)
meu_termostato.diminuir(1)
print(f"Temeperatura final: {meu_termostato.temperatura} graus")