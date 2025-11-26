idade = int(input("Digite a sua idade: "))

# --- Estrutura de Decisão para Dirigir ---

if idade >= 18:
    # A pessoa é maior de idade, AQUI a CNH é uma possibilidade.

    entrada_carteira = input("Você tem CNH? (sim/nao): ").lower()
    tem_carteira = (entrada_carteira == "sim")

    if tem_carteira:
        print("Resultado: Você é maior de idade E tem CNH. Você pode dirigir.")
    else:
        print(" Resultado: Você é maior de idade, mas NÃO tem CNH. Você não pode dirigir legalmente.")
else:
    # A pessoa é menor de idade. Não há necessidade de perguntar sobre CNH.

    # Podemos testar o 'mentiroso' aqui, se quisermos mostrar a impossibilidade:
    entrada_carteira = input("Você tem CNH? (sim/nao): ").lower()

    if entrada_carteira == "sim":
        print(
            "ALERTA: Você é menor de idade ({} anos). Não é legalmente possível ter CNH. Você está mentindo!".format(
                idade))
    else:
        print("Resultado: Você é menor de idade ({} anos) e não pode dirigir.".format(idade))