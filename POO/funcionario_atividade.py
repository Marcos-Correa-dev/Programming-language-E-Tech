class Funcionario:

    taxa_bonus = 0.10

    def __init__(self, nome, cargo, salario):

        self.nome =nome

        self.cargo = cargo

        self.salario = int(salario)

    def calcular_bonus(self):


        return self.salario * Funcionario.taxa_bonus

print("-"*40)
print("Cadastro de Funcionário (1/2)")
print("-"*40)

nome_a = input("Nome do funcionário A: ")
cargo_a = input("Cargo do funcionário A:")
salario_a = input("Salário (Apenas números inteiros) do funcionario A:")

func_a = Funcionario(nome_a, cargo_a, salario_a)

print("\n" + "-"*40)
print("Cadastro de funcionário (2/2)")
print("-"*40)


nome_b = input("Nome do funcionario B:")
cargo_b = input("Cargo do funcionario B")
salario_b = input("Salario do funcionario B")

func_b = Funcionario(nome_b, cargo_b, salario_b)

print(f"Bonus de {func_a.nome}: R${func_a.calcular_bonus():}")

print(f"Bonus de {func_b.nome}: R${func_b.calcular_bonus():}")
