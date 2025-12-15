class Funcionario:
    def __init__(self, nome):
        self.__nome = nome  # atributo privado.

    def get_nome(self):
        return self.__nome  # GETTER

    def calcular_salario(self):
        return 0  # É o metodo que vai ser sobrescrito (polimorfismo)

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario_fixo):
        super().__init__(nome)
        self.__salario = salario_fixo

    def get_salario(self):
        return self.__salario  #GETTER

    def calcular_salario(self):
        return self.__salario

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.__horas = horas_trabalhadas
        self.__valor_hora = valor_hora

    def calcular_salario(self):
        return self.__horas * self.__valor_hora # Salário por HORA


# ------ Programa Principal ------

funcionarios = [] # Lista de Objetos.
total_folha = 0

quantidade = int(input("Quantos funcionario deseja cadastrar ?"))

for i in range(quantidade):
    print("\n1 Funcionario CLT")
    print("2 - Funcionario Horista")
    tipo = int(input("Escolha o tipo de funcionario ?"))

    nome = input("Digite o nome do funcionario: ")

    if tipo == 1:
        salario = float(input("Digite o Salário fixo: "))
        funcionario = FuncionarioCLT(nome, salario)

    elif tipo == 2:
        horas = float(input("Digite as horas trabalhadas: "))
        valor = float(input("Digite o valor da hora: "))
        funcionario = FuncionarioHorista(nome, horas, valor)

    else:
        print("Tipo invalido. Funcionario não encontrado")
        break

    funcionarios.append(funcionario)


print("\n--- Folha de Pagamento --")

for f in funcionarios:
    salario = f.calcular_salario() # Polimorfismo
    print(f"{f.get_nome()} - Salário: R$ {salario:.2f}")
    total_folha += salario

print(f"\nTotal de folha de pagamento: R$ {total_folha:.2f}")