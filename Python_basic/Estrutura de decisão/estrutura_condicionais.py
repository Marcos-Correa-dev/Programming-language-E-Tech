#
# # Definindo uma variável
# idade = 20
#
# if idade >=18:
#     # Código executado se a condição for verdadeira
#     print("Você é maior de idade")
# elif 13 <= idade < 18:
#     # Código executado se o primeiro if der falso
#     print("Você é adolescente")
# else:
#     # Código executado se todas as condições anteriores derem falsas.
#     print("você é menor de idade")

# exemplo com múltiplas condições e operadores lógicos

# numero = 10
#
# if numero > 0 and numero % 2 == 0:
#     print("O numero é positivo e par.")
# elif numero > 0 and numero % 2 != 0:
#     print("O numero é positivo e impar.")
# else:
#     print("O numero é zero ou negativo.")


# Exemplo de estrutura aninhada

idade = 20
tem_CNH = True

if idade >= 18:
    if tem_CNH:
        print("Você pode dirigir.")
    else:
        print("você não pode dirigir.")
else:
    print("Você é menor de idade e não deve dirigir.")