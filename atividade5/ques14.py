lin = int(input())
col = int(input())

matriz = []

for i in range(lin):
    matriz.append(list(map(int, input().split())))

transposta = []

for j in range(col):
    linha = []

    for i in range(lin):
        linha.append(matriz[i][j])

    transposta.append(linha)

for linha in transposta:
    print(linha)
