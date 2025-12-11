def calular_combustivel(missoes_base, *gastos_adicionais):
    combustivel_base = missoes_base * 100

    soma_adicionais = 0

    for gastos in gastos_adicionais:
        soma_adicionais += gastos

    total = combustivel_base + soma_adicionais
    print(f"Total do combustivel necessário: {total}")

missoes = int(input("Digite o número de missões base: "))

gastos_fixos = (50,25,10)

calular_combustivel(missoes, *gastos_fixos)
