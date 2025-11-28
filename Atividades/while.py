for i in range(1, 21):
    # condição de pular (continue)
    if i % 3 == 0:
        continue #  Se for divisivel por 3, volta ao inicio

    # condição para PARAR (BREAK)
    if i == 17:
        print("Chegamos ao 17. Parando o laço")
        break

    print(i)