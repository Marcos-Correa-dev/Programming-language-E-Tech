class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    # Método que retorna o salário
    # Aqui pode ser sobrescrito futuramente (polimorfismo)
    def calcular_salario(self):
        return self.__salario