idade = int(input("Digite sua idade:"))

# ----- estrutura de decisão ---

if idade >= 18:
    # A pessoa é maior de idade, Aqui a CNH é uma possibilidade.

    entrada_carteira = input("Você tem CNH {SIM/Não}:").lower()
    tem_carteira = (entrada_carteira == "sim")

    if tem_carteira:
        print("Resultado: Você é maior de idade e tem CNH. pode dirigir.")
    else:
        print("Resultado: VocÊ é maior de idade mas não tem CNH, você não pode dirigir.")
else:

    entrada_carteira = input("Você tem CNH? (SIM/Não):").lower()

    if entrada_carteira == "não":
        print(
        "Resultado: você é menor de idade ({} anos). Não pode dirigir.".format(idade)
        )
    else:
        print("Resultado: Você é menor de idade ({} anos) e não pode dirigir.".format(idade))