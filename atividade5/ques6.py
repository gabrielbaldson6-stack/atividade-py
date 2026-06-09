while True:
    nome = input("Atleta: ")

    if nome == "":
        break

    saltos = []

    for i in range(5):
        saltos.append(float(input(f"Salto {i+1}: ")))

    melhor = max(saltos)
    pior = min(saltos)

    saltos.remove(melhor)
    saltos.remove(pior)

    media = sum(saltos) / 3

    print("Melhor salto:", melhor)
    print("Pior salto:", pior)
    print("Média:", round(media,2))
