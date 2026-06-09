lin = int(input())
col = int(input())

matriz = []

for i in range(lin):
    linha = []

    for j in range(col):
        linha.append(i * j)

    matriz.append(linha)

for linha in matriz:
    print(linha)
