n = int(input("Ordem da matriz: "))

matriz = []

for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

principal = 0
secundaria = 0

for i in range(n):
    principal += matriz[i][i]
    secundaria += matriz[i][n-1-i]

print("Diagonal principal:", principal)
print("Diagonal secundária:", secundaria)
