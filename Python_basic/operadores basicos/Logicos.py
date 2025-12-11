# O operador and retorna True (Verdadeiro)
# somente se ambas as condições comparadas
# forem True.

# idade = 19  # int
# possui_cnh = True  ## booleano
#
# # A pessoa é maior de idade E possui CNH?
# if idade >= 18 and possui_cnh == True:
#     print("Apto a dirigir legalmente.")
# else:
#     print("Não está apto.")
# Output neste caso: Apto a dirigir legalmente.


# O operador or retorna True se pelo menos
# uma das condições comparadas for True.
# Só retorna False se ambas forem False.
# Sintaxe: condição1 or condição2
# #
# # Regra: False se False ou False, senão é True


dia = "Sábado"
feriado = False  # booleano

# É final de semana OU é feriado?
if dia == "Sábado" or dia == "Domingo" or feriado == True:
    print("É dia de folga!")
else:
    print("Dia útil.")
# Output neste caso: É dia de folga!




