def calcula_combustivel(missoes_base, *gastos_adicionais):
    combustivel_base = missoes_base * 100

    soma_adicionais = 0
    for gasto in gastos_adicionais:
        soma_adicionais += gasto

    total = combustivel_base + soma_adicionais
    print(f"Total de combustível necessário: {total} unidades")


missoes = int(input("Digite o número de missões base: "))

gastos_fixos = (50, 25, 10)

calcula_combustivel(missoes, *gastos_fixos)

