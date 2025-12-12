class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def info(self):
        super().info()
        print(f"Marca: {self.marca} Modelo: {self.modelo}")

carro = Veiculo("BMW", "X1")
carro.info()
