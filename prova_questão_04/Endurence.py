# A nave Endurance precisa calcular a quantidade total de combustível necessária para várias
# missões de reconhecimento em sistemas estelares diferentes. Cada missão exige uma quantidade
# específica de unidades de combustível.

# Crie uma função em Python chamada calcula_combustivel que receba:
# 1. Um argumento posicional obrigatório: missoes_base (o número de missões fixas, por exemplo,
# 2).
# 2. Um número variável de argumentos usando *args: gastos_adicionais (uma série de números
# que representam as unidades extras de combustível necessárias para cada missão de
# reconhecimento).
# A função deve:
#  Considerar que cada missão fixa (missoes_base) gasta 100 unidades de combustível.
#  Usar um laço de repetição para somar todos os valores em gastos_adicionais.
#  Calcular o total geral (combustível das missões fixas + gastos adicionais).
#  Imprimir (usando print) o total de combustível necessário.
#  calcula_combustivel(2, 50, 25, 10) – utilize esses valores, já supõe que tem 2 missões fixas e
# os gastos adicionais são 50, 25 e 10 unidades
#  Extra (Considere fazer com input)

def calcular_combustivel(missoes_base, *gastos_adicionais):

    combustivel_base = missoes_base * 100

    total_adicional = 0
    for gasto in gastos_adicionais:
        total_adicional += gasto

    total_geral = combustivel_base + total_adicional
    print(f"Total de combustivel necessário: {total_geral}")

calcular_combustivel(2, 50,25,10)

# outout: 287