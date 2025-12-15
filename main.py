from operações import dividir

try:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print(dividir(x, y))
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Digite apenas números.")
