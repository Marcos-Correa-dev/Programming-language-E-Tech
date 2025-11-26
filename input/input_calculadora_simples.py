# Exemplo de calculadora básica com input
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {subtracao}")
print(f"{numero1} × {numero2} = {multiplicacao}")

# Divisão com tratamento de erro
try:
    divisao = numero1 / numero2
    print(f"{numero1} ÷ {numero2} = {divisao}")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
