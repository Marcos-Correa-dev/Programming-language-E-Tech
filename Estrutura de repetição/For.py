
# frutas = ["maça", "banana", "cereja"]
# for fruta in frutas:
#          print(fruta)


# interando 'range' para repetir um bloco de código  5 vezes

# for i in range(5):
#     print("Interação:", i)


# enumerate() é últil para interar sobre uma sequência e, ao mesmo tempo, manter
# um contador automático (indice)
frutas = ["maçã", "banana", "cereja"]
for indice, fruta in enumerate(frutas):
    print(f"Fruta {indice}: {fruta}")