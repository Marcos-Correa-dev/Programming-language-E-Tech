class Interruptor:
    def __init__(self):
        self.ligado = False

    def alternar(self):
        if self.ligado:
            self.ligado = False
            print("Luz DESLIGADO")

        else:
            self.ligado = True
            print("Luz DESLIGADO")

luz_sala = Interruptor()
print(f"Luz incial: {luz_sala.ligado}")  # False

luz_sala.alternar()  # Liga: True
print(f"Luz após 1 uma alternância: {luz_sala.ligado}")

luz_sala.alternar()  # Desliga: false
print(f"Luz após 2 segunda alternância: {luz_sala.ligado}")