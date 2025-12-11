class Nave:

    def __init__(self, nome, combustivel1):
        self.nome = nome
        self.combustivel1 = combustivel1
        self.status = "Estacionada"

    # Metodo para decolar a nave
    def decolar(self):
        # Primero verificamos se há combustoivel na Nave(Pelo meno 20)
        if self.combustivel1 >= 20:
            self.combustivel1 -= 20    # Gasta 20 unidade de combustivel
            self.status = "Em voo"      # Atualiza o status da Nave
            print(f"{self.nome} decolou! Combustivel restante: {self.combustivel1}")
        else:
            print("Combustivel insuficiente!")

    def recarregar(self, quantidade):
        self.combustivel1 += quantidade
        print(f"Combustivel recarregado. Nivel atual dele: {self.combustivel1}")

    def verificar_status(self):
        print(f" Nave: {self.nome} | Status: {self.status} | Combustivel: {self.combustivel1}")

n1 = Nave("Apolo 11", 10)

n1.verificar_status()     # Mostra o status atual da Nave

n1.decolar()      # Tenta decolar, mas não vai conseguir

n1.recarregar(50)   # Recarregar combustivel

n1.decolar()    # Agora a nave consegue decolar

n1.verificar_status()    # Mostra o novo status (atual)