atriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

quadrada = True

n = len(matriz)

for linha in matriz:
    if len(linha) != n:
        quadrada = False

print(quadrada)
