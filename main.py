# importa a classe Funcionario do modulo funcionario.py
from funcionario import Funcionario

# Lista que irá armazenar os objetos Funcionario
funcionarios = []

# Variável para acumular o total da folha de pagamento
total_folha = 0

# Quantidade de funcionarios a cadastrar
quantidade = int(input("Quantos funcionários deseja cadastrar ? "))

# Laço para cadastrar vários funcionários
for i in range(quantidade):
    print(f"\nCadastro do Funcionário {i+1}")

    # Leitura do nome
    nome = input("Digite o nome do funcionário: ")

    # Laço para validar o salário usando exceções
    while True:
        try:
            # Tenta converter o salário para float
            salario = float(input("Digite o salário do funcionario: "))

            if salario < 0:
                print("O salário não pode ser negativo")
            else:
                break  # sai do laço de repetição se estiver correto
        except ValueError:
            # obriga a escrever um numero
            print("Erro: Digite um valor número para salário")

    # Criação do objeto Funcionario
    funcionario = Funcionario(nome, salario)

    # Adiciona o objeto na lista
    funcionarios.append(funcionario)


print("\n FOLHA DE PAGAMENTO\n")

for funcionario in funcionarios:

    # Polimorfismo: chamando o método calcular_salario
    total_folha += funcionario.calcular_salario()

print("Total da folha de pagamento: ", total_folha)