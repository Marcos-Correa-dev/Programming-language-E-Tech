while True:
    try:
        numero = int(input("Digite um número: "))
        print(10 / numero)
        break
    except ValueError:
        print("Erro: Digite um número ")
    except ZeroDivisionError:
        print("Erro: divisão por zero")