while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            break
        else:
            print("Valor inválido! A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Por favor, digite um número válido.")

print(f"Nota registrada: {nota}")
