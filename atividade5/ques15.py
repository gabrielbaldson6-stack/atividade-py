lin = int(input())
col = int(input())

matriz = []

for i in range(lin):
    matriz.append(list(map(int, input().split())))

maior = max(max(linha) for linha in matriz)
menor = min(min(linha) for linha in matriz)

print("Maior:", maior)
print("Menor:", menor)
