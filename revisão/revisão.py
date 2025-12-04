# Crie a função calcular_custo_total que aceita
# um custo fixo obrigatório e utiliza *args para
# receber os custos de itens variáveis.
# A função deve retornar o valor total somado.


def calcular_custo_total(custo_base, *itens_comprados):
    # Lógica: O custo total é o custo_base
    total_itens = 0

    for item in itens_comprados:
        total_itens += item

    custo_final = custo_base + total_itens
    return custo_final

custo_do_pedido = calcular_custo_total(25.0, 10.0, 25.00, 5.0)
print(f"Custo total do pedido: {custo_do_pedido}")